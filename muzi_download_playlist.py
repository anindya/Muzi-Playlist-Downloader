import urllib
import os
import sys
import json
import wget

url = "https://sdslabs.co.in/muzi/ajax/playlist/?id=1971" 
#url = "https://sdslabs.co.in/muzi/ajax/playlist/?id="ID HERE"" 
#Add your ID here. Can be found using following steps
"""
		1. Login to sdslabs.co.in/muzi
		2. Press F12 to open developer tools and go to Network
		3. Find ?id=***** with /muzi/ajax/playlist/ written below it 
		4. The ***** is your ID. Add it to the above ID HERE and uncomment the second url statement
		5. Now run the python file and enjoy music...
"""

page = urllib.urlopen(url)
data = page.read()
i =0 
data_new = data
file_rename = dict()

try:
	i = 1
	while(data_new.index('{"id":')	):
		startIndex = data_new.index('{"id":')
		#print data_new[startIndex:]
		#print data_new[startIndex+7:]
		endIndex = (data_new[startIndex+7:]).index('"')
		#print data_new[endIndex]
		#print endIndex
		song_id = data_new[startIndex+7:startIndex + 7 + endIndex]
		data_new = data_new[startIndex + 8 + endIndex:]
		#print "Song"
		#print song_id
		i += 1
		url_song = "https://sdslabs.co.in/muzi/ajax/track/?id=" + song_id
		song_url_page = urllib.urlopen(url_song)
		data_song_page = song_url_page.read()
		
		startIndex_title = data_song_page.index('title')
		endIndex_title = data_song_page[startIndex_title+1:].index('",')
		title = data_song_page[startIndex_title+8:startIndex_title+1+endIndex_title]
		print "Downloading.. " 
		print title

		startIndex_file = data_song_page.index('file')
		endIndex_file = data_song_page[startIndex_file+1:].index(',')
		file_location = data_song_page[startIndex_file+7:startIndex_file+endIndex_file]
		
		file_location = file_location.replace('\\', "")
		file_location_dictionary = file_location[file_location.index('/')+1:]
		file_type = file_location[-4:]
		file_location = "https://music.sdslabs.co.in/" + file_location
		#print file_location
		
		#print file_type
		file_rename[file_location_dictionary] = title
		wget.download(file_location)
		
		title = title + file_type
		try:
			os.rename(file_location_dictionary, title)
		except:
			print "\nCannot rename " +  title
		#urllib.urlretrieve(file_location, title + ".mp3")
except:
	print "EOF"

#for filename in os.listdir("."):
#	os.rename(filename, file_rename[filename])
