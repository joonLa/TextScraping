# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 14:07:17 2016

@author: joonhyun
reference: http://blog.rolffredheim.com/2013/11/top-seven-tips-for-processing-foreign.html
This function helps us to read the files correctly.
"""
import codecs

def file_contents(file_name):
    with codecs.open(file_name,encoding="windows-1251") as f:  ##The files are encoded in windows-1251.
        try:
            return f.read()
        finally:
            f.close()