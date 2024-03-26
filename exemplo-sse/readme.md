
# Projeto SSE com FastAPI e JavaScript

Este projeto demonstra a implementação de Server Sent Events (SSE) usando FastAPI no servidor e JavaScript puro no cliente. Ele permite que o servidor envie atualizações em tempo real para o navegador do cliente de forma eficiente e com baixa latência.

## Características

- **FastAPI** para criar um endpoint que transmite eventos em tempo real.
- Uso de **SSE (Server Sent Events)** para enviar mensagens do servidor para o cliente.
- Implementação de **CORS (Cross-Origin Resource Sharing)** para permitir requisições entre domínios diferentes.

## Pré-requisitos

Antes de iniciar, certifique-se de que você tem Python 3.12+ e pip instalados em seu sistema.

## Configuração do Ambiente

Para configurar o ambiente e instalar as dependências necessárias, siga os passos abaixo:

1. Clone o repositório para sua máquina local:

2. Navegue até o diretório do projeto:

   ```bash
   cd caminho-para-o-projeto
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Executando o Projeto

Para rodar o servidor FastAPI, execute o seguinte comando no diretório do projeto:

```bash
python server.py
```

O servidor iniciará na porta `8000`. Você pode acessar o endpoint SSE em `http://localhost:8000/events`.

Para visualizar o cliente, abra o arquivo `index.html` em seu navegador.

## Estrutura do Projeto

- `server.py`: Contém a lógica do servidor FastAPI, incluindo a configuração de CORS e o endpoint SSE.
- `index.html`: A página HTML que o usuário final interage.