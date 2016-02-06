# import libraries
import urllib2
import re
from bs4 import BeautifulSoup as BSHTML
from textblob import TextBlob
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ""
    def handle_endtag(self, tag):
        print ""
    def handle_data(self, data):
        print data

# define a function for converting none strings to empty strings
def xstr(s):
    if s is None:
        return ''
    return str(s)

# read html from website
req = urllib2.Request('http://www.nytimes.com/')
response = urllib2.urlopen(req)
the_page = response.read()

# get headers from page and perfrom sentiment analysis on them
# parse page
BS = BSHTML(the_page)

# search for paragraph
for text in BS.find_all('p'):
    # find the string in the text
    for child in text.descendants:
        string = child

    # process text
    string = string.lower()
    string = string.split()
    string = " ".join(string)
    string = string.strip()
    re.sub('[^a-zA-Z0-9-_*.]', '', string)
    if len(string.split()) > 0:
        print string
    #string22 = xstr(string)
    # remove punctuation
    #re.sub('[^A-Za-z0-9]+', '', string)
    #blob = TextBlob(string)
    #print blob.sentiment
