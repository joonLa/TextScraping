# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:23:22 2016

@author: joonhyun
"""
def import_doc(k):
## k is the region you want to read. k=2 gives Arkhangelskaya region. See List.txt
    """
    First, take the current directory.
    """
    import os
    cd = os.path.dirname(os.path.abspath(__file__))
    """
    Next, create the list of data files. titles is a list(datatype list) for the titles for the documents for each region.
    """
    titles = []
    with open(cd+'/List.txt') as inputfile:
        for line in inputfile:
            titles.append(line.strip().split(','))
    """
    Step 2. Create the directory of file that we wan to read.
    """
    regionfile = cd + '/Data/Foreigner/2017/' + ''.join(titles[k])
    """
    Step 3. Using reading function file_contents to read the file correctly.
    """
    from file_contents import file_contents
    contents = file_contents(regionfile) #Now contents reads files correctly.
    return contents + ''.join(titles[k])

