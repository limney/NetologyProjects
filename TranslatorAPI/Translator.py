import requests

KEY = 'trnsl.1.1.20161216T160124Z.4a07c4b6a2f01566.ade260e6c684818698899fd08a9c15d72faca843'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class Translator:
    """
    Переводчик текстов через API удаленных сервисов
    """
    def __init__(self, key, url):
        self.__key = key
        self.__url = url
        self.__lang = ("ru", "en")  # направление перевода, первое ОТ (языка оригинала) и второе К (языку результата)

    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, value):
        self.__lang = value[0].lower(), value[1].lower()

    def translate_me(self, my_text):
        """
        YANDEX translation plugin

        docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

        https://translate.yandex.net/api/v1.5/tr.json/translate ?
        key=<API-ключ>
         & text=<переводимый текст>
         & lang=<направление перевода>
         & [format=<формат текста>]
         & [options=<опции перевода>]
         & [callback=<имя callback-функции>]

        :param my_text: <str> text for translation.
        :return: <str> translated text.
        """
        params = {
            "key": self.__key,
            "text": my_text,
            "lang": "-".join(self.lang),
        }
        response = requests.get(self.__url, params=params)
        return response.json()


if __name__ == "__main__":

    translator = Translator(KEY, URL)
    translator.lang = "ru", "fr"

    json = translator.translate_me("Как дела человек?")
    print(' '.join(json["text"]))
