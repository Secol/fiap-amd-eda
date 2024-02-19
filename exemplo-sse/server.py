from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import time
import uvicorn

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Monta um diretório como um local para servir arquivos estáticos, acessíveis em '/static'
# Útil para servir o cliente JavaScript, CSS, imagens, etc.
app.mount("/static", StaticFiles(directory="./"), name="static")

# Configura a política CORS para a aplicação
# Isso permite que a aplicação seja acessada de diferentes origens (domínios)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens acessarem a aplicação
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos HTTP
)

def event_stream():
    """Gera um stream de eventos SSE, enviando uma mensagem a cada segundo."""
    count = 0
    while True:
        time.sleep(1)  # Espera 1 segundo antes de enviar a próxima mensagem
        count += 1  # Incrementa o contador para a próxima mensagem
        yield f"data: Message {count}\n\n"  # Formato SSE: 'data: <message>\n\n'

# Define um endpoint GET que retorna um stream de eventos SSE
@app.get("/events")
def events():
    # Retorna uma resposta de streaming usando o gerador event_stream()
    # 'text/event-stream' é o tipo de mídia para SSE
    return StreamingResponse(event_stream(), media_type="text/event-stream")

# Ponto de entrada para executar a aplicação com o Uvicorn como servidor ASGI
# Especifica o host, porta e nível de log, e habilita o modo de recarga para desenvolvimento
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
