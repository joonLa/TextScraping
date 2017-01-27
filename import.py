# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:23:22 2016

@author: joonhyun
"""
"""
Step 1. Create the list of data files. titles is a list(datatype list) for
the titles for the documents for each region.
You should adjust your directory before you start.
"""

titles = []
with open('/Users/joonhyunla/Documents/TextScraping/Version0601_2Joon/txtscr/Songha/RL1/RLF/List.txt') as inputfile:
    for line in inputfile:
        titles.append(line.strip().split(','))
        
"""
Step 2. Create the directory of each file.
"""

k=1 ## The region you want to read. k=2 gives Arkhangelskaya region. See List.txt
regionfile = '//Users/joonhyunla/Documents/TextScraping/Version0601_2Joon/txtscr/Songha/RL1/RLF/Data/' + ''.join(titles[k])

#""" These parts are dummy now. I just leave it because they might be useful later.
#Step 3. Read the file.
#"""
#results = []
#with open(regionfile) as inputfile:
#    for line in inputfile:
#        results.append(line.strip().split(','))
"""
Step 3. Using reading function file_contents to read the file correctly.
"""
from file_contents import file_contents
contents = file_contents(regionfile) #Now contents is correctly reading files. Use print contents to check it. type(contents) = unicode. Great!
print(contents)


#"""These parts are dummy now, too. Just leave it for later possible use.
#A failed attempt: This is not scalable.. It took too much time to operate.
#temp = open(regionfile).read() # Even this part is not scalable.
#temp.decode("utf-16")
#"""
