# !/usr/bin/env python

"""
    File name: anagrams.py
    Author: Su-Young Hong
    Date created: 10/16/2016
    Date last modified: 10/16/2016
    Python Version: 2.7
    Description: script for checking for anagrams in a 
    Wikipedia page and printing tuples of found anagrams 
    	- execute script via this command: 

    		coolguy$ python anagrams.py url1 url2 etc. 
"""

from resources import *
import sys
import requests


# get list of links to Wikipedia pages 
urls = sys.argv[1:]


# check if links are valid
bad_links = []
for link in urls:
	try:
		req = requests.get(link)
		if req.status_code < 200 and req.status_code > 300:
			bad_links.append(link)
			urls.remove(link)
	except requests.exceptions.MissingSchema:
		bad_links.append(link)
		urls.remove(link)
if bad_links != []:
	print "These links don't seem seem to work:"
	for i in bad_links:
		print '\t' + i


# if there are valid links, give status message
if urls != []:
	print "Checking anagrams for:"
	for i in urls:
		print '\t' + i


# download each link and collect text (via generator) 
all_generators = []
for i in urls:
	page_info = get_text(i)
	all_generators.append(page_info)


# clean and tokenize text from all of the pages
cleaned = clean_and_tokenize(all_generators)


# organize words by length
bigdict = group_by_size(cleaned)


# check for anagrams
anas = all_anagrams(bigdict)


# print all found anagrams via standard output with each group of 
# anagrams being printed per line separated by a space
for i in anas:
	print " ".join(i)


