"""
Created on Sat Jan 28 2017
@author: joonhyun
"""
def law_list():
    from import_doc import import_doc
    lenlist = 81 #The number of regions in Russia
    regdoc = []
    for l in range(lenlist):
        regdoc.append(import_doc(l))
    return regdoc
