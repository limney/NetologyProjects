import requests
from urllib.parse import urlencode, urlparse
import pickle

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

    def get_access_token(self):
        params = {
            "client_id": self.__app_id,
            "display": "page",
            "response_type": "token",
            "scope": "friends,status",
            "v": self.__VERSION
        }
        token_url = "?".join((self.__AUTHORIZE, urlencode(params)))

        # token_url_response = requests.get(token_url)
        #print(token_url)

        token_url_response = "https://oauth.vk.com/blank.html#access_token=be60be246d6aee24a158713a897320d375c449ff3160742eea7de68f14795b641849c0483aa8564791168&expires_in=86400&user_id=83492044"

        o = urlparse(token_url_response)
        fragment = dict((i.split("=") for i in o.fragment.split("&")))
        return fragment["access_token"]

    def get_my_friends(self):
        access_token = self.get_access_token()
        params = {
            "access_token": access_token,
            "v": self.__VERSION
        }
        id_users = requests.get("https://api.vk.com/method/friends.get", params)
        my_friends = []
        for user_id in id_users.json()["response"]["items"]:
            user = requests.get("https://api.vk.com/method/users.get", {"user_id": user_id})
            my_friends.append(UserVK(user.json()["response"][0]))
            # Добавим друзей моего друга
            try:
                my_friend_id_users = requests.get("https://api.vk.com/method/friends.get", {"user_id": user_id})  # друзья друга
                for my_friend_user_id in my_friend_id_users.json()["response"]:
                    my_friend_user_id_user = requests.get("https://api.vk.com/method/users.get", {"user_id": my_friend_user_id})
                    my_friends[-1].friends.append(UserVK(my_friend_user_id_user.json()["response"][0]))
            except:
                # Если по какой-то причине нельзя узнать друзей моего друга то пропускаем
                pass
        return my_friends


if __name__ == "__main__":

    vk = ClientVK(app_id=5786550)
    my_friends = vk.get_my_friends()
    # for my_friend in my_friends:
    #     print(my_friend)

    # Сохраним объект my_friends (JSON сериализация)
    with open('my_friends.pickle', 'wb') as f:
        pickle.dump(my_friends, f)

    # Читаем объект my_friends (JSON сериализация)
    with open('my_friends.pickle', 'rb') as f:
        my_friends_saved = pickle.load(f)

    for my_friend in my_friends_saved:
        print(my_friend)

