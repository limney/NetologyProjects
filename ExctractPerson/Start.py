#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from ClientVK import *
import os
import time
import threading

MY_APP_ID = 5786550

def clear():
    """
    Чистит консоль
    :return:
    """
    if os.name in ('nt', 'dos'):
        os.system('cls')
    elif os.name in ('linux', 'osx', 'posix'):
        os.system('clear')
    else:
        print("\n"*120)
    show_head()

head_lines = [
    "-----------------------------------------------------------------------",
    "--- Программа извлечения друзей и подписчиков пользователя в VK.com ---",
    "-----------------------------------------------------------------------"
]


def show_head():
    """
    Заголовок программы
    :return:
    """
    for lile in head_lines:
        print(lile)


if __name__ == "__main__":

    clear()

    # Получаем сведения о пользователе
    user_id = input("Введите id пользоателя в VK.com:\n>")
    head_lines.append("Введите id пользоателя в VK.com:\n>" + str(user_id))

    vk = ClientVK(app_id=MY_APP_ID)
    vk.get_access_token()

    friends = []
    followers = []
    groups_followers_friends = {}

    threads_friends = threading.Thread(target=vk.get_friends, args=(user_id, friends, groups_followers_friends))
    threads_friends.start()

    # Сбор друзей и групп пользователя
    while threads_friends.isAlive():
        clear()
        print("Нашли {0} друзей и {1} групп".format(len(friends), len(groups_followers_friends)))
        print("Поиск ...")
        time.sleep(1)

    head_lines.append("Нашли {0} друзей и {1} групп".format(len(friends), len(groups_followers_friends)))

    threads_followers = threading.Thread(target=vk.get_followers, args=(user_id, followers, groups_followers_friends))
    threads_followers.start()

    # Сбор подписчиков и групп пользователя (ограничение до 100 подписчиков)
    while threads_followers.isAlive():
        clear()
        print("Нашли {0} подписчиков и {1} групп".format(len(followers), len(groups_followers_friends)))
        print("Поиск ...")
        time.sleep(1)

    head_lines.append("Нашли {0} подписчиков и {1} групп".format(len(followers), len(groups_followers_friends)))

    # Сохраним все группы друзей и подписчиков
    with open('groups.json', 'w', encoding="utf-8") as json_file:
        json.dump(groups_followers_friends, json_file, ensure_ascii=False)
    report = "Сохранили список групп в которых состоят подписчики и друзья нашего пользователя в файл groups.json, " \
             "всего записано групп: {0}".format(len(groups_followers_friends))
    print(report)
    head_lines.append(report)

    # Сохраним 100 групп друзей и подписчиков
    groups_followers_sorted = list(reversed(sorted(groups_followers_friends, key=lambda g: g['count'])))  # сортировка по количеству людей в группе
    with open('top100.json', 'w', encoding="utf-8") as json_file:
        json.dump(groups_followers_sorted[:100], json_file, ensure_ascii=False)
    report = "Сохранили список 100 групп в которых состоят подписчики нашего пользователя в файл top100.json"
    print(report)
    head_lines.append(report)

    input("Нажвите любую клавишу, чтобы закрыть программу")

