# regex python
import sys
import time
import re

def start():
    path = 'index.html'
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
    print(f"Python Regex\t\t\t\tDuration: {duration:.9f}\t Found: {len(links)}")



start()