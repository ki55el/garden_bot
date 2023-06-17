from random import choice, randint

import requests
from bs4 import BeautifulSoup


def choice_recommend():
    response = requests.get('https://iamik.ru/news/tekhnologii/56592/')
    full_data = response.text.split('   ')

    recommendations = 'Советы не найдены'
    for data in full_data:
        if 'Гимадетдинов' in data:
            recommendations = data.replace('\xa0', ' ')
            break

    text = BeautifulSoup(recommendations, 'html.parser').get_text()
    recommendation = text.replace(' \nР. Гимадетдинов', '').split('• ')

    return choice(recommendation)


def choice_plant():
    kinds = [
        ('home', (741, 868)),
        ('lis', (872, 962)),
        ('hvo', (963, 1048)),
        ('trava', (1049, 1065)),
        ('lian', (1069, 1077))
    ]
    description, name = '', ''
    while not description:
        kind, nums = choice(kinds)
        num = randint(*nums)
        response = requests.get(f'https://www.landy-art.ru/helpful_information/catalogue/{kind}.html/nid/{num}')
        if response:
            bs = BeautifulSoup(response.text, 'html.parser')
            name = bs.find('h1', 'title is-nom').text
            description = bs.find('div', 'description').text

    plant = BeautifulSoup(name+description, 'html.parser').get_text()

    return plant


def choice_joke():
    response = requests.get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')

    joke = response.text.split('"')[3]

    return joke
