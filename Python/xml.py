# xml/html parse python
import sys
import time
from lxml import html
from selectolax.parser import HTMLParser

def start():
    path = 'index.html'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    text = readFile(path)
    parseReferencesLXML(text)
    parseReferencesSelectolax(text)

def readFile(path):
    f = open(path, 'r', encoding="latin-1")
    return f.read()

def parseReferencesLXML(text):
    start = time.time()
    tree = html.fromstring(text)
    links = [el.attrib['href'] for el in tree.findall('.//a')]
    end = time.time()
    duration = end -start
    print(f"Python LXML\t\t\t\tDuration: {duration:.9f}\t Found: {len(links)}")

def parseReferencesSelectolax(text):
    start = time.time()    
    html_parser = HTMLParser(text)
    links = [tag.attrs['href'] for tag in html_parser.tags('a') if 'href' in tag.attrs]
    end = time.time()
    duration = end - start
    print(f"Python Selectolax\t\t\tDuration: {duration:.9f}\t Found: {len(links)}")

start()