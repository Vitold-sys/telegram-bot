import pyowm
import telebot
import time
import datetime
import schedule
import emoji
import random
import requests

from datetime import datetime
from telebot import types

owm = pyowm.OWM('TOKEN', language="ru")
bot = telebot.TeleBot("TOKEN")


#Your user ID: 11111111
#Current chat ID: 22222222
#Current group chatid = -21211111


@bot.message_handler(commands=['start'])

def send_welcome(mes):
    smile = emoji.emojize(":iphone:", use_aliases=True)
    sad = emoji.emojize(":cry:", use_aliases=True)
    bad = emoji.emojize(":man:", use_aliases=True)
    bot.send_message(mes.chat.id, "Привет, босс!!! Напиши мне город" + str(smile))
    

@bot.message_handler(commands=['check'])

def send_welcome(me):
    '''Function print Hello if you are friend'''
    smo = emoji.emojize(":relaxed:", use_aliases=True)
    ver = emoji.emojize(":smiling_imp:", use_aliases=True)
    angry = emoji.emojize(":rage:", use_aliases=True)
    zzz = emoji.emojize(":zzz:", use_aliases=True)
    ver1 = emoji.emojize(":flushed:", use_aliases=True)
    if me.from_user.id == 111111111:
        bot.send_message(me.chat.id, str(zzz) + "Я скучал. Мой босс ты лучший" + str(smo))
    elif me.from_user.id == 22222222:
        bot.send_message(me.chat.id, str(zzz) + "Привет." + str(ver1) + "Зачем это ты сюда зашел?" + str(ver))
    else:
        bot.send_message(me.chat.id,
                         "Запрещено, как как вы не находитесь в списке доверенных лиц."
                         + str(angry))


@bot.message_handler(commands=["weather"])

def city(city):
    '''Function that print Weather'''
    key = types.InlineKeyboardMarkup()
    button_city1 = types.InlineKeyboardButton(text="Минск", callback_data="Minsk")
    button_city2 = types.InlineKeyboardButton(text="Москва", callback_data="Moscow")
    button_city3 = types.InlineKeyboardButton(text="Варшава", callback_data="Warsaw")
    key.add(button_city1,  button_city2,  button_city3)
    bot.send_message(city.chat.id, "Напиши город или выбери город, нажав на кнопку!" + random.choice(smiles),
                     reply_markup=key)


@bot.message_handler(commands=['help'])

def send_welcome(helper):
    '''Function that do nothing'''
    zzz = emoji.emojize(":eyes:", use_aliases=True)
    point = emoji.emojize(":round_pushpin:", use_aliases=True)
    phone = emoji.emojize(":iphone:", use_aliases=True)
    bro = emoji.emojize(":sunglasses:", use_aliases=True)
    bro1 = emoji.emojize(":fist:", use_aliases=True)
    bro2 = emoji.emojize(":hand:", use_aliases=True)
    bot.send_message(helper.chat.id, str(zzz) + "To start conversation use one of the commands:" + "\n" +
                     str(point) + "/start - to cheer with bot" + "\n" +
                     str(point) + "/check - to find out if bot trusts you" + "\n" +
                     str(point) + "/mood -  to find out your mood " + "\n" +
                     str(point) + "/weather - to find out weather in city" + "\n" +
                     str(point) + "/location - to  to find out where you are" + "\n" +
                     str(point) + "/lol - to participate in an interesting game" + "\n" +
                     str(point) + "/video - bot is sending video to you" + "\n" +
                     str(point) + "/memories - bot is sending url video for you" + "\n"
                     "Or you can just write city to get weather in this place" + str(phone) + "\n\n" +
                     "Have a nice day, bro" + str(bro) + str(bro1) + str(bro2))


smiles = ['🤣','😕','😊','😀','😌', '😗', '😋', '😭']


@bot.message_handler(commands=['lol'])

def inline1(lol1):
    '''Function that print Love'''
    key = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text="Я тебя люблю", callback_data="Love")
    but2 = types.InlineKeyboardButton(text="Я тебя не люблю", callback_data="Nolove")
    key.add(but1, but2)
    bot.send_message(lol1.chat.id, "Ты меня любишь??? :-/," + random.choice(smiles), reply_markup=key)


@bot.message_handler(commands=['mood'])

def inline(mood):
    '''Function Output Love and Mood'''
    intro = emoji.emojize(":small_orange_diamond:", use_aliases=True)
    key1 = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(text="Хорошее", callback_data="Top")
    but2 = types.InlineKeyboardButton(text="Нормально", callback_data="Norm")
    but3 = types.InlineKeyboardButton(text="Не очень", callback_data="Sad")
    key1.add(but1, but2, but3)
    bot.send_message(mood.chat.id, str(intro) + "Как ваше настроение сегодня?", reply_markup=key1)


