## Script for Checking Anagrams on Wikipedia Page
Author: Su-Young Hong
Date: 10/16/2016
Email: suyoung.hong@gmail.com

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

**Author's Notes / Improvements**
* This script just checks the body of the Wikipedia page, not the rest. 
* Tokenizing the textstring is pretty imperfect right now, wierd unicode stuff, like "\u03c0", "\u2026", "\u0027" isn't handled in any special way (wait, are they all \uxxxx format???) so I regex out all non-numerics other then "'" and "-". There could be orphaned bits of words that are messing things up. Also, it won't handle stuff like umlauts well because of this, so the more... international a page is, the worse this script will perform. 
* If you have suggestions for improvement or comment on the code, please email me!




