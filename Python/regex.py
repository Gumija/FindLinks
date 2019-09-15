# regex python
import sys
import time
import re

def start():
    print("Starting parsing XML")
    path = '../index.html'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    text = readFile(path)
    parseReferencesRegex(text)

def readFile(path):
    f = open(path, 'r', encoding='latin-1')
    return f.read()

def parseReferencesRegex(text):
    start = time.time()
    links = re.findall('<a.*href="(.*)".*>', text)
    end = time.time()
    duration = end -start
    print("LXML")
    print(f"Duration: {duration}\t Found: {len(links)}")



start()