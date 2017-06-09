# -*- coding: utf8 -*- 
# appmetrica 17890127-b2d9-419a-a75d-67f17939a7bc

import telebot
from telebot import types
import random

token = '316066244:AAHx-0Xs_KAotsQa8YSAKftqg7uTk-zdIIs'
bot = telebot.TeleBot(token)

eji = ['Этот вопрос - сложный вопрос, а Ежи и Петруччо они простые.', 'Где здесь право, а где лево?','Надо купить бубен.', 'Две и две трети ноги - это не так уж мало!', 'Надо прибавить четкости.', 'А дальше?', 'можно ли собаку посадить на стул?', 'Ежи - Ежино, а Петруччо - Петруччино.', 'Так держать!', 'Много всего, а класть некуда.', 'тот, кто задумался над этим вопросом, обречен на неудачу.', 'я Ежи, а ты Петруччо', 'собственно, не было выбора', 'одна река течет', 'одному нужна книга, а другому нет.', 'а Ежи не обиделся', 'далеко занесло Петруччо', 'От прибавленного к прибавочной, и прибавленному', 'Это «My Way»!', 'Покоя нет!', 'откуда ты это взял?']

petrucho = ['Есть река, она течет…', 'Сейчас брошу в тебя вилкой!', 'Нет Ежи, нет и Петруччо.', 'Не отвечал за свои поступки, потому что был собак.', 'Принести хурму!', 'Мы все вышли из одного мешка.', 'Дальше: лес, река, поле…', 'раз это так естественно происходит, то значит так оно и должно быть, а собаку тут нечего приплетать...', 'Пусть каждый решает сам. Ежи сам, а Петруччо тоже сам.', 'Слава тебе господи, что это не Билли Джонс!', 'Все вернулось на круги своя.', 'В чем тут закон?', 'Ориентируйся по звездам', 'я Петруччо', 'таков Петруччо', 'остались, фактически, только имена', 'бросить все, пойти в другой лес', 'там надо рыбу резать ножом', 'ну, а дальше уже не интересно', 'Есть жизнь за пределами Ежи и Петруччо.', 'сейчас время разбрасывать…']

@bot.message_handler(commands=['start'])
def start(m):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*[types.KeyboardButton(name) for name in ['Спросить Ежи', 'Спросить Петруччо']])
	msg = bot.send_message(m.chat.id, 'Кому вопрос?', reply_markup=keyboard)
	bot.register_next_step_handler(msg, name)

def eji_answ(m):
	if m.text == 'Спросить Петруччо':
		keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard1.add(*[types.KeyboardButton(answer1) for answer1 in ['Спросить Ежи']])
		sent = bot.send_message(m.chat.id, 'Петруччо слушает', reply_markup=keyboard1)
		bot.register_next_step_handler(sent, petrucho_answ)
	elif ("?" in m.text)==True:
		message1 = random.choice(eji)
		sent = bot.send_message(m.chat.id, message1)
		bot.register_next_step_handler(sent, eji_answ)
	else:
		sent = bot.send_message(m.chat.id, "Кажется, это не вопрос... Попробуйте с \"?\"")
		bot.register_next_step_handler(sent, eji_answ)

def petrucho_answ(m):
	if m.text == 'Спросить Ежи':
		keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard1.add(*[types.KeyboardButton(answer1) for answer1 in ['Спросить Петруччо']])
		sent = bot.send_message(m.chat.id, 'Ежи слушает', reply_markup=keyboard1)
		bot.register_next_step_handler(sent, eji_answ)
	elif ("?" in m.text)==True:
		message2 = random.choice(petrucho)
		sent = bot.send_message(m.chat.id, message2)
		bot.register_next_step_handler(sent, petrucho_answ)
	else:
		sent = bot.send_message(m.chat.id, "Кажется, это не вопрос... Попробуйте с \"?\"")
		bot.register_next_step_handler(sent, petrucho_answ)

def name(m):

	if m.text == 'Спросить Ежи':
		keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard1.add(*[types.KeyboardButton(answer1) for answer1 in ['Спросить Петруччо']])
		sent = bot.send_message(m.chat.id, 'Ежи слушает', reply_markup=keyboard1)
		bot.register_next_step_handler(sent, eji_answ)

	elif m.text == 'Спросить Петруччо':
		keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard1.add(*[types.KeyboardButton(answer1) for answer1 in ['Спросить Ежи']])
		sent = bot.send_message(m.chat.id, 'Петруччо слушает', reply_markup=keyboard1)
		bot.register_next_step_handler(sent, petrucho_answ)
	else:
		sent = bot.send_message(m.chat.id, "Кого спрашиваете?")
		bot.register_next_step_handler(sent, name)

bot.polling()