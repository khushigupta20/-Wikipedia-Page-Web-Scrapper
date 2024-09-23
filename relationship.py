import spacy
import requests
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

url = "https://en.wikipedia.org/wiki/Goddeti_Madhavi"
headers = { 
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    'Accept-Encoding': 'utf-8' 
} 

nlp=spacy.load("en_core_web_sm")

r = requests.get(url=url , headers=headers) 
soup = BeautifulSoup(r.content, 'html5lib')

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(soup_object):
    texts = soup_object.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html=soup.select('div#mw-content-text')
text = text_from_html(html[0])
doc=nlp(text)
for sent in doc.sents:
    print(sent)

#print(doc)