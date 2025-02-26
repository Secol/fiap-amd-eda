# Importando as bibliotecas necessárias:
# FastAPI para a criação da API e uvicorn para o servidor ASGI.
from fastapi import FastAPI, Request
import uvicorn

# Cria uma instância do aplicativo FastAPI.
app = FastAPI()

# Define um endpoint na raiz ("/") que aceita apenas solicitações POST.
# Este endpoint atua como um receptor de eventos.
@app.post("/")
async def event_receiver(request: Request):
    # A função async permite o processamento assíncrono, melhorando a performance.
    # Extrai os dados JSON da solicitação recebida.
    event_data = await request.json()
    
    # Imprime os dados do evento no console para fins de debug.
    # Isso é útil para verificar se os eventos estão sendo recebidos corretamente.
    print("Evento recebido:", event_data)
    
    # Responde à solicitação com uma mensagem de sucesso em formato JSON.
    return {"message": "Evento recebido com sucesso!"}

# Um bloco condicional que verifica se este script é o ponto de entrada principal.
if __name__ == "__main__":
    # Se for o caso, o servidor Uvicorn é iniciado com este aplicativo FastAPI.
    # Configura o servidor para escutar em todas as interfaces de rede (0.0.0.0) na porta 8001.
    # Isso permite que o servidor seja acessível em sua rede local.
    uvicorn.run(app, host="0.0.0.0", port=8001)