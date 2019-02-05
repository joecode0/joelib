import pandas as pd
import requests
from bs4 import BeautifulSoup as soup


def get_basic_block(url, blockType, tagType, tag):
    response = requests.get(url, headers={'User-Agent': 'Custom'})
    page = soup(response.content, "html.parser")
    block = page.findAll(str(blockType), {str(tagType): str(tag)})
    return block
