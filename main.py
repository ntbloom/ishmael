# ishmael.py -- Flask web app for parsing Moby Dick book

from flask import Flask, render_template, request, redirect
import requests, codecs 

# connect to the book
book = requests.get('http://www.gutenberg.org/cache/epub/2489/pg2489.txt')
book.raise_for_status()

# loop through and count paragraphs at are longer than a single line
i = 0
bookDict = {} # dictionary for storing entire book
candidates = []
for chunk in book.iter_content(100000):
    text = codecs.decode(chunk, 'unicode_escape') # decode the weirdly coded text chars (\\n, \\r) 
    paragraphs = text.split("\n\r\n") # split on paragraph seperator
    for p in paragraphs:
        bookDict[i+1] = p
        i = i + 1 # increment paragraph counter
        # ignore skipping of paragraphs
        if '\n' in p: # if it's more than a single line, like a chapter heading
            candidates += [i]

a = int(input('#: \n'))
print(bookDict[a])
while a != 0:
    a = int(input('#: \n'))
    print(bookDict[a])
