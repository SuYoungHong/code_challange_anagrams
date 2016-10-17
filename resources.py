# !/usr/bin/env python

"""
    File name: resources.py
    Author: Su-Young Hong
    Date created: 10/16/2016
    Date last modified: 10/16/2016
    Python Version: 2.7
    Description: resources for use with anagrams.py 
"""

from collections import Counter
import requests
from bs4 import BeautifulSoup
import re


def get_text(url):
	"""
	pull text from wikipedia URL into a text generator object
	:note: url must be valid otherwise function returns False
	:param: url (string) url address of wikipeida page
	:return: text_generator object from BeautifulSoup 
	"""
	resp = requests.get(url)
	soup = BeautifulSoup(resp.content, "html.parser")
	bodycontent = soup.find("body").find(id="content").find(id="bodyContent")
	text_generator = bodycontent.stripped_strings
	return text_generator


def clean_and_tokenize(generators_list):
	"""
	take 1 or more text generator objects, pull text, tokenize into
	words, and create set of all words found in all documents
	:param: generators_list (list), list of all generators created with 
	get_text()
	:return: words_set (set) set of all cleaned and tokenized words from
	docs
	"""
	words_set = set()
	for page in generators_list:
		for text in page:
			cleaned = text.replace("\u2019", "'")
			cleaned = cleaned.replace("\'", "'")
			cleaned = cleaned.lower()
			cleaned = cleaned.split(" ")
			cleaned = map(lambda x: re.sub(r"[^A-Za-z'-]", "", x), cleaned)
			cleaned = map(lambda x: x.strip("-"), cleaned)
			cleaned = map(lambda x: x.strip("'"), cleaned)
			cleaned = map(lambda x: x.strip(" "), cleaned)
			words_set.update(cleaned)
	return words_set


def group_by_size(words_set):
	"""
	take set of words and organize them by word length
	:param: words_set (set), set of words created by clean_and_tokenize()
	:return: words_dict (dict), dictionary of the words organized by length
	in the form {int:[word1, word2, etc.], etc.}
	"""
	words_dict = {}
	for word in words_set:
		try :
			words_dict[len(word)].append(word)
		except KeyError:
			words_dict[len(word)] = [word]
	return words_dict


def check_anagram(word1, word2):
	"""
	checks if 2 words are anagrams, returns True or False
	:param: word1, word2 (strings), the 2 words to check
	:return: True or False
	"""
	if Counter(word1) == Counter(word2):
		return True
	else:
		return False


def check_group(words_list):
	"""
	checks for anagrams in a group of words in a list
	:note: this function is to be used with the list of words with same
	length found in the dictionary produced by group_by_size()
	:param: words_list (list of strings) to check
	:return: anagrams (list of tuples), a list of tuples of all words that
	are anagrams of each others 
	"""
	ready_words = list(words_list)
	anagrams = []
	while ready_words != []:
		word = ready_words.pop()
		group = tuple()
		for i in ready_words:
			if check_anagram(word, i) == True:
				group = group + (i,)
		if len(group) > 0:
			for j in group:
				ready_words.remove(j)
			group = group + (word,)
			anagrams.append(group)
	return anagrams


def all_anagrams(words_dict):
	"""
	executes check_groups() for all of the word lists found in the dictionary
	of organized words produced by group_by_size()
	:param: words_dict (dict), dict of {word size: [list of words],} produced
	by group_by_size()
	:return: anagram_groups (list of tuples), a list of all tuples of words
	that are anagrams for each other 
	"""
	anagram_groups = []
	for i in words_dict:
		anagram_groups = anagram_groups + check_group(words_dict[i])
	return anagram_groups






