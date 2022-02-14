import telebot
import logging
import gc

logging.basicConfig(filename="./log.txt", level=logging.ERROR)

bot = telebot.TeleBot("<token_bot>")
gc.enable()


def sendMes(id,mes):
    """
    Функция, которая разбивает сообщение для отправки на сообщения, длина текста в которых 4000 символов или меньше.
    Необходима, так как в стандартной функции send_message возникает ошибка при отправлении сообщения длиной более 4000
    символов
    :param id:
    :param mes:
    :return:
    """
    if len(mes)>4000:
        bot.send_message(id,mes[:4000])
        sendMes(id,mes[4000:])
    else:
        bot.send_message(id, mes)


try:
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        bot.sendMes(message.from_user.id, message.text)


    bot.polling(none_stop=True, interval=1)
except Exception as e:
    logging.error("Error: "+str(e))