@bot.callback_query_handler(func=lambda c: True)

def inlin1(c):
    '''Function that print Love and Mood'''
    top = emoji.emojize(":relaxed:", use_aliases=True)
    norm = emoji.emojize(":rage:", use_aliases=True)
    sad = emoji.emojize(":tired_face:", use_aliases=True)
    angry = emoji.emojize(":rage:", use_aliases=True)
    zzz = emoji.emojize(":zzz:", use_aliases=True)
    poop = emoji.emojize(":poop:", use_aliases=True)
    tr = emoji.emojize(":bust_in_silhouette:", use_aliases=True)

    minsk = owm.weather_at_place('Minsk, BY')
    w = minsk.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    hum = w.get_humidity()
    wind = w.get_wind()["speed"]

    moscow = owm.weather_at_place("Moscow, RU")
    m = moscow.get_weather()
    temp1 = m.get_temperature('celsius')["temp"]
    hum1 = m.get_humidity()
    wind1 = m.get_wind()["speed"]

    warsawa = owm.weather_at_place('Warsaw, PL')
    wa = warsawa.get_weather()
    temp2 = wa.get_temperature('celsius')["temp"]
    hum2 = wa.get_humidity()
    wind2 = wa.get_wind()["speed"]

    smile = emoji.emojize(":sunglasses:", use_aliases=True)
    tempem = emoji.emojize(":bar_chart:", use_aliases=True)
    humem = emoji.emojize(":droplet:", use_aliases=True)
    windem = emoji.emojize(":dash:", use_aliases=True)
    point = emoji.emojize(":small_red_triangle_down:", use_aliases=True)
    if c.data == "Love":
        bot.send_message(c.message.chat.id, "Я тебя тоже люблю!!! :-)" + random.choice(smiles))
    elif c.data == "Nolove":
        bot.send_message(c.message.chat.id, "Я тебя не люблю!!! :-( " + random.choice(smiles))
    elif c.data == "Top":
        bot.send_message(c.message.chat.id, "Хорошее настроение, залог чудесного времени" + str(top))
    elif c.data == "Norm":
        bot.send_message(c.message.chat.id, "Нормально это и не плохо, и не хорошо" + str(norm) + "\n " +
                         "Ответьте нормально!" + str(angry))
    elif c.data == "Sad":
        bot.send_message(c.message.chat.id, "Держись, это всего лишь один день" + str(sad))
    elif c.data == "Minsk":
        bot.send_message(c.message.chat.id,
                         "В городе: " + "Минск" + ", по крайней мере сейчас, " + w.get_detailed_status() +
                         str(smile) + "\n")
        bot.send_message(c.message.chat.id, str(point) + "Температура в данный момент в районе " + str(temp) +
                         str(tempem) + "\n")
        bot.send_message(c.message.chat.id,  str(point) + "Влажность " + str(hum) + " % " + str(humem) + "\n")
        bot.send_message(c.message.chat.id, str(point) + "Скорость ветра " + str(wind) + " м/с " + str(windem) + "\n")
        bot.send_photo(c.message.chat.id,
                       'https://www.belarus.by/dadvimages/s002312_447577.jpg')
    elif c.data == "Moscow":
        bot.send_message(c.message.chat.id,
                         "В городе: " + "Москва" + ", по крайней мере сейчас, " + m.get_detailed_status() +
                         str(smile) + "\n")
        bot.send_message(c.message.chat.id, str(point) + "Температура в данный момент в районе " + str(temp1) +
                         str(tempem) + "\n")
        bot.send_message(c.message.chat.id, str(point) + "Влажность " + str(hum1) + " % " + str(humem) + "\n")
        bot.send_message(c.message.chat.id, str(point) + "Скорость ветра " + str(wind1) + " м/с " + str(windem) + "\n")
        bot.send_photo(c.message.chat.id,
                       'https://upload.wikimedia.org/wikipedia/commons/a/a2/Moscow-City2015.jpg')
    elif c.data == "Warsaw":
        bot.send_message(c.message.chat.id,
                         "В городе: " + "Варшава" + ", по крайней мере сейчас, " + wa.get_detailed_status() +
                         str(smile) + "\n")
        bot.send_message(c.message.chat.id, str(point) + "Температура в данный момент в районе " + str(temp2) +
                         str(tempem) + "\n")
        bot.send_message(c.message.chat.id, str(point) + "Влажность " + str(hum2) + " % " + str(humem) + "\n")
        bot.send_message(c.message.chat.id, str(point) + "Скорость ветра " + str(wind2) + " м/с " + str(windem) + "\n")
        bot.send_photo(c.message.chat.id,
                       'https://www.droneinwarsaw.com/wp-content/uploads/2018/01/FOTO_0005-1.png')


