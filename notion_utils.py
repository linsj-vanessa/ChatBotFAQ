import os
from dotenv import load_dotenv
from notion_client import Client
from sentence_transformers import SentenceTransformer
import numpy as np

# Forçando a recarga do arquivo .env
load_dotenv(override=True)

# Configurando o cliente Notion
notion = Client(auth=os.getenv("NOTION_KEY"))

def carregar_faq_do_notion():
    print("Tentando listar bancos de dados disponíveis...")
    databases = notion.search(filter={"property": "object", "value": "database"}).get("results", [])
    print(f"Bancos de dados encontrados: {len(databases)}")
    
    if not databases:
        raise Exception("Nenhum banco de dados encontrado no Notion")
    
    database_id = os.getenv("NOTION_DATABASE_ID")
    print(f"Tentando acessar o banco de dados {database_id}...")
    
    # Buscando as páginas do banco de dados
    pages = notion.databases.query(database_id=database_id, page_size=100).get("results", [])
    print(f"Número de resultados encontrados: {len(pages)}")
    
    # Extraindo perguntas e respostas
    base_faq = {}
    documents = []
    
    for page in pages:
        props = page.get("properties", {})
        pergunta = props.get("Pergunta", {}).get("title", [{}])[0].get("text", {}).get("content", "")
        resposta = props.get("Resposta", {}).get("rich_text", [{}])[0].get("text", {}).get("content", "")
        
        if pergunta and resposta:
            base_faq[pergunta] = resposta
            documents.append(f"Pergunta: {pergunta}\nResposta: {resposta}")
    
    return base_faq, documents

def encontrar_resposta_semantica(pergunta_usuario, base_faq, documents):
    # Carregar o modelo de embeddings
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    # Calcular embeddings para a pergunta do usuário
    pergunta_embedding = model.encode(pergunta_usuario)
    
    # Calcular embeddings para todas as perguntas da base
    perguntas_embeddings = model.encode(list(base_faq.keys()))
    
    # Calcular similaridade de cosseno
    similaridades = np.dot(perguntas_embeddings, pergunta_embedding) / (
        np.linalg.norm(perguntas_embeddings, axis=1) * np.linalg.norm(pergunta_embedding)
    )
    
    # Encontrar a pergunta mais similar
    idx_mais_similar = np.argmax(similaridades)
    pergunta_mais_similar = list(base_faq.keys())[idx_mais_similar]
    
    # Retornar a resposta correspondente
    return base_faq[pergunta_mais_similar]

def encontrar_resposta_simples(pergunta_usuario, base_faq):
    # Busca exata
    pergunta_usuario = pergunta_usuario.lower()
    for pergunta, resposta in base_faq.items():
        if pergunta_usuario in pergunta.lower():
            return resposta
    return None
