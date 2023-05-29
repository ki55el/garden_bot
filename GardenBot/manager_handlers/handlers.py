from datetime import datetime as dt

from aiogram import types
import requests

from keyboard.kb import get_keyboard
from manager_handlers import instruction
from manager_handlers.parse import choice_recommend, choice_plant, choice_joke


async def send_welcome(message: types.Message):
    user_full_name = message.from_user.full_name
    text = [
        f'Привет👋, {user_full_name}! Я Сад Бот🌻!',
        '\nСписок моих команд 🧭:',
        ' /plant - случайное растение 🔍 ',
        ' /joke - анекдот 🎭 ',
        ' /advice - полезные советы 📝 ',
        ' /weather - данные о погоде ☁',
        ' /orange - инструкция по выращиванию апельсинового дерева 🍊 ',
        '\nАвтор 👤:',
        ' Студент группы МО-221 Сыздыков Дамир 🥸'
    ]

    await message.reply('\n'.join(text), reply_markup=get_keyboard(
        '/help',
        '/plant',
        '/joke',
        '/advice',
        '/weather',
        '/orange'
        )
    )


async def random_plant(message: types.Message):
    await message.reply('Выбирается случайное растение 🌵')

    text = choice_plant()

    await message.answer(text)


async def joker(message: types.Message):
    text = 'Внимание, анекдот 🍆🍆🍆'

    await message.reply('\n'.join(text))

    await message.answer(choice_joke())


async def recommendation(message: types.Message):
    text = [
        'Полезный совет 📝 ',
        'Возможно будет интересно 👇'
    ]
    recommend = choice_recommend()

    await message.reply('\n'.join(text))

    await message.answer(recommend)


async def weather_data(message: types.Message):
    try:
        param = {
            '0': '',
            'T': '',
            'M': '',
            'lang': 'ru'
        }
        response = requests.get('https://wttr.in/', params=param)

        data = response.text.split('  ')
        weather = [
            data[0],
            data[6],
            data[12]
        ]
        for line in data[12:]:
            if 'м' in line:
                weather.append(line)
        weather = '\n'.join(map(str.strip, weather))
        time = f'🕰 Время: {dt.now().strftime("%H:%M")}\n'

        await message.answer(time+'🌦 '+weather)

    except:
        await message.answer('Ошибка сервера. . .')


async def orange_tree(message: types.Message):
    text = [
        'Выращивание апельсинового дерева 🍊',
        '  Я помогу тебе вырастить апельсиновое дерево🪴',
        'Вот инструкция по выращиванию апельсинового дерева 👇'
    ]
    await message.reply('\n'.join(text))

    for block in instruction.orangetree:
        await message.answer('\n'.join(block))
