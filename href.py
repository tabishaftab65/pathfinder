#!/usr/bin/python

import urllib2
import re
from bs4 import BeautifulSoup

url = raw_input("Give the url")
quote_page = url+'/'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out all the href tags
href = []
exp = url+r'/*'
#for a in soup.find_all('a', href=True):
for a in soup.find_all('a', {'href': re.compile(exp)}):	
	href.append(a['href'])
	
#print href

import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('index.csv', 'w') as csv_file:
  writer = csv.writer(csv_file)
  for tags in href:
    writer.writerow([tags, datetime.now()])

# soup.find_all('a', {'href': re.compile(r'http://www.bloomberg.com/*')})
