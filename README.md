Muzi-Playlist-Downloader
========================

A downloader for playlists on Muzi(Internal music player at IITR made by SDSLabs)

####How to use?

* Clone the repository 'git clone git@github.com:anindya/Muzi-Playlist-Downloader.git' or 'git clone https://github.com/anindya/Muzi-Playlist-Downloader.git'

* Goto muzi_download_playlist.py

* Login to sdslabs.co.in/muzi

* Open the playlist of songs you want to download

* Press F12 to open developer tools and go to Network

* Find ?id=***** with /muzi/ajax/playlist/ written below it 

* The ***** is your ID. Replace 1971 with this ID

* Now run this python file

* All songs will be downloaded to the directory of python script

####TO-DO

* Add functionality to not download songs already downloaded

* Check for songs that are not downloaded(eg. Call me Maybe)
