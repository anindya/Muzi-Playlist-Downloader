import requests as r
import jsontree as j
import json
import urllib

class Muzi:

    def __init__(self, config):

        self.username = config['username']
        self.password = config['password']

        self.home_url = "https://sdslabs.co.in/home/"
        self.login_url = "https://accounts.sdslabs.co.in/login"
        self.logout_url = "https://accounts.sdslabs.co.in/logout"
        self.playlist_url = "https://muzi.sdslabs.co.in/ajax/user/info.php?userid=me"
        self.check_login = "https://accounts.sdslabs.co.in/info"
        self.songs_in_playlist_url = "https://muzi.sdslabs.co.in/ajax/playlist/?id=" #Attach id here.
        self.track_url = "https://muzi.sdslabs.co.in/ajax/track/?id=" #Attach song id here
        self.song_url = "https://music.sdslabs.co.in/"

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

        # print self.playlist

        return self.playlist

    def songs_extractor(self, s_id):

        temp_session = self.hero
        id_req = json.loads(self.playlist)['playlists'][int(s_id)]['pid']
        
        temp = temp_session.get(self.songs_in_playlist_url+id_req)

        # print self.songs_in_playlist_url+str(s_id)

        self.songs = json.loads(temp.text)
        song_id = []

        for track in self.songs['tracks']:
            song_id.append(track['id'])

        self.id = song_id

    def song_downloader(self, folder_name):

        temp_session = self.hero

        for song_id in self.id:

            temp = temp_session.get(self.track_url+str(song_id))
            song_url = json.loads(temp.text)['file']

            song_name = song_url.split('/')

            print "Downloading %s" % song_name[len(song_name) - 1]
            urllib.urlretrieve(self.song_url+song_url, folder_name+"/"+song_name[len(song_name) - 1])
