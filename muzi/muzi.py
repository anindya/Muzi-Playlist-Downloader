import requests as r
import jsontree as j
import json

class Muzi:

    def __init__(self, config):

        self.username = config['username']
        self.password = config['password']
        self.home_url = "https://sdslabs.co.in/home/"
        self.login_url = "https://accounts.sdslabs.co.in/login"
        self.logout_url = "https://accounts.sdslabs.co.in/logout"
        self.playlist_url = "https://muzi.sdslabs.co.in/ajax/user/info.php?userid=me"
        self.check_login = "https://accounts.sdslabs.co.in/info"

    def login(self):

        session = r.Session()
        session.get(self.home_url)

        data = {
        "username": self.username,
        "password": self.password,
        "persistent": "on"
        }

        """
        data = j.jsontree()
        data.username = self.username
        data.password = self.password
        data.persistent = "on"

        data = json.dumps(data)

        print data
        """

        session.post(self.login_url, data=data)
        self.hero = session

        self.check()
        return session

    def check(self):
        q = self.hero.get(self.check_login)
        print q.text

    def logout(self):

        data = j.jsontree()
        data.redirect = self.home_url
        data = json.dumps(data)

        self.hero.get(self.logout_url, data=data)

    def playlist_extractor(self):

        temp_session = self.hero
        temp = temp_session.get(self.playlist_url)
        self.playlist = temp.text

        return self.playlist
