from flask import Flask, request, jsonify
import random
import telebot

# Конфигурация Flask и Telegram Bot
app = Flask(__name__)
SECRET_TOKEN = "token was here"
BOT_TOKEN = "token was here"
bot = telebot.TeleBot(BOT_TOKEN)
print("Checking tokens...")
# Ключевые слова
keywords = {
    'alan@sms.ru': '@alan3c',
    'stas2@sms.ru': '@Leofromufa',
    'stas1@sms.ru': '@Leofromufa',
    'nastya@sms.ru': '@zxcPolpiramida',
    'Art_East@gmail.com': '@iirinovna',
    'olesya@sms.ru': '@Malessia3',
    'toha@sms.ru': '@sliperslipknot',
    'kolyan_2@gmail.com': '@Re1ocate',
    'kolyan\\_2@gmail.com': '@Re1ocate'
}
print("Dictionaries loaded...")
# Список случайных фраз
replies_pool = [
    "глянь-ка.",
    "о, а вот этот тебе.",
    "опять работа.",
    "по-моему, это твоё.",
    "шо там?",
    "надо бы посмотреть.",
    "взгляни.",
    "погляди.",
    "хоба.",
    "ну это твоё, ясное дело.",
    "а вот это твоё.",
    "не завершена аренда.",
    "ping.",
    "вжух, и прибавилось работы.",
    "лови.",
    "Ы",
    "тут прикол.",
    "снова работа.",
    "я бы сам посмотрел, но ты понимаешь, у меня лапки.",
    "делегирую это тебе",

]
print("Random replies loaded...")
# Маршрут для обработки сообщений
@app.route('/process_message', methods=['POST'])
def process_message():
    # Проверка токена
    token = request.headers.get("Authorization")
    print("Checking tokens...")
    if token != f"Bearer {SECRET_TOKEN}":
        print("UNAUTHORISED ACCESS ATTEMPT DETECTED!")
        return "Unauthorized", 403


    # Извлечение данных из запроса
    data = request.get_json()
    chat_id = data.get("chat_id")
    text = data.get("text", "").lower()  # Приводим текст к нижнему регистру
    if not chat_id or not text:
        print("Error: Invalid chat id or no text.")
        return jsonify({"error": "Invalid data"}), 400

    # Проверка ключевых слов
    for keyword, username in keywords.items():
        if keyword.lower() in text:
            random_message = random.choice(replies_pool)
            bot.send_message(chat_id, f"{username}, {random_message}")
            print(f"Sent message to {chat_id}: {username}, {random_message}")
            break
    else:
        print(f"No keyword found in message: {text}")

    return jsonify({"status": "processed"}), 200

# Запуск сервера
if __name__ == "__main__":
    from waitress import serve  # Более надежный сервер
    serve(app, host="0.0.0.0", port=5000)
    print("Waitress server online...")
