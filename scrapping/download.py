# -*- coding:utf-8 -*-"""@author:Levy@file:chapter2.py@time:2017/12/151:11"""
import urllib.request
import urllib.error
def download(url, headers, proxy, num_retries, data=None):
    print
    'Downloading:', url
    request = urllib.request.Request(url, data, headers)
    opener = urllib.request.build_opener()
    if proxy:
        proxy_params = {urllib.urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        code = response.code
    except urllib.error.URLError as e:
        print
        'Download error:', e.reason
        html = ''
        if hasattr(e, 'code'):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                # retry 5XX HTTP errors
                return download(url, headers, proxy, num_retries - 1, data)
        else:
            code = None
    return html

print(download("https:\\www.baidu.com",{},{},5))