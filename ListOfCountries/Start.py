#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pprint import pprint
import xml.etree.ElementTree as ET

# Cловарь содержащий сведения о странах
countries = {
    # 'Cuba': data_about_Cuba,
    'Thailand': {'sea': True,
                 'schengen': False,
                 'average_temperature': 30,
                 'currency_rate': 1.8,
                 'cost_day': 50},
    'Hungary': {'sea': False,
                'schengen': True,
                'average_temperature': 10,
                'currency_rate': 0.3,
                'cost_day': 100},
    'Germany': {'sea': True,
                'schengen': True,
                'average_temperature': 5,
                'currency_rate': 0.3,
                'cost_day': 200},
    'Japan': {'sea': True,
              'schengen': False,
              'average_temperature': 15,
              'currency_rate': 0.61,
              'cost_day': 250
              },
}

# Добавьте в программу ещё 5 стран (любых, по вашему усмотрению, достоверность данных большой роли не играет)
countries["Russia"] = {'sea': True, 'schengen': False, 'average_temperature': -30, 'currency_rate': 1, 'cost_day': 180}
countries["USA"] = {'sea': True, 'schengen': False, 'average_temperature': 20, 'currency_rate': 0.5, 'cost_day': 300}
countries["Poland"] = {'sea': False, 'schengen': True, 'average_temperature': 15, 'currency_rate': 1.4, 'cost_day': 140}
countries["Spain"] = {'sea': True, 'schengen': True, 'average_temperature': 25, 'currency_rate': 2, 'cost_day': 220}
countries["China"] = {'sea': True, 'schengen': False, 'average_temperature': 10, 'currency_rate': 1.1, 'cost_day': 110}

# -------------------------- JSON ---------------------------------------------------
# Сохраним список стран в файл JSON
with open('list_of_countries.json', 'w', encoding="UTF-8") as f:
    json.dump(countries, f)
# Прочитаем список стар из файла в формате JSON
with open('list_of_countries.json', 'r', encoding="UTF-8") as f:
    list_of_countries = json.load(f)
pprint(list_of_countries)  # красиво напечатеам список стран

# -------------------------- XML ----------------------------------------------------
# Создадим XML документ
root = ET.Element('countries')
for country, properties in countries.items():
    country_element = ET.SubElement(root, 'country')
    country_element.text = country
    for property_name, property_value in properties.items():
        c = ET.SubElement(country_element, property_name)
        c.text = str(property_value)
# Сохраним список стран в файл XML
with open('list_of_countries.xml', 'w') as f:
    f.write("<?xml version='1.0'?>\n")  # заголовок
    f.write(str(ET.dump(root)))

#pprint(list_of_countries)  # красиво напечатеам список стран

print("_"*60)

# Пользуясь множествами, найдите список стран, которые: тёплые и есть море или находятся в шенгене,
# и нам хватит денег прожить там месяц.
my_money = 15000  # рублей
count_days = 30  # количество дней проживания

# Выведем все страны и цена проживания в ней за месяц в рублях

# Жаркие страны, температора > 20
warm_countries = set([country for country, properties in countries.items() if properties['average_temperature'] > 20])
# Есть море
sea_countries = set([country for country, properties in countries.items() if properties['sea']])
# Входят в Шенген
shengen_countries = set([country for country, properties in countries.items() if properties['schengen']])
# Страны где хватит денег, чтобы прожить там месяц
lowcost_shengen_countries = set([country for country, properties in countries.items()
                                 if my_money - properties['cost_day']*count_days*properties['currency_rate'] > 0])

# Перечень стран при выполнении всех условий
for country in warm_countries & (sea_countries | shengen_countries) & lowcost_shengen_countries:
    print("Страна: {0}".format(country), "и сколько денег потратим: %.2f" % (countries[country]['cost_day']*count_days*countries[country]['currency_rate']))

# Напишите, список значений какого типа вернёт конструкция: list(countries.items()) где countries - словарь из кода программы.
print(type(list(countries.items())))  # вернет тип list т.е. список, внутри списка элементы типа кортеж