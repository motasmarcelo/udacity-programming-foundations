#!/bin/env python

import os
import shutil
import random




MESSAGE = """Did you like it??
            """

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
    '!': 'macau.jpg',
    '?': 'madagascar.jpg',
    ' ': 'madrid.jpg'
}


def clear_output():
    try:
        shutil.rmtree(OUTPUT_DIR)
    except OSError as err:
        print 40*"=","ERROR",40*"="
        print str(err)
    finally:
        os.mkdir(OUTPUT_DIR)


def make_dictionary():
    pass

def encode_message(message):
    files = []
    message = " ".join(message.upper().split())
    for char in message:
        if char in IMAGES_DICT.keys():
            files.append(IMAGES_DICT[char])
    return files

def new_file_name(filename, number, salt):
    number = int(number)
    salt = int(salt)
    lpad = str(number + salt)
    rpad = str(number) if lpad > salt else ''
    salt = int(random.random()*100)
    filename = filename.split('.')
    new_name = "".join([lpad, filename[0], rpad,'.',filename[1]])
    return new_name



def init(message):
    clear_output()
    message_list = encode_message(message)
    filename_list = IMAGES_DICT.values()
    filename_list.sort()
    if message_list:
        i = 0
        pre_name = ''
        for filename in message_list:
            index = message_list.index(filename)
            salt = int(random.random()*100)
            new_file = new_file_name(pre_name + filename_list[i], index + i, salt)
            shutil.copy(os.path.join(IMAGES_PATH, filename), os.path.join(MESSAGE_OUTPUT, new_file))
            # print "%s - %s - %s" % (IMAGES_DICT.keys()[IMAGES_DICT.values().index(filename)], filename, new_file)
            if i >= len(filename_list) - 1:
                pre_name += "z"
                i = 0
            i += 1





if __name__ == "__main__":
    init(MESSAGE)