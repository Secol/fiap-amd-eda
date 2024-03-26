# Importando as dependências necessárias.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import httpx
import uuid
import uvicorn

# Cria uma instância da aplicação FastAPI.
app = FastAPI()

# Inicializa um dicionário para armazenar as subscrições dos eventos.
subscriptions = {}

# Define um modelo Pydantic para os eventos que serão recebidos e enviados.
class Event(BaseModel):
    event_type: str  # O tipo do evento.
    data: str  # Os dados do evento, armazenados como string.

# Define um modelo Pydantic para as subscrições, incluindo o tipo de evento e a URL de callback.
class Subscription(BaseModel):
    event_type: str  # O tipo do evento ao qual se inscrever.
    callback_url: HttpUrl  # A URL de callback para onde os eventos serão enviados.

# Endpoint para permitir a subscrição a eventos específicos.
@app.post("/subscribe")
async def subscribe(subscription: Subscription):
    # Gera um ID único para a subscrição.
    subscription_id = str(uuid.uuid4())
    # Cria um dicionário para o tipo de evento se ainda não existir.
    if subscription.event_type not in subscriptions:
        subscriptions[subscription.event_type] = {}
    # Armazena a URL de callback sob o ID de subscrição no dicionário de eventos.
    subscriptions[subscription.event_type][subscription_id] = subscription.callback_url
    # Retorna o ID de subscrição ao cliente.
    return {"subscription_id": subscription_id}

# Endpoint para permitir o cancelamento da subscrição usando o ID de subscrição.
@app.delete("/unsubscribe/{subscription_id}")
async def unsubscribe(subscription_id: str):
    # Procura e remove a subscrição correspondente ao ID fornecido.
    for event_type in subscriptions:
        if subscription_id in subscriptions[event_type]:
            del subscriptions[event_type][subscription_id]
            return {"message": "Unsubscribed successfully"}
    # Se a subscrição não for encontrada, retorna um erro.
    raise HTTPException(status_code=404, detail="Subscription not found")

# Endpoint para receber eventos e notificar os inscritos.
@app.post("/webhook")
async def webhook_receiver(event: Event):
    # Verifica se existem subscrições para o tipo de evento recebido.
    if event.event_type in subscriptions:
        # Para cada inscrição, envia o evento para a URL de callback.
        for subscription_id, callback_url in subscriptions[event.event_type].items():
            # Converte a URL de callback em uma string.
            str_callback_url = str(callback_url)
            async with httpx.AsyncClient() as client:
                # Prepara o objeto a ser enviado, incluindo o ID da subscrição e o evento.
                object = {
                    'subscription_id': subscription_id,
                    'event': event.dict()
                }
                # Faz uma requisição POST para a URL de callback com o objeto do evento.
                await client.post(str_callback_url, json=object)
    # Retorna uma mensagem indicando que o evento foi processado.
    return {"message": "Event processed"}

# Se o script for executado diretamente, inicia o servidor Uvicorn na porta 8000.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)