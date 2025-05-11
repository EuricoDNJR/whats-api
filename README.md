# WhatsApp Cloud API - FastAPI Integration

Esta aplicação é uma API REST construída com FastAPI que envia e recebe mensagens utilizando a **API Cloud do WhatsApp** (via Meta).

---

📌 Requisitos

- Python 3.9+
- Conta de desenvolvedor Meta com número de teste no WhatsApp Cloud API
- Token de acesso e ID do número do WhatsApp configurados no `.env`

---

📌 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/whatsapp-fastapi.git
   cd whatsapp-fastapi
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais:

   ```
   WHATSAPP_TOKEN=seu_token_de_acesso
   PHONE_NUMBER_ID=seu_id_de_numero
   VERIFY_TOKEN=seu_token_de_verificacao
   ```

4. Rode a aplicação:
   ```bash
   uvicorn main:app --reload
   ```

🚀 Rotas disponíveis:

- `POST /send_message`: Envia uma mensagem para um número de telefone específico.
- `POST /webhook`: Validação inicial do Webhook (usado pelo Meta para confirmação).
- `GET /webhook`: Endpoint para receber mensagens do WhatsApp.

> ⚠️ **Atenção:**
>
> - O Webhook deve ser configurado no painel do WhatsApp Cloud API para receber mensagens.

💡 Dica:

- Voce pode usar o [ngrok](https://ngrok.com/) para expor sua aplicação localmente e testar o Webhook.

  Assim que o ngrok estiver instalado e configurado, execute o seguinte comando:

  ```bash
  ngrok http 8000
  ```

  Isso irá gerar um URL público que você pode usar para configurar o Webhook no painel do WhatsApp Cloud API.
  No painel, vá para a seção de Webhooks e adicione o URL gerado pelo ngrok seguido do endpoint `/webhook`. Por exemplo:

  ```
  https://seu-url-ngrok.ngrok.io/webhook
  ```

  Certifique-se de que o método HTTP esteja definido como `POST` e que o token de verificação corresponda ao que você definiu no arquivo `.env`.

  Após adicionar o Webhook, clique em "Verificar e salvar". O Meta enviará uma solicitação para o seu endpoint com o token de verificação. Se tudo estiver correto, você verá uma mensagem de sucesso.

  Depois de configurar o Webhook, você pode testar enviando mensagens para o número do WhatsApp associado à sua conta de desenvolvedor Meta.

Logs:

📝 Logs

Os logs são salvos em `app/logs/` com as seguintes informações:

- Método HTTP
- Endpoint acessado
- Payload enviado
- Resposta da API
- Erros (se houver)

---

📚 Documentação:

- [FastAPI](https://fastapi.tiangolo.com/)
- [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api)
- [ngrok](https://ngrok.com/)
