 #!/usr/bin/env python3
# -*- coding: utf-8 -*-


#uses GoogleScraper package for python3

from GoogleScraper import scrape_with_config, GoogleSearchError
import os,sys
import subprocess
import glob
from os import path


keywords = [
    'Search query goes here'  #input your google search query here ' '
]

# See in the config.cfg file for possible values
config = {
    'use_own_ip': True,
    'keywords': keywords,
    'search_engines': ['google'],   #add other search engines if you need
    'num_pages_for_keyword': 50,
    'scrape_method': 'selenium',
    'sel_browser': 'chrome',
}

try:
	search = scrape_with_config(config)
except GoogleSearchError as e:
	print(e)

f = open('searchresultlinks.txt','w')    #indicate name of output file with google search links
sys.stdout = f
path= '/home/Desktop'

for serp in search.serps:
	#print(serp)

	for link in serp.links:
		#print(link)
		print (link, f)  # or f.write('...\n')  print each link to the file
f.close()