@bot.message_handler(commands=["location"])

def geo(message):
    intro = emoji.emojize(":small_orange_diamond:", use_aliases=True)
    geo = emoji.emojize(":round_pushpin:", use_aliases=True)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text=str(geo) + "Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, str(intro) + "Привет! Нажми на кнопку и передай мне свое местоположение",
                     reply_markup=keyboard)


@bot.message_handler(content_types=["location"])

def location(message):
    geo = emoji.emojize(":round_pushpin:", use_aliases=True)
    if message.location is not None:
        print(message.location)
        bot.send_message(message.chat.id, str(geo) + "Ты сейчас тут!")


@bot.message_handler(commands=["video"])

def vide(vid):
    '''Function that send you video'''
    now = datetime.now()
    t = now.strftime("%H")
    a = str(12)
    url = 'http://clips.vorwaerts-gmbh.de/VfE_html5.mp4'

    if t < a:
        bot.send_video(vid.chat.id, url)
    else:
        bot.send_video(vid.chat.id, 'http://techslides.com/demos/sample-videos/small.mp4')


@bot.message_handler(commands=["memories"])

def mem(vid):
    '''Function that gives you url'''
    intro = emoji.emojize(":small_orange_diamond:", use_aliases=True)
    now = datetime.now()
    t = now.strftime("%H")
    a = str(12)
    b = str(17)
    c = str(20)
    if t < a:
        bot.send_message(vid.chat.id, str(intro) + "Открой это видео" + "\n" +
                         'url')
    elif a > t < b:
        bot.send_message(vid.chat.id, str(intro) + "Открой это видео" + "\n" +
                         'url')
    elif b > t < c:
        bot.send_message(vid.chat.id, str(intro) + "Открой это видео" + "\n" +
                         'url')
    else:
        bot.send_message(vid.chat.id, str(intro) + "Открой это видео" + "\n" +
                         'url')


@bot.message_handler(content_types=['text'])

def send_echo(message):
    '''Function that get weather for input place'''
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    hum = w.get_humidity()
    wind = w.get_wind()["speed"]
    smile = emoji.emojize(":sunglasses:", use_aliases=True)
    warm = emoji.emojize(":smirk:", use_aliases=True)
    norm = emoji.emojize(":stuck_out_tongue_closed_eyes:", use_aliases=True)
    cold = emoji.emojize(":astonished:", use_aliases=True)
    warm1 = emoji.emojize(":+1:", use_aliases=True)
    norm1 = emoji.emojize(":ok_hand:", use_aliases=True)
    cold1 = emoji.emojize(":-1:", use_aliases=True)
    tempem = emoji.emojize(":bar_chart:", use_aliases=True)
    humem = emoji.emojize(":droplet:", use_aliases=True)
    windem = emoji.emojize(":dash:", use_aliases=True)
    point = emoji.emojize(":small_red_triangle_down:", use_aliases=True)


    answer = "В городе: " + message.text + ", по крайней мере сейчас, " + w.get_detailed_status() + str(smile) + "\n"
    answer += str(point) + "Температура в данный момент в районе " + str(temp) + str(tempem) + "\n\n"
    answer += str(point) + "Влажность " + str(hum) + " % " + str(humem) + "\n"
    answer += str(point) + "Скорость ветра " + str(wind) + " м/с " + str(windem) + "\n"

    if temp < 10:
        answer += str(cold1) + "Очень холодно, нужно одеться потеплее! и это не шутки..." + str(cold)
        bot.send_photo(message.chat.id,
                       'http://nk-tv.com/wp-content/uploads/2014/02/%D0%BC%D0%BE%D1%80%D0%BE%D0%B7.jpg')
    elif temp < 20:
        answer += str(norm1) + "Можно одеть легкую куртку или идти в байке, но на самом деле можно ожидать чего угодно"\
                  + str(norm)
        bot.send_photo(message.chat.id,
                      'https://travelest.ru/images/for_artickles/225NYEsea8.jpg')
    else:
        answer += str(warm1) + "Очень тепло, можно раздеться!!! Точно не заболеешь!" + str(warm)
        bot.send_photo(message.chat.id,
                       'https://www.columbista.com/data/blog/89/middle_kakoe-more-v-gretsii-vybrat-samoe-teploe-samoe-krasivoe-samoe-spokojnoe.jpg')

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, timeout=123)
