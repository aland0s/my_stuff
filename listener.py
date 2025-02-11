import asyncio
from telethon import TelegramClient, events
print("Initialising listener...")
# Конфигурация
API_ID = "apiid"  # Ваш API ID
API_HASH = "there was the hash"  # Ваш API Hash
FLASK_SERVER_URL = "http://127.0.0.1:5000/process_message"  # URL Flask-сервера
SECRET_TOKEN = "oYW42UN9-TcEBJYotEPAcEFLJkVvPhJ176AR0pP0Ajg"
print("Loaded tokens...")
# Создаем клиента
client = TelegramClient("listener_session", API_ID, API_HASH)
print("Client created...")
# Асинхронная функция отправки сообщений на сервер Flask
async def send_to_flask(chat_id, text):
    import aiohttp
    async with aiohttp.ClientSession() as session:
        try:
            headers = {"Authorization": f"Bearer {SECRET_TOKEN}"}  # Авторизация
            payload = {"chat_id": chat_id, "text": text}
            async with session.post(FLASK_SERVER_URL, json=payload, headers=headers) as response:
                if response.status != 200:
                    print(f"Error sending to Flask: {response.status}")
                else:
                    print(f"Message sent to Flask: {chat_id}, {text}")
        except Exception as e:
            print(f"Error during Flask communication: {e}")

# Обработчик новых сообщений
@client.on(events.NewMessage)
async def handle_new_message(event):
    try:
        chat_id = event.chat_id
        text = event.message.message.strip()  # Убираем лишние пробелы
        print(f"New message from {chat_id}: {text}")
        # Отправляем сообщение на Flask-сервер
        await send_to_flask(chat_id, text)
    except Exception as e:
        print(f"Error processing message: {e}")

# Запуск клиента
async def main():
    print("Starting Telegram Listener...")
    async with client:
        await client.run_until_disconnected()

asyncio.run(main())
