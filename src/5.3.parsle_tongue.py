# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 22:28:57 2025

@author: meron
"""
import re

def read_binary_file_in_chunks(file_path, chunk_size=1024):
    with open(file_path, "rb") as file:
        while chunk := file.read(chunk_size): 
            yield chunk

def extract_hidden_messages(file_path):
    buffer = b""  
    pattern = re.compile(rb"[a-z]{4,}!+")  
    for chunk in read_binary_file_in_chunks(file_path):
        buffer += chunk
        matches = pattern.findall(buffer)  
        for match in matches:
            yield match.decode()  
        buffer = buffer[-10:]  

def parsle_tongue():
    file_path = "resources/logo.jpg"
    for message in extract_hidden_messages(file_path):
        print(message)            