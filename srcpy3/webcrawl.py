# -*- coding:utf8 -*-
#!/user/bin/env python

import urllib
from http import cookiejar
import json
import random

user_agent = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
cookie = "SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; Hm_lvt_65e796f34b9ee7170192209a91520a9a=1542707356; Hm_lpvt_65e796f34b9ee7170192209a91520a9a=1542707356"
url = 'http://www.bee-ji.com/data/search/json'
image_base_url = "http://image.bee-ji.com/"

cj = cookiejar.CookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

def get_image_url():
    req = urllib.request.Request(url + '?size=5')
    req.add_header('User-Agent', user_agent)
    req.add_header('Cookie', cookie)
    data = opener.open(req).read()
    items = json.loads(data)
    if len(items) == 0:
        return None
    image_item = random.choice(items)
    image_url = image_base_url + str(image_item['id'])
    return image_url

def get_image_url_with_query(content):
    param = {"w": content}
    req = urllib.request.Request(url + '?' + urllib.parse.urlencode(param))
    req.add_header('User-Agent', user_agent)
    req.add_header('Cookie', cookie)
    data = opener.open(req).read()
    items = json.loads(data)
    if len(items) == 0:
        return None
    image_item = random.choice(items)
    image_url = image_base_url + str(image_item['id'])
    return image_url

if __name__ == '__main__':
    print(get_image_url())
    print(get_image_url_with_query("狗"))