import requests

KEY = 'trnsl.1.1.20161216T160124Z.4a07c4b6a2f01566.ade260e6c684818698899fd08a9c15d72faca843'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_me(mytext):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & __lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    params = {
        'key': KEY,
        'text': mytext,
        '__lang': 'en-fr',
    }
    response = requests.get(URL, params=params)
    return response.json()

json = translate_me('How are you?')
print(' '.join(json['text']))


