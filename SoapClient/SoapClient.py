import osa
import suds


class SoapClient:
    """
    Класс - фасад SOAP клиентов
    """
    def __init__(self):
        # Конвернтор температур
        url_wsdl_osa_temperature = "http://www.webservicex.net/ConvertTemperature.asmx?WSDL"
        self.__client_osa_temperature = osa.client.Client(url_wsdl_osa_temperature)
        # Конвернтор валют
        url_wsdl_osa_currency = "http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL"
        self.__client_osa_currency = osa.client.Client(url_wsdl_osa_currency)
        # Конвертор расстояний
        url_wsdl_osa_distance_convector = "http://www.webservicex.net/length.asmx?WSDL"
        self.__client_osa_distance_convector = osa.client.Client(url_wsdl_osa_distance_convector)

    def convert_temperature(self, temperature, from_unit="degreeFahrenheit", to_unit="degreeCelsius"):
        """
        Конвертация температуры
        :param temperature:
        :param from_unit: единица измерения источника (по-умолчанию Фаренгейт)
        :param to_unit: единица измерения преобразования (по-умолчанию Цельсий)
        :return:
        """
        response = self.__client_osa_temperature.service.ConvertTemp(Temperature=temperature, FromUnit="degreeFahrenheit", ToUnit="degreeCelsius")
        return response

    def convert_currency(self, money, from_unit="USD", to_unit="RUB"):
        """
        Конвертация валют
        :param money:
        :param from_unit: единица измерения источника (по-умолчанию Доллар США)
        :param to_unit: единица измерения преобразования (по-умолчанию Рубль)
        :return:
        """
        # response = self.__client_osa.service.currencies(Temperature=temperature, FromUnit="degreeFahrenheit", ToUnit="degreeCelsius")
        response = self.__client_osa_currency.service.ConvertToNum(amount=money, fromCurrency=from_unit, toCurrency=to_unit, rounding=True)
        return response

    def currencies(self):
        """
        Список кодов валют
        :return:
        """
        return self.__client_osa_currency.service.currencies()

    def convert_distance(self, length_value, from_length_unit="Miles", to_length_unit="Kilometers"):
        """
        Конвертация меры длинны
        :param length_value:
        :param from_length_unit: единица измерения источника (по-умолчанию мили)
        :param to_length_unit: единица измерения преобразования (по-умолчанию километры)
        :return:
        """
        return self.__client_osa_distance_convector.service.ChangeLengthUnit(LengthValue=length_value,
                                                                             fromLengthUnit=from_length_unit,
                                                                             toLengthUnit=to_length_unit)

