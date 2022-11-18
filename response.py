from pprint import pprint
import re
import typing

import requests


HTTP_METHODS: list = [
    'get',
    'post',
    'put',
    'delete',
    'head',
    'options',
]

regex = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE
)


def method_request(url: str) ->dict:
    result = {}
    for method in HTTP_METHODS:
        response = getattr(requests, method)
        try:
            status = response(url).status_code
        except requests.exceptions.ConnectionError:
            return None
        if status != 405:
            result[method] = status
    return result

def url_request(urls: typing.Optional[list]) ->typing.Optional[dict]:
    result = {}
    for url in urls:
        method = method_request(url)
        if method is not None:
            result[url] = method
    return result

def url_verification(url: str) ->bool:
    return re.match(regex, url) is not None

if __name__ == '__main__':
    quantity = 0
    result = []
    while quantity < 1:
        try:
            quantity = int(input('Введите количество ссылок: '))
        except ValueError:
            print('Неверный тип данных')
            continue
        if quantity < 1:
            print('Количество не может быть меньше 1')
    for index in range(quantity):
        url = input('Введите ссылку: ')
        if url in result:
            print('Ссылка уже введена')
            continue
        if url_verification(url) is not True:
            print('Строка не является ссылкой')
            continue
        result.append(url)
    response = url_request(result)
    if not response:
        print('Нет активных ссылок')
    else:
        pprint(response)