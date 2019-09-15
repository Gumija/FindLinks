# xml/html parse python
import sys
import time
from lxml import html

def start():
    print("Starting parsing XML")
    path = '../index.html'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    # text = readFile(path)
    parseReferencesLXML(path)

def readFile(path):
    f = open(path, 'r')
    return f.read()

def parseReferencesLXML(path):
    start = time.time()
    tree = html.parse(path)
    links = [el.attrib['href'] for el in tree.findall('//a')]
    end = time.time()
    duration = end -start
    print("LXML")
    print(f"Duration: {duration}\t Found: {len(links)}")



start()