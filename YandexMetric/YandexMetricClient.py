from abc import ABCMeta, abstractmethod, abstractproperty
from urllib.parse import urlencode, urlparse, urljoin
import requests



class YandexMetricClient:
    """
    Абстрактный класс клиентя Яндекс метрики (Базовый класс)
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
    """
    Подкласс для работы с API отчётов
    """
    _METRIC_STAT_URL = "https://api-metrika.yandex.ru/stat/v1/"

    def __init__(self, token):
        super(YandexMetricStat, self).__init__(token)

    def get_visits_count(self, counter_id):
        """
        Визиты
        :param counter_id:
        :return:
        """
        url = urljoin(self._METRIC_STAT_URL, 'data')
        headers = self.get_header()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(url, params, headers=headers)
        visits_count = response.json()['data'][0]['metrics'][0]
        return visits_count

    def get_page_views(self, counter_id):
        """
        Просмотры
        :param counter_id:
        :return:
        """
        url = urljoin(self._METRIC_STAT_URL, 'data')
        headers = self.get_header()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:pageviews'
        }
        response = requests.get(url, params, headers=headers)
        visits_count = response.json()['data'][0]['metrics'][0]
        return visits_count

    def get_visitors(self, counter_id):
        """
        Посетители
        :param counter_id:
        :return:
        """
        url = urljoin(self._METRIC_STAT_URL, 'data')
        headers = self.get_header()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users'
        }
        response = requests.get(url, params, headers=headers)
        visits_count = response.json()['data'][0]['metrics'][0]
        return visits_count


class YandexMetricManagement(YandexMetricClient):
    """
    Подкласс для работы с API управления
    """
    _METRIC_MANAGEMENT_URL = "https://api-metrika.yandex.ru/management/v1/"

    def __init__(self, token):
        super(YandexMetricManagement, self).__init__(token)

    def counter_list(self):
        url = urljoin(self._METRIC_MANAGEMENT_URL, 'counters')
        headers = self.get_header()
        response = requests.get(url, headers=headers)
        counter_list = [c['id'] for c in response.json()['counters']]
        return counter_list


if __name__ == "__main__":

    metrika = YandexMetricStat("")
    print(metrika.get_visits_count(41885614))


