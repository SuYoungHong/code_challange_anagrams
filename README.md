## Script for Checking Anagrams on Wikipedia Page
Author: Su-Young Hong
Date: 10/16/2016

#### Description: 
Python script which checks the content of one or more Wikipedia pages (user supplied) and outputs all anagrams found through standard output. 

Script is written in Python 2.7.10 and requires the following packages: 
* collections
* requests
* bs4 (beautifulsoup 4)
* re
* sys

#### Instructions: 
Run script by running the following command from this directory

	
		python anagrams.py url1 url2 etc
	

where url1, url2, etc are links to Wikipedia pages. User can provide 1 or more links. For example: 


		python anagrams.py https://en.wikipedia.org/wiki/Deadpool https://en.wikipedia.org/wiki/El_Modena_High_School https://en.wikipedia.org/wiki/Colin_Kaepernick

**Note** url should start with "https://" otherwise can't read the content won't run. 

#### Files: 
**resources.py**
* Module which includes various functions for use in the main script (anagrams.py)

**anagrams.py**
* Script which checks for anagrams from Wikipedia page (this is the file you run!!!)

