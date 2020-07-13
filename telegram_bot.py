import telebot
from telebot import types
import xlsxwriter
import time

TOKEN = 'Не могу показать'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Приветствуем вас в боте своей игры \n "
                                      "Введите название команды:")
    bot.register_next_step_handler(message, enter_team_name)


def enter_team_name(message):
    team_name = message.text
    msg = bot.send_message(message.chat.id, text='Nazvanie komandi: %s' % team_name)
    bot.register_next_step_handler(msg, menu)


def menu(message):
    # Отрисовка клавиатуры
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    butt1 = types.KeyboardButton('Theme1')
    butt2 = types.KeyboardButton('Theme2')
    butt3 = types.KeyboardButton('Theme3')
    butt4 = types.KeyboardButton('Theme4')
    butt5 = types.KeyboardButton('Theme5')
    butt6 = types.KeyboardButton('Theme6')

    list_of_buttons = [butt1, butt2, butt3, butt4, butt5, butt6]
    list_of_buttons = {'butt1', 'butt2', 'butt3', 'butt4', 'butt5', 'butt6'}
    menu_markup.add(list_of_buttons)
    bot.send_message(message.chat.id, reply_markup=menu_markup, text='Viberite temu')
    bot.register_next_step_handler(message, theme_commutation)


def theme_commutation(message):
    if message.text == 'Theme1':
        first_theme(message)
    if message.text == 'Theme2':
        second_theme(message)
    if message.text == 'Theme3':
        third_theme(message)
    if message.text == 'Theme4':
        fourth_theme(message)
    if message.text == 'Theme5':
        fifth_theme(message)
    if message.text == 'Theme6':
        sixth_theme(message)


def first_theme(message, theme1=types.KeyboardButton('100'),
                theme2=types.KeyboardButton('200'),
                theme3=types.KeyboardButton('300'),
                theme4=types.KeyboardButton('400'),
                theme5=types.KeyboardButton('500')):
    func_name = first_theme_questions
    nominal_menu(message, func_name, theme1, theme2, theme3, theme4, theme5)


def second_theme(message):
    bot.send_message(message.chat.id, text='Тема 2')
    bot.register_next_step_handler(message, menu)


def third_theme(message):
    bot.send_message(message.chat.id, text='Тема 3')
    bot.register_next_step_handler(message, menu)


def fourth_theme(message):
    bot.send_message(message.chat.id, text='Тема 4')
    bot.register_next_step_handler(message, menu)


def fifth_theme(message):
    bot.send_message(message.chat.id, text='Тема 5')
    bot.register_next_step_handler(message, menu)


def sixth_theme(message):
    bot.send_message(message.chat.id, text='Тема 6')
    bot.register_next_step_handler(message, menu)


def nominal_menu(message, func_name,
                 theme1=types.KeyboardButton('100'),
                 theme2=types.KeyboardButton('200'),
                 theme3=types.KeyboardButton('300'),
                 theme4=types.KeyboardButton('400'),
                 theme5=types.KeyboardButton('500')):


    nominal_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    nominal_menu_markup.add(theme1, theme2, theme3, theme4, theme5)
    bot.send_message(message.chat.id, reply_markup=nominal_menu_markup, text='Выберите номинал')
    bot.register_next_step_handler(message, func_name)




def first_theme_questions(message):
    theme1 = [
        'Theme1Question1',
        'Theme1Question2',
        'Theme1Question3',
        'Theme1Question4',
        'Theme1Question5'
    ]

    if message.text == '100':
        bot.send_message(message.chat.id, text=theme1[0])
        bot.register_next_step_handler(message, first_theme)

    if message.text == '200':
        bot.send_message(message.chat.id, text=theme1[1])
        bot.register_next_step_handler(message, first_theme)

    if message.text == '300':
        bot.send_message(message.chat.id, text=theme1[2])
        bot.register_next_step_handler(message, first_theme)

    if message.text == '400':
        bot.send_message(message.chat.id, text=theme1[3])
        bot.register_next_step_handler(message, first_theme)

    if message.text == '500':
        bot.send_message(message.chat.id, text=theme1[4])
        bot.register_next_step_handler(message, first_theme)


@bot.message_handler(content_types=['text'])
def other_text_handler(message):
    bot.send_message(message.chat.id, 'vipolnilsya std handler')
    if message.text == 'недоступно':
        bot.send_message(message.chat.id, 'idi naxyi')
        bot.register_next_step_handler(message, menu)
    bot.register_next_step_handler(message, menu)


# Запуcк
bot.polling(none_stop=True)
