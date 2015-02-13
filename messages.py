#!/bin/env python

import os
import shutil
import random

OUTPUT_DIR = "output"

IMAGES_PATH = os.path.join(os.getcwd(),"alphabet")
MESSAGE_OUTPUT = os.path.join(os.getcwd(), OUTPUT_DIR)

IMAGES_DICT = {
    'A': 'athens.jpg', 
    'B': 'austin.jpg', 
    'C': 'bangalore.jpg', 
    'D': 'barcelona.jpg', 
    'E': 'beijing.jpg', 
    'F': 'berkeley.jpg', 
    'G': 'bogota.jpg', 
    'H': 'bristol.jpg', 
    'I': 'bucharest.jpg', 
    'J': 'buenos aires.jpg', 
    'K': 'cairo.jpg', 
    'L': 'chennai.jpg', 
    'M': 'chicago.jpg', 
    'N': 'colombo.jpg',
    'O': 'dallas.jpg', 
    'P': 'delhi.jpg', 
    'Q': 'edinbrugh.jpg', 
    'R': 'gainesville.jpg', 
    'S': 'houston.jpg', 
    'T': 'hyderabad.jpg', 
    'U': 'istanbul.jpg', 
    'V': 'ithaca.jpg', 
    'W': 'jacksonville.jpg', 
    'X': 'karachi.jpg',
    'Y': 'kiev.jpg', 
    'Z': 'london.jpg',
    '.': 'los angeles.jpg',
    ' ': 'madrid.jpg'
}


def clear_output():
    try:
        shutil.rmtree(OUTPUT_DIR)
        os.mkdir(OUTPUT_DIR)
    except OSError:
        pass



def make_dictionary():
    pass

def encode_message(message):
    files = []
    message =  message.upper()
    for char in message:
        if char in IMAGES_DICT.keys():
            files.append(IMAGES_DICT[char])
    return files

def new_file_name(filename, number, salt):
    new_name = 
    return 



def init(message):
    file_list = encode_message(message)
    salt = int(random.random()*100)
    if file_list:
        for file in file_list:
            new_file = new_file_name(file, file_list.index(file))
            shutil.copy(os.path.join(IMAGES_PATH, file), os.path.join(MESSAGE_OUTPUT, new_file)) 


if __name__ == "__main__":
    print encode_message("oi como vai")