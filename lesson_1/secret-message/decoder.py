#!/bin/env python

import os

OUTPUT_DIR = "output"
IMAGES_DIR = "alphabet"
IMAGES_PATH = os.path.join(os.getcwd(), IMAGES_DIR)
MESSAGE_OUTPUT = os.path.join(os.getcwd(), OUTPUT_DIR)


def decode():
	file_list = os.listdir(MESSAGE_OUTPUT)
	saved_path = os.getcwd()
	os.chdir(MESSAGE_OUTPUT)
	for name in file_list:
		os.rename(name, name.translate(None, "0123456789"))
	os.chdir(saved_path)



if __name__ == "__main__":
    decode()