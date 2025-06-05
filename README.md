# 🤖 ChatBot FAQ com Notion e IA Local

Este projeto é um chatbot inteligente que combina uma base de conhecimento do Notion com processamento de linguagem natural e geração de texto usando IA local. O sistema permite respostas personalizadas em diferentes formatos (WhatsApp e Email) baseadas em uma FAQ estruturada.

> 💡 Este projeto foi inspirado no vídeo ["Como criar um ChatBot com Notion e IA Local"](https://www.youtube.com/watch?v=rOjusRRO1EI) da Asimov Academy.

## ✨ Funcionalidades

- 💬 Interface web moderna e responsiva
- 🔍 Busca semântica nas perguntas
- 🤖 Geração de respostas com IA local (Ollama)
- 📱 Múltiplos formatos de resposta (WhatsApp/Email)
- 📚 Base de conhecimento integrada com Notion
- 🎨 Design moderno com Tailwind CSS
- ⚡ Respostas em tempo real

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Flask
- Notion API
- Ollama (IA Local)
- Sentence Transformers
- Tailwind CSS
- JavaScript

## 📋 Pré-requisitos

1. Python 3.11 ou superior
2. Conta no Notion com uma base de dados configurada
3. Ollama instalado e rodando localmente
4. Modelo Gemma 3 4B baixado no Ollama

## 🔧 Configuração

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd chatBot
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
- Copie o arquivo `.env.example` para `.env`:
```bash
cp .env.example .env
```
- Edite o arquivo `.env` com suas credenciais:
```
NOTION_KEY=sua_chave_do_notion
NOTION_DATABASE_ID=id_do_seu_banco_de_dados
```

5. Configure o banco de dados no Notion:
- Crie um banco de dados com as colunas:
  - "Pergunta" (título)
  - "Resposta" (texto)

## 🚀 Executando o Projeto

1. Inicie o servidor Flask:
```bash
python app.py
```

2. Acesse a interface web:
```
http://localhost:5000
```

## 📝 Estrutura do Projeto

```
chatBot/
├── app.py              # Aplicação Flask
├── main.py            # Versão CLI do chatbot
├── notion_utils.py    # Utilitários para integração com Notion
├── requirements.txt   # Dependências do projeto
├── static/           # Arquivos estáticos
│   ├── css/         # Estilos CSS
│   └── js/          # Scripts JavaScript
└── templates/        # Templates HTML
```

## 👩‍💻 Desenvolvimento

1. **Configuração do Ambiente de Desenvolvimento**:
   - Instale as dependências de desenvolvimento:
   ```bash
   pip install -r requirements-dev.txt
   ```
   - Configure o pre-commit:
   ```bash
   pre-commit install
   ```

2. **Padrões de Código**:
   - Siga o PEP 8 para código Python
   - Use docstrings para documentar funções e classes
   - Mantenha o código organizado e bem comentado

3. **Testes**:
   - Execute os testes:
   ```bash
   pytest
   ```
   - Mantenha a cobertura de testes acima de 80%

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos

- [Asimov Academy](https://www.youtube.com/@AsimovAcademy) pelo vídeo inspirador ["Como criar um ChatBot com Notion e IA Local"](https://www.youtube.com/watch?v=rOjusRRO1EI)
- [Notion API](https://developers.notion.com/)
- [Ollama](https://ollama.ai/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Flask](https://flask.palletsprojects.com/)
