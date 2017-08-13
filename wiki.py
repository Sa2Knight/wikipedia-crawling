# -*- coding: utf-8 -*-
import sys
import re
import time
import os
import requests
import random
from bs4 import BeautifulSoup

BASEURL = 'https://ja.wikipedia.org'

# 指定したWikipediaページ内のaタグからランダムで一つ戻す
def get_wiki_a_tag(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')
  print(soup.find('h1').text)
  a_tags = filter(
    lambda a: 'href' in a.attrs and
               a.text and
               a.attrs['href'].startswith('/wiki') and
               a.attrs['href'].find('Wikipedia') and
               a.text.find('年') == -1,
    soup.select('.mw-parser-output p a')
  )
  a_tags_list = list(a_tags)
  if not len(a_tags_list):
    print("end")
    sys.exit()
  return random.sample(a_tags_list, 1)[0]

# 開始地点を設定
word  = '阿部寛'
url   = f"{BASEURL}/wiki/{word}"
# ランダムにWikipediaのリンクを飛び続ける
while True:
  a_tag = get_wiki_a_tag(url)
  url  = f"{BASEURL}{a_tag.attrs['href']}"
  time.sleep(1)
