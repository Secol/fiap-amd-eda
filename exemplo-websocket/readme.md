
# Chat Online com FastAPI e WebSockets

Este projeto é um exemplo simples de chat online que utiliza FastAPI para o backend e WebSockets para comunicação em tempo real entre o servidor e os clientes. O frontend é construído com HTML, CSS e JavaScript puro para demonstrar a funcionalidade de WebSockets em um ambiente de chat.

## Características

- **Comunicação em tempo real**: Utiliza WebSockets para troca de mensagens em tempo real.
- **Layout fluido**: O design responsivo se adapta a diferentes tamanhos de tela.
- **ID único para usuários**: Cada usuário recebe um ID único ao se conectar, melhorando a identificação nas conversas.

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)**: Para criar o backend e gerenciar as conexões WebSocket.
- **[Uvicorn](https://www.uvicorn.org/)**: Como servidor ASGI para servir a aplicação FastAPI.
- **HTML/CSS/JavaScript**: Para o frontend e interação com WebSockets.

## Instalação

Certifique-se de ter o Python 3.12+ instalado no seu sistema. Então, siga os passos abaixo para configurar o ambiente do projeto:

1. Clone este repositório para o seu local de trabalho:

2. Navegue até a pasta do projeto e instale as dependências usando `pip`:
   ```bash
   cd caminho/para/o/projeto
   pip install -r requirements.txt
   ```

3. Inicie o servidor FastAPI:
   ```bash
   python server.py
   ```

## Uso

Após iniciar o servidor, abra um navegador e vá para `http://localhost:8000/static/index.html` para acessar a interface do chat. Você pode abrir várias abas ou janelas no navegador para simular múltiplos usuários interagindo no chat.