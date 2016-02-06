# import libraries
import urllib2
import re
from bs4 import BeautifulSoup as BSHTML
from textblob import TextBlob
from HTMLParser import HTMLParser
import sys
import urllib
from cookielib import CookieJar
from textblob.sentiments import NaiveBayesAnalyzer
from pattern.en import sentiment
import cgi
form = cgi.FieldStorage()

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# define a function for converting none strings to empty strings
def xstr(s):
    if s is None:
        return ''
    re.sub('[^a-zA-Z0-9-_*.]', '', s)
    s = s.encode('ascii','ignore')
    return s

# read html from website
req = urllib2.Request(form["url"], headers={'User-Agent' : "Magic Browser"})
response = opener.open(req)
the_page = response.read()

# get headers from page and perfrom sentiment analysis on them
# parse page
BS = BSHTML(the_page)
i = 0
p_sum = 0
n_sum = 0
# search for paragraph
for text in BS.find_all('p'):
    # find the string in the text
    for child in text.descendants:
        string = child.string

    # process text
    string = xstr(string)
    string = string.lower()
    string = string.split()
    string = " ".join(string)
    string = string.strip()
    string = string.encode('ascii','ignore')
    
    # calculate sentiment
    if len(string.split()) > 0:
        blob = sentiment(string, analyzer=NaiveBayesAnalyzer())
        p_sum += blob[0]
        n_sum += blob[1]
        i += 1
       

# print sentiment values
print "Polarity:     ", p_sum/i
print "Subjectivity: ", n_sum/i
