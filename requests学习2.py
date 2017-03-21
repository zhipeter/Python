from Download import request
from bs4 import BeautifulSoup
import traceback
import re

def getHTML(url):
    try:
        r=request.get(url,3)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList()