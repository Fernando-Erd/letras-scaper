# coding=utf-8

import json
import subprocess
import time
import requests
import sys
import re
from pprint import pprint
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


######## Get Page Link #########
def getLink(title, artist):
	title = re.sub('[\\\\/:*?"#()<>|]', '', title)
	artist = re.sub('[\\\\/:*?#()"<>|]', '', artist)
	cmd = 'node search.js -t  "' + str(title) + '" -a "' + str(artist) + '"'
	print cmd
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	process.wait()
	line = process.stdout.readline()
	return line.rstrip()

######## Get Song Writer #######
def getSongWriter(pageSoup):
	songWriterSoup = pageSoup.find_all("div", {"class": "letra-info_comp"})
	songWriterSoup[0].a.decompose()
	
	songWriter = songWriterSoup[0].text
	songWriter = songWriter.encode('utf-8').replace('Composição:  ', '')
	return songWriter[:-5]

def getGenre(pageSoup):
	genre = pageSoup.find_all("span", {"itemprop": "name"})
	return genre[1].text

############ Main #############
data_name = sys.argv[1]
json_name = data_name + ".json"
data = json.load(open(json_name))
csv_name = sys.argv[1] + ".csv"

for a in data:
	page = ''
	page = getLink(a['title'], a['artist'])
	if page != '':
		pageTree = requests.get(page, headers=headers)
		pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

	try:
		songWriter = getSongWriter(pageSoup)
		musicGenre = getGenre(pageSoup)
	except:
		songWriter = ""
		musicGenre = ""
	

	print "--------------------"
	title = str(a['title']).encode('utf-8')
	artist = str(a['artist']).encode('utf-8')
	songWriter = str(songWriter).encode('utf-8')
	if (len(musicGenre) > 1):
		musicGenre = musicGenre.encode('utf-8')
	else:
		musicGenre = ""

	print "Title: " + title
	print "Artist: " + artist
	print "URL: " + page
	print "Song Writer: " + songWriter
	print "Music Genre: " + musicGenre
	print "\n"

	with open(csv_name, 'a') as arq:
		arq.write(title + ";" + artist  + ";" + page + ";" + songWriter  + ";" + musicGenre)
		arq.write("\n")

	time.sleep(50)
