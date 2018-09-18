# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:51:30 2018

@author: Anton
"""

import requests

def awesome_function():
    print('Do some heavy calculations')
    return 42

def download_text_from_web():
    r = requests.get('https://docs.python.org/3/library/unittest.mock.html')    
    print('Pretend we download something')
    return r.text

def countWords(text):
    return len(text)

def do_text_analysis():
    text = download_text_from_web()
    word_count = countWords(text)
    return word_count