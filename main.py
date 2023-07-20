import telebot
import requests
import base64
import json
from telebot import types
from telebot.types import InputMediaPhoto
import os
from os.path import join, dirname
from dotenv import load_dotenv
def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)
token = get_from_env('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/tip')
    markup.add(back)
    bot.send_message(message.chat.id, 'Send keywords to me, i generate image for you (all languages apply)', reply_markup=markup)
@bot.message_handler(commands=['tip'])
def tip(message):
    bot.send_message(message.chat.id, 'If you wanna tip me - https://www.buymeacoffee.com//wolfhoundt6')

@bot.message_handler()
def generate(message):
    with open("id.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(f"{message.chat.id}")
    with open("request.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(f"{message.text}")
    try:
        url = 'https://bf.dallemini.ai/generate'
        myobj = {'prompt': f'{message.text}'}
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        back = types.KeyboardButton('/tip')
        markup.add(back)
        bot.send_message(message.chat.id, 'Accepted, processing', reply_markup=markup)
        x = requests.post(url, json=myobj)
        json_string = x.content
        imgstring = json.loads(json_string)
        imgdata = base64.b64decode(imgstring['images'][0])
        file = open('1.png', 'wb')
        file.write(imgdata)
        file.close()
        imgdata = base64.b64decode(imgstring['images'][1])
        file = open('2.png', 'wb')
        file.write(imgdata)
        file.close()
        imgdata = base64.b64decode(imgstring['images'][2])
        file = open('3.png', 'wb')
        file.write(imgdata)
        file.close()
        imgdata = base64.b64decode(imgstring['images'][3])
        file = open('4.png', 'wb')
        file.write(imgdata)
        file.close()
        imgdata = base64.b64decode(imgstring['images'][4])
        file = open('5.png', 'wb')
        file.write(imgdata)
        file.close()
        imgdata = base64.b64decode(imgstring['images'][5])
        file = open('6.png', 'wb')
        file.write(imgdata)
        file.close()
        imgdata = base64.b64decode(imgstring['images'][6])
        file = open('7.png', 'wb')
        file.write(imgdata)
        file.close()
        imgdata = base64.b64decode(imgstring['images'][7])
        file = open('8.png', 'wb')
        file.write(imgdata)
        file.close()
        imgdata = base64.b64decode(imgstring['images'][8])
        file = open('9.png', 'wb')
        file.write(imgdata)
        file.close()
        with open('9.png', 'rb') as photo9, open('8.png', 'rb') as photo8, open('7.png', 'rb') as photo7, open('6.png', 'rb') as photo6, open('5.png', 'rb') as photo5, open('4.png', 'rb') as photo4, open('3.png', 'rb') as photo3, open('2.png', 'rb') as photo2, open('1.png', 'rb') as photo1:
            bot.send_media_group(message.chat.id, [InputMediaPhoto(photo9), InputMediaPhoto(photo8), InputMediaPhoto(photo7), InputMediaPhoto(photo6), InputMediaPhoto(photo5), InputMediaPhoto(photo4), InputMediaPhoto(photo3), InputMediaPhoto(photo2), InputMediaPhoto(photo1)])
    except:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        retry = types.KeyboardButton(f'{message.text}')
        markup.add(retry)
        bot.send_message(message.chat.id, 'Request failed, please try again, press button to repeat', reply_markup=markup)
bot.polling(none_stop=True)
