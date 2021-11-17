#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 00:13:27 2021

@author: nairuhi
"""


def findWords(words):
    first_row = "qwertyuiop"
    second_row = "asdfghjkl"
    third_row = "zxcvbnm"
    
    first_letters = set(first_row)
    second_letters = set(second_row)
    third_letters = set(third_row)
    
    result = []
    
    for word in words:
        word_letters = set(word.lower())
        if word_letters.difference(first_letters) == set():
            result.append(word)
        elif word_letters.difference(second_letters) == set():
            result.append(word)
        elif word_letters.difference(third_letters) == set():
            result.append(word)
        else:
            pass
            
    return result



words = ["Hello","Alaska","Dad","Peace"]
print(findWords(words))

words = ["omk"]
print(findWords(words))

words = ["adsdf","sfd"]
print(findWords(words))


