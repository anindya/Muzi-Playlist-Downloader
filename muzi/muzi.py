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

    def login(self):

        session = r.Session()
        session.get(self.home_url)

        data = j.jsontree()
        data.username = self.username
        data.password = self.password
        data.persistent = "on"

        data = json.dumps(data)

        hero = session.post(self.login_url, data=data)
        self.hero = hero

        return hero

    def logout(self):

        data = j.jsontree()
        data.redirect = self.home_url
        data = json.dumps(data)

        self.hero.get(logout_url, data=data)
