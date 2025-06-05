from flask import Flask, render_template, request, jsonify
from notion_utils import carregar_faq_do_notion, encontrar_resposta_semantica
from ollama import Client as OllamaClient

app = Flask(__name__)
ollama = OllamaClient()
modelo = "gemma3:4b"

# Carregar a base de FAQ do Notion ao iniciar a aplicação
base_faq, documents = carregar_faq_do_notion()

def gerar_prompt(pergunta, formato, contexto):
    instrucoes = {
        "whatsapp": "Responda de forma curta, simpática e informal, como uma mensagem para WhatsApp.",
        "email": "Responda de forma educada, detalhada e profissional, como se fosse um e-mail formal para um cliente."
    }

    return f"""
Você é um assistente de atendimento ao cliente. Abaixo está uma base de conhecimento da empresa:

\"\"\"{contexto}\"\"\"

Com base nisso, responda à pergunta do cliente:
\"\"\"{pergunta}\"\"\"

Formato da resposta: {formato.upper()}
Instruções: {instrucoes[formato]}
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.json
    pergunta = data.get('pergunta')
    formato = data.get('formato', 'whatsapp')

    if not pergunta:
        return jsonify({'erro': 'Pergunta não fornecida'}), 400

    resposta_base = encontrar_resposta_semantica(pergunta, base_faq, documents)
    if not resposta_base:
        return jsonify({'erro': 'Não encontrei nenhuma resposta para essa pergunta'}), 404

    prompt = gerar_prompt(pergunta, formato, resposta_base)
    resposta = ollama.chat(
        model=modelo,
        messages=[{"role": "user", "content": prompt}]
    )["message"]["content"]

    return jsonify({
        'resposta': resposta,
        'formato': formato
    })

if __name__ == '__main__':
    app.run(debug=True) 