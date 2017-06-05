# -*- coding: utf8 -*- 
import telebot
import random
from telebot import types

token = '316066244:AAHx-0Xs_KAotsQa8YSAKftqg7uTk-zdIIs'
bot = telebot.TeleBot(token)

eji = ['Этот вопрос - сложный вопрос, а Ежи и Петруччо они простые.', 'Где здесь право, а где лево?','Надо купить бубен.', 'Две и две трети ноги - это не так уж мало!', 'Надо прибавить четкости.', 'А дальше?', 'можно ли собаку посадить на стул?', 'Ежи - Ежино, а Петруччо - Петруччино.', 'Так держать!', 'Много всего, а класть некуда.', 'тот, кто задумался над этим вопросом, обречен на неудачу.', 'я Ежи, а ты Петруччо', 'собственно, не было выбора', 'одна река течет', 'одному нужна книга, а другому нет.', 'а Ежи не обиделся', 'далеко занесло Петруччо', 'От прибавленного к прибавочной, и прибавленному', 'Это «My Way»!', 'Покоя нет!', 'откуда ты это взял?']

petrucho = ['Есть река, она течет…', 'Сейчас брошу в тебя вилкой!', 'Нет Ежи, нет и Петруччо.', 'Не отвечал за свои поступки, потому что был собак.', 'Принести хурму!', 'Мы все вышли из одного мешка.', 'Дальше: лес, река, поле…', 'раз это так естественно происходит, то значит так оно и должно быть, а собаку тут нечего приплетать...', 'Пусть каждый решает сам. Ежи сам, а Петруччо тоже сам.', 'Слава тебе господи, что это не Билли Джонс!', 'Все вернулось на круги своя.', 'В чем тут закон?', 'Ориентируйся по звездам', 'я Петруччо', 'таков Петруччо', 'остались, фактически, только имена', 'бросить все, пойти в другой лес', 'там надо рыбу резать ножом', 'ну, а дальше уже не интересно', 'Есть жизнь за пределами Ежи и Петруччо.', 'сейчас время разбрасывать…']

@bot.message_handler(commands=['start'])
def start(m):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*[types.KeyboardButton(name) for name in ['Спросить Ежи', 'Спросить Петруччо']])
	msg = bot.send_message(m.chat.id, 'Кому вопрос?',
		reply_markup=keyboard)
	bot.register_next_step_handler(msg, name)

def name(m):
	if m.text == 'Спросить Ежи':
		sent = bot.send_message(m.chat.id, 'Ежи слушает')
		def answer1(message):
			message1 = random.choice(eji)
			bot.send_message(m.chat.id, message1.format(name=message.text))
			bot.register_next_step_handler(sent, answer1)
		bot.register_next_step_handler(sent, answer1)

	elif m.text == 'Спросить Петруччо':
		sent = bot.send_message(m.chat.id, 'Петруччо слушает')
		def answer2(message):
			message2 = random.choice(petrucho)
			bot.send_message(m.chat.id, message2.format(name=message.text))
			bot.register_next_step_handler(sent, answer2)
		bot.register_next_step_handler(sent, answer2)

bot.polling()