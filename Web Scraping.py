#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:43:31 2019

@author: sunny
"""


import requests 
from bs4 import BeautifulSoup

base_url = "http://api.genius.com" 
# Authorizing request
headers = {'Authorization': 'Bearer LN_du9SZQY30MnFsuFEk9PZ3LIvuejg3BAb-5gV-Ejcy7WyoGcberBz-p-eUWDWA'} 
search_url = base_url + "/search" 
artist = "Alison Wonderland"  
params = {'q': artist} 

# API call
resp = requests.get(search_url, params=params, headers=headers)
data = resp.json()
data


#parsing through API to get the URL to the lyrics for Church by Alison Wonderland
song_title="Church" 

for song in data['response']['hits']:
    if song['result']['title'] == song_title:
        lyrics_url = song['result']['url']



#Initial steps to printing lyrics with html tags
lyricsresp = requests.get(lyrics_url)
html_str = lyricsresp.text

document = BeautifulSoup(html_str, 'html.parser')

lyrics = document.find('div', attrs={'class':'lyrics'}).p

#removing tags
unecessary_tags = ['br', 'a']
for tag in unecessary_tags: 
    for match in lyrics.find_all(tag):
        match.replaceWithChildren()
    

Church = "".join(lyrics)

file = open('Church.txt', 'w')
file.write(Church)
file.close()

