#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SoapClient import SoapClient

soap_client = SoapClient()  # SOAP клиент


"""
1) Дано: Семь значений температур по Фаренгейту. Файл temps.txt.
Вопрос: Какая средняя арифм. температура по Цельсию на неделю?
"""

# Чтение данных о температурах на этой недели
week_temperatures = []
with open("temps.txt", "r") as f:
    for line in f.readlines():
        fahrenheit = float(line.split()[0])
        week_temperatures.append(soap_client.convert_temperature(fahrenheit, from_unit="degreeFahrenheit", to_unit="degreeCelsius"))

print("Средняя температура за неделю: {:.2f} градусов цельсия".format(sum(week_temperatures)/len(week_temperatures)))


"""
2) Дано: Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты. Даны цены на билеты в
местных валютах. Файл currencies.txt
(Формат данных в файле: “<откуда куда>: <стоимость билета> <код валюты>”)
Вопрос: Посчитайте сколько вы потратите на путешествие денег в рублях. Точность: без копеек, округлить в большую сторону.
"""
# Чтение данных о поездках
prices = []
with open("currencies.txt", "r") as f:
    for line in f.readlines():
        _, price, cod_currency = line.split()
        prices.append((float(price), cod_currency))

# Расчет сколько потратим денег в рублях на всех поездках
costs = 0
for price, cod_currency in prices:
    costs += soap_client.convert_currency(float(price), from_unit=cod_currency, to_unit="RUB")

print("На все путешествия мы потратим %.2f рублей" % costs)


"""
3) Дано: Длина пути в милях, название пути. Файл travel.txt
(Формат: “<название пути>: <длина в пути> <мера расстояния>”)
      Вопрос: Посчитать суммарное расстояние пути в километрах? Точность: .01 .
"""

# Чтение данных о путях
sum_distances = 0.0
with open("currencies.txt", "r") as f:
    for line in f.readlines():
        _, distance, _ = line.split()
        sum_distances += soap_client.convert_distance(float(distance))

print("Общая длина пути путешествий в километрах: %.2f" % sum_distances)

