#!/bin/python3
import wikipedia
from bs4 import BeautifulSoup
import sys
def wiki(arg):
    try:
        wikipad = wikipedia.summary(arg)
        soup = BeautifulSoup(wikipad, 'html5lib')
        print(soup.get_text())
    except Exception as e :
        print(e)
wiki(sys.argv[1])


