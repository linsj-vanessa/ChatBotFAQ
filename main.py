from notion_utils import carregar_faq_do_notion, encontrar_resposta_semantica
from ollama import Client as OllamaClient

ollama = OllamaClient()
modelo = "mistral:latest"

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

def main():
    print("🤖 Central de Atendimento (FAQ + IA Local)")
    print("Formato disponível: whatsapp / email\nDigite 'sair' para encerrar.\n")

    base_faq, documents = carregar_faq_do_notion()

    while True:
        formato = input("Formato desejado (whatsapp ou email): ").strip().lower()
        if formato == "sair":
            break
        if formato not in ["whatsapp", "email"]:
            print("❌ Formato inválido. Tente novamente.")
            continue

        pergunta = input("Digite a pergunta do cliente: ").strip()
        if pergunta.lower() == "sair":
            break

        resposta_base = encontrar_resposta_semantica(pergunta, base_faq, documents)
        if not resposta_base:
            print("❌ Não encontrei nenhuma resposta para essa pergunta. Atualize o Notion ou refine sua pergunta.\n")
            continue

        prompt = gerar_prompt(pergunta, formato, resposta_base)

        resposta = ollama.chat(
            model=modelo,
            messages=[{"role": "user", "content": prompt}]
        )["message"]["content"]

        print(f"\n📬 Resposta gerada ({formato}):\n{resposta}\n")

if __name__ == "__main__":
    main()
