import telebot, logging

owner = 205529605
bot = telebot.TeleBot('5992639409:AAHoNN7SrAY7t6sVanHvBuW3tYmjHtGyxGQ')

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


@bot.message_handler(commands=["ping"])
def start(message):
    try:
        bot.send_message(message.chat.id, "PONG!", parse_mode="HTML")
    except:
        bot.send_message(owner, 'Что-то пошло не так')


@bot.message_handler(content_types=["text", "photo", "video"])
def messages(message):
    if int(message.chat.id) == owner:
        try:
            bot.send_message(message.chat.id, 'Сообщение от администратора получено')
        except:
            bot.send_message(owner, 'Что-то пошло не так! Бот продолжил работу.')
    else:
        pass
    try:
        bot.forward_message(owner, message.chat.id, message.message_id)
        bot.send_message(message.chat.id,
                         str(message.from_user.first_name) + ',' + ' я получил сообщение и очень скоро на него отвечу :)')
    except:
        bot.send_message(owner, 'Что-то пошло не так! Бот продолжил работу.')


bot.polling(non_stop=True)
