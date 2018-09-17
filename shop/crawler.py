import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','shop.settings')

import django # django 환경 셋팅
django.setup()

import sys
import requests
from bs4 import BeautifulSoup

from django.core.files import File
from shopping.models import Item

def main(query):
    url = 'https://search.shopping.naver.com/search/all.nhn'
    params = {
        'query':query,
    }
    res = requests.get(url,params=params)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')

    items = soup.select('#_search_list > div.search_list.basis > ul > li')
    for item in items:
        name = trim(item.select('a.tit')[0].text)
        price = int(trim(item.select('.price .num')[0].text).replace(',',''))
        img_url = item.select('img[data-original]')[0]['data-original']

        res = requests.get(img_url,stream=True)
        img_name = os.path.basename(img_url.split('?',1)[0])

        item = Item(name=name,amount=price,is_public=True)
        item.photo.save(img_name,File(res.raw))
        item.save()

def trim(s):
    return ' '.join(s.split())

if __name__ == '__main__':
    try:
        query = sys.argv[1]
        main(query)
    except IndexError:
        print("오류!")


