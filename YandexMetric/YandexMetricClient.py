from abc import ABCMeta, abstractmethod, abstractproperty
from urllib.parse import urlencode, urlparse, urljoin
import requests

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

print('?'.join((authorize_url, urlencode(auth_data))))

counter_id = 41885614

my_token = "AQAAAAACjA_HAAPysuizpgddT0VxmnA4eNZ6tNM"


class YandexMetricClient:
    """
    Абстрактный класс клиентя Яндекс метрики
    """
    __metaclass__ = ABCMeta

    def __init__(self, token):
        self.__token = token

    @property
    def token(self):
        return self.__token

    def get_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # @abstractmethod
    # def move():
    #     """Переместить объект"""
    #
    # @abstractproperty
    # def speed():
    #     """Скорость объекта"""


class YandexMetricStat(YandexMetricClient):
    _METRIC_STAT_URL = "https://api-metrika.yandex.ru/stat/v1/"
    _METRIC_MANAGMENT_URL = "https://api-metrika.yandex.ru/managment/v1/"

    def __init__(self, token):
        super(YandexMetricStat, self).__init__(token)

    def counter_list(self):
        url = urljoin(self._METRIC_MANAGMENT_URL, 'counter')
        headers = self.get_header()
        response = requests.get(url, headers=headers)
        counter_list = [c['id'] for c in response.json()['counters']]
        return counter_list

    def get_visits_count(self, counter_id):
        url = urljoin(self._METRIC_MANAGMENT_URL, 'data')
        headers = self.get_header()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(url, params, headers=headers)
        visits_count = response.json()['data'][0]['metrics'][0]
        return visits_count

if __name__ == "__main__":
    metrika = YandexMetricStat(my_token)
    print(metrika.get_visits_count(41885614))
