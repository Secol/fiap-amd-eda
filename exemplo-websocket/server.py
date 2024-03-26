from fastapi import FastAPI, WebSocket  # Importa as classes FastAPI e WebSocket
from fastapi.staticfiles import StaticFiles  # Importa a classe StaticFiles para servir arquivos estáticos
from fastapi.responses import HTMLResponse  # Importa a classe HTMLResponse para enviar respostas HTML
import uvicorn  # Importa o servidor ASGI uvicorn para rodar a aplicação
from uuid import uuid4  # Importa a função uuid4 para gerar identificadores únicos

app = FastAPI()  # Cria uma instância do aplicativo FastAPI

# Monta um diretório como um local para servir arquivos estáticos, acessíveis em '/static'
# Útil para servir o cliente JavaScript, CSS, imagens, etc.
app.mount("/static", StaticFiles(directory="./"), name="static")

# Dicionário para manter as conexões WebSocket ativas, identificadas por um UUID
connections = {}

# Define um endpoint WebSocket no caminho "/ws"
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # Aceita a conexão WebSocket
    connection_id = str(uuid4())  # Gera um ID único para a conexão
    connections[connection_id] = websocket  # Armazena a conexão usando o ID como chave

    try:
        # Envia uma mensagem de boas-vindas ao cliente, incluindo o ID único da conexão
        await websocket.send_text(f"Você está conectado com o ID: {connection_id}")
        
        # Loop infinito para receber mensagens do cliente
        while True:
            data = await websocket.receive_text()  # Aguarda por uma mensagem do cliente
            message = f"{connection_id} diz: {data}"  # Monta a mensagem a ser enviada para todos
            
            # Envia a mensagem recebida para todas as conexões ativas
            for conn_id, conn_websocket in connections.items():
                await conn_websocket.send_text(message)
    except Exception as e:
        # Opcional: tratamento de exceções específicas pode ser adicionado aqui
        pass
    finally:
        # Garante que a conexão seja removida do dicionário e fechada adequadamente ao desconectar
        del connections[connection_id]
        await websocket.close()

# Se este arquivo for executado como script principal, inicia o servidor usando o uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Configurações do servidor, como host e porta