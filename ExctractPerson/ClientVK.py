#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urllib
from urllib.parse import urlencode, urlparse
import time
from datetime import datetime
import webbrowser

ID_USER_GARIKHARLAMOV = 80491907
CURRENT_YEAR = datetime.now().year

class UserVK:
    """
    Пользователь в ВК
    """
    def __init__(self, profile):
        self.friends = []
        self.profile = profile

    def __str__(self):
        string_out = self.profile["first_name"] + " " + self.profile["last_name"]
        for friend in self.friends:
            string_out += "\n\t" + friend.profile["first_name"] + " " + friend.profile["last_name"]
        return string_out

    @property
    def my_name(self):
        return self.profile["first_name"] + " " + self.profile["last_name"]


class ClientVK:
    """
    Клиент по работе с ВК через API
    """
    def __init__(self, app_id):
        self.__AUTHORIZE = "https://oauth.vk.com/authorize"
        self.__VERSION = "5.60"
        self.__app_id = app_id
        self.__access_token = None

    def get_access_token(self):
        params = {
            "client_id": self.__app_id,
            "display": "page",
            "response_type": "token",
            "scope": "friends,status",
            "v": self.__VERSION
        }
        token_url = "?".join((self.__AUTHORIZE, urlencode(params)))
        webbrowser.open(token_url)  # запрос у пользователя url с токеном доступа
        print("Скопируйте сюда пожалуйста url открытый из вашего открытого браузера:")
        token_url_response = input(">")
        o = urlparse(token_url_response)
        fragment = dict((i.split("=") for i in o.fragment.split("&")))
        self.__access_token = fragment["access_token"]

    def get_friends(self, id_user, friends, groups_friends):
        params = {
            "access_token": self.__access_token,
            "v": self.__VERSION,
            "user_id": id_user
        }
        id_users = requests.get("https://api.vk.com/method/friends.get", params)  # params
        my_friends = []
        for user_id in id_users.json()["response"]["items"]:
            user = requests.get("https://api.vk.com/method/users.get", {"user_id": user_id})
            my_friends.append(UserVK(user.json()["response"][0]))
            friends.append(user_id)
            # Добавим новоую группу в общий список
            for new_group in self.get_groups(user_id):
                if new_group["id"] not in [group["id"] for group in groups_friends]:  # если такой группы нет в списке
                    groups_friends.append(new_group)
        return my_friends

    def get_followers(self, id_user, followers, groups_followers):
        params = {
            "access_token": self.__access_token,
            "v": self.__VERSION,
            "user_id": id_user
        }
        id_followers = requests.get("https://api.vk.com/method/users.getFollowers", params)
        my_followers = []
        for follower_id in id_followers.json()["response"]["items"]:
            try:
                follower = requests.get("https://api.vk.com/method/users.get", {"user_id": follower_id})
                my_followers.append(UserVK(follower.json()["response"][0]))
                # Добавим новоую группу в общий список
                for new_group in self.get_groups(follower_id):
                    if new_group["id"] not in [group["id"] for group in groups_followers]:  # если такой группы нет в списке
                        groups_followers.append(new_group)
                followers.append(follower_id)
            except Exception as e:
                self.write_to_log("Ошибка! follower_id=" + str(follower_id) + " Текст ошибки: " + str(e))
                time.sleep(1)
        return my_followers

    def get_groups(self, id_user):
        """
        Найдем список групп для данного пользователя
        :param id_user:
        :return:
        """
        params = {
            "access_token": self.__access_token,
            "v": self.__VERSION,
            "user_id": id_user
        }
        try:
            groups = requests.get("https://api.vk.com/method/groups.get", params)
            my_groups = []
            for group_id in groups.json()["response"]["items"]:
                group_info = requests.get("https://api.vk.com/method/groups.getById", {"group_id": group_id})
                group_members = requests.get("https://api.vk.com/method/groups.getMembers", {"group_id": group_id})
                my_groups.append({"title": group_info.json()["response"][0]["name"],
                                  "count": group_members.json()["response"]["count"],
                                  "id": group_id
                                })
            return my_groups
        except Exception as e:
            ClientVK.write_to_log("Ошибка! id_user=" + str(id_user) + " Текст ошибки: " + str(e))
            return []

    def get_members(self, group_id):
        group_members_info = []
        try:
            group_members = requests.get("https://api.vk.com/method/groups.getMembers", {"group_id": group_id})
            for user_id in group_members.json()["response"]["users"]:
                try:
                    user = requests.get("https://api.vk.com/method/users.get", {"user_id": user_id, "fields": "sex, bdate"})
                    uid = user.json()["response"][0]["uid"]
                    age = CURRENT_YEAR - datetime.strptime(user.json()["response"][0]["bdate"], "%d.%m.%Y").year
                    sex = "Ж" if int(user.json()["response"][0]["sex"]) == 1 else "М"
                    group_members_info.append({"uid": uid,
                                               "sex": sex,
                                               "age": age
                                               })
                except Exception as e:
                    ClientVK.write_to_log("Ошибка! user_id=" + str(user_id) + " Текст ошибки: " + str(e))
            return group_members_info
        except Exception as e:
            ClientVK.write_to_log("Ошибка! group_id=" + str(group_id) + " Текст ошибки: " + str(e))

    @staticmethod
    def write_to_log(line):
        """
        Запись ошибки в лог файл
        :param line:
        :return:
        """
        with open("error.log", "a", encoding="UTF-8") as log:
            log.write(line + "\n")
            log.flush()


