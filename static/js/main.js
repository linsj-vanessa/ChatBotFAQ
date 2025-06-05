let formatoAtual = 'whatsapp';

function selecionarFormato(formato) {
    formatoAtual = formato;
    
    // Remove a classe 'active' de todos os botões
    document.querySelectorAll('.formato-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Adiciona a classe 'active' apenas no botão selecionado
    const botaoSelecionado = document.querySelector(`[data-formato="${formato}"]`);
    if (botaoSelecionado) {
        botaoSelecionado.classList.add('active');
    }
}

function adicionarMensagem(texto, tipo) {
    const chatContainer = document.getElementById('chat-container');
    const mensagemDiv = document.createElement('div');
    mensagemDiv.className = `mensagem ${tipo}`;
    mensagemDiv.textContent = texto;
    chatContainer.appendChild(mensagemDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

async function enviarPergunta() {
    const inputPergunta = document.getElementById('pergunta');
    const pergunta = inputPergunta.value.trim();
    
    if (!pergunta) return;
    
    // Adiciona a pergunta do usuário ao chat
    adicionarMensagem(pergunta, 'mensagem-usuario');
    inputPergunta.value = '';

    try {
        const response = await fetch('/perguntar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                pergunta: pergunta,
                formato: formatoAtual
            })
        });

        const data = await response.json();

        if (response.ok) {
            adicionarMensagem(data.resposta, 'mensagem-bot');
        } else {
            adicionarMensagem(data.erro || 'Erro ao processar sua pergunta', 'mensagem-erro');
        }
    } catch (error) {
        adicionarMensagem('Erro ao conectar com o servidor', 'mensagem-erro');
    }
}

// Permite enviar a pergunta com a tecla Enter
document.getElementById('pergunta').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        enviarPergunta();
    }
});

// Inicializa o estado dos botões ao carregar a página
document.addEventListener('DOMContentLoaded', function() {
    selecionarFormato('whatsapp');
}); 