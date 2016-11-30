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

# -------------------------- JSON (запись) ---------------------------------------------------
# Сохраним список стран в файл JSON
with open('list_of_countries.json', 'w', encoding="UTF-8") as f:
    json.dump(countries, f)
# Прочитаем список стар из файла в формате JSON
with open('list_of_countries.json', 'r', encoding="UTF-8") as f:
    list_of_countries = json.load(f)
#pprint(list_of_countries)  # красиво напечатеам список стран

# -------------------------- XML (запись) ----------------------------------------------------
# Создадим XML документ
root = ET.Element("countries")
for country, properties in countries.items():
    country_element = ET.SubElement(root, "country", attrib={'name': country})
    for propety_name, property_value in properties.items():
        country_sea = ET.SubElement(country_element, propety_name)
        country_sea.text = str(property_value)
tree_countries = ET.ElementTree(root)  # дерево документа
# Запишем список стран в файл XML
tree_countries.write('list_of_countries.xml', encoding="UTF-8", xml_declaration=True)
#print(ET.dump(tree_countries))  # красиво напечатеам список стран


select = int(input("Нажмите - 1 чтобы загрузить списко стран из файла формата Json или 2 - чтобы загрузить из файла формата XML:\n"))

if select == 1:
    countries = {}
    # ---------- JSON (чтение) ---------------------------
    with open('list_of_countries.json') as f:
        countries = json.load(f)
        for country, properties in countries.items():
            countries[country] = properties
        # pprint(countries)
elif select == 2:
    countries = {}
    # ---------- JSON (чтение) ---------------------------
    convertor = {'cost_day': int, 'schengen': bool, 'average_temperature': int, 'sea': bool, 'currency_rate': float}
    tree = ET.parse('list_of_countries.xml')
    root = tree.getroot()
    for country in root.findall("./country"):
        properties = {}
        for property in country:
            properties[property.tag] = convertor[property.tag](property.text)
        countries[country.get('name')] = properties
else:
    print("Вы введи не коректные данные, списки будут использованы из кода программы")

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