"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem

import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет! Этот бот может подсказать, '
                              'в каком созвездии находится планета. '
                              'Введи команду /planet и название планеты на английском, чтобы проверить')


def get_planet(update, context):
    print(f'Вызван {update.message.text}')
    if update.message.text == '/planet':
        update.message.reply_text('Для расчета созвездия введите команду /planet и название планеты на английском, '
                                  'например, /planet Mars')

    user_command = update.message.text.split()
    user_planet = user_command[1]
    today = datetime.datetime.now().strftime('%Y/%d/%m')

    if user_planet == 'Mercury':
        planet = ephem.Mercury(today)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet} сегодня находится в созвездии {const}')
    elif user_planet == 'Venus':
        planet = ephem.Venus(today)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet} сегодня находится в созвездии {const}')
    elif user_planet == 'Mars':
        planet = ephem.Mars(today)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet} сегодня находится в созвездии {const}')
    elif user_planet == 'Jupiter':
        planet = ephem.Jupiter(today)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet} сегодня находится в созвездии {const}')
    elif user_planet == 'Saturn':
        planet = (ephem.Saturn(today))
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet} сегодня находится в созвездии {const}')
    elif user_planet == 'Uranus':
        planet = ephem.Uranus(today)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet} сегодня находится в созвездии {const}')
    elif user_planet == 'Neptune':
        planet = ephem.Neptune(today)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet} сегодня находится в созвездии {const}')
    elif user_planet == 'Pluto':
        planet = ephem.Pluto(today)
        const = ephem.constellation(planet)
        update.message.reply_text(f'Планета {user_planet} сегодня находится в созвездии {const}')
    else:
        update.message.reply_text(
            'Введите название планеты на английском языке. Подсказка: Меркурий - Mercury, Венера - Venus, '
            'Марс - Mars, Юпитер - Jupiter, Сатурн - Saturn, Уран - Uranus, Нептун - Neptune, Плутон - Pluto')


planets = ['Меркурий', 'Mercury', 'Венера', 'Venus', 'Марс', 'Mars', 'Юпитер', 'Jupiter', 'Сатурн', 'Saturn',
           'Уран', 'Uranus', 'Нептун', 'Neptune', 'Плутон', 'Pluto']


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    if user_text in planets:
        update.message.reply_text(f'Чтобы узнать, в каком созвездии находится планета {user_text}, '
                                  f'добавьте команду /planet перед названием планеты на английском языке')
    else:
        update.message.reply_text(user_text)


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
