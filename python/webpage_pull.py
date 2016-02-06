# import libraries
import urllib2
import re
from bs4 import BeautifulSoup as BSHTML
from textblob import TextBlob
from HTMLParser import HTMLParser
import sys

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
req = urllib2.Request(sys.argv[1])
response = urllib2.urlopen(req)
the_page = response.read()

# get headers from page and perfrom sentiment analysis on them
# parse page
BS = BSHTML(the_page)
i = 0
polarity_sum = 0
subjectivity_sum = 0
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
    
    # calculate sentiment
    if len(string.split()) > 0:
        string = string.encode('ascii','ignore')
        blob = TextBlob(string)
        polarity_sum += blob.sentiment.polarity
        subjectivity_sum += blob.sentiment.subjectivity
        i += 1
       

# print sentiment values
print "Polarity:     ", polarity_sum/i
print "Subjectivity: ", subjectivity_sum/i
