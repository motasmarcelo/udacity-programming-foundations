#!/bin/env python

import urllib

PROFANITY_URL = "http://www.wdyl.com/profanity?q=%s"

def read_text():
    quotes = open("./movie_quotes.txt")
    contents = quotes.read()
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    query = PROFANITY_URL % text_to_check
    connection = urllib.urlopen(query)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


if __name__ == "__main__":
    read_text()