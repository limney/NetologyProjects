#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import urlencode, urlparse, urljoin
from YandexMetricClient import *

"""
Приложение: NetologyProject
ID: 1703177ac368422cbe14d1901a44b1b2
Пароль: 8aa517215ac84f8f9d45c72d7430cdfa
Callback URL: https://oauth.yandex.ru/verification_code
"""
authorize_url = "https://oauth.yandex.ru/authorize"
app_id = "1703177ac368422cbe14d1901a44b1b2"

auth_data = {
    'response_type': 'token',
    'client_id': app_id
}

#print('?'.join((authorize_url, urlencode(auth_data)))) для извлечение запроса, чтобы получить токен

counter_id = 41885614  # id моего счетчика
my_token = "AQAAAAACjA_HAAPysuizpgddT0VxmnA4eNZ6tNM"

# Адрес моего сайта с счетчиком Яндекс Метрика: https://perfectstepcoder.github.io/
url_my_site = "https://perfectstepcoder.github.io/"

metrika_stat = YandexMetricStat(my_token)
print("Адрес моего сайта: {0}\nКод счетчика: {1}\nКоличетсво:\n\t- поситителей: {2}\n\t- просмотров: {3}\n\t- визитов: {4}".format(
    url_my_site,
    counter_id,
    metrika_stat.get_visitors(counter_id),
    metrika_stat.get_page_views(counter_id),
    metrika_stat.get_visits_count(counter_id)
))

metrika_mng = YandexMetricManagement(my_token)

print("Доступные счетчики: ", metrika_mng.counter_list())
