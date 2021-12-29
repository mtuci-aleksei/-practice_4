import telebot
import sqlite3


bot = telebot.TeleBot('token')


@bot.message_handler(commands=["start"])
def start(message):
    id = str(message.chat.id)
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton('ПОНЕДЕЛЬНИК'))
    keyboard.add(telebot.types.KeyboardButton('ВТОРНИК'))
    keyboard.add(telebot.types.KeyboardButton('СРЕДА'))
    keyboard.add(telebot.types.KeyboardButton('ЧЕТВЕРГ'))
    keyboard.add(telebot.types.KeyboardButton('ПЯТНИЦА'))
    keyboard.add(telebot.types.KeyboardButton('СУББОТА'))
    bot.send_message(id, 'ВЫБЕРИ ДЕНЬ НЕДЕЛИ', reply_markup=keyboard)


@bot.message_handler()
def handle_text(message):
    id = str(message.chat.id)
    week = {'ПОНЕДЕЛЬНИК': 'monday', 'ВТОРНИК': 'tuesday', 'СРЕДА': 'wednesday', 'ЧЕТВЕРГ': 'thursday', 'ПЯТНИЦА': 'friday', 'СУББОТА': 'saturday'}
    base = sqlite3.connect('base.db')
    cursor = base.cursor()
    if message.text in week:
        lessons = cursor.execute('select * from timetable where day=?', (week[message.text],)).fetchall()
        text = ''
        for lesson in lessons:
            text += f'**{lesson[2]}**\nКабинет: {lesson[3]}\nНачало в {lesson[4]}\n\n'
        bot.send_message(id, text, parse_mode='MarkdownV2')


if __name__ == '__main__':
    bot.polling(none_stop=True)
