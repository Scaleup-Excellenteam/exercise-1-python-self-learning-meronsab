# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 02:37:49 2025

@author: meron
"""
def long_cat_is_long(text):
    """
    this func get a text and return a dict of all the words in the text and their len
    """
    text = text.lower()
    cleaned_text = ''.join(char if char.isalpha() or char.isspace() else ' ' for char in text)
    words = cleaned_text.split()
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths
