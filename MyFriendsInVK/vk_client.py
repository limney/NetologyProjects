import requests
from urllib.parse import urlencode, urlparse

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

        token = "https://oauth.vk.com/blank.html#access_token=c93dfe19a243b84ead51d261b067b971e3e4fa7f599df7fcc85d62a57f21e1c2a1ffd4c8371d22dece23d&expires_in=86400&user_id=83492044"

        # token_url_response = requests.get(token_url)
        print(token_url)
        o = urlparse(token_url)
        fragment = dict((i.splite("=") for i in o.fragment.splite("&")))
        return fragment["access_token"]


if __name__ == "__main__":

    vk = ClientVK(app_id=5786550)

    print(vk.get_access_token())
