from http.cookies import SimpleCookie
import requests
from bs4 import  BeautifulSoup
url='https://movie.douban.com/subject/26935251/collections'
cookie='ll="108296"; bid=imGZGSnfer8; __utma=30149280.540834791.1513529863.1513703501.1513708366.8; __utmz=30149280.1513619745.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513708366%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fredir%3Dhttps%253A%2F%2Fmovie.douban.com%2Fsubject%2F26862829%2Fcollections%22%5D; _pk_id.100001.4cf6=0b84cb941b456850.1513529870.8.1513708694.1513704179.; __utma=223695111.1713362382.1513529870.1513703501.1513708366.8; __utmz=223695111.1513619745.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _vwo_uuid_v2=FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13; __utmv=30149280.14651; dbcl2="146518831:IB3TzikoGJg"; ck=4TIo; __utmc=30149280; __utmc=223695111; ct=y; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1513708366; __utmb=223695111.0.10.1513708366'

headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'Cookie': cookie,
    'Host':'movie.douban.com',
    'Referer':'https://movie.douban.com/subject/26935251/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0',
        }
r=requests.get(url,headers=headers)
print(r.text)

def find_user(cookie):
    n=0

    url = 'https://movie.douban.com/subject/26935251/collections'
    cookie = 'll="108296"; bid=imFZGDnfer8; __utma=30149280.540834791.1513529863.1513703501.1513708366.8; __utmz=30149280.1513619745.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513708366%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fredir%3Dhttps%253A%2F%2Fmovie.douban.com%2Fsubject%2F26862829%2Fcollections%22%5D; _pk_id.100001.4cf6=0b84cb941b456850.1513529870.8.1513708694.1513704179.; __utma=223695111.1713362382.1513529870.1513703501.1513708366.8; __utmz=223695111.1513619745.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _vwo_uuid_v2=FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13; __utmv=30149280.14651; dbcl2="146518831:IB3TzikoGJg"; ck=4TIo; __utmc=30149280; __utmc=223695111; ct=y; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1513708366; __utmb=223695111.0.10.1513708366'

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Connection': 'keep-alive',
               'Cookie': cookie,
               'Host': 'movie.douban.com',
               'Referer': 'https://movie.douban.com/subject/26935251/',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0',
               }
    r = requests.get(url, headers=headers)
    print(r.text)
    for start in range(0,5):
        print (start)
        collection_url=url+'?start={}'.format(20*start)
        print(url)
        html = requests.get(collection_url, headers=headers)
        print(html.text)
        obj_bs = BeautifulSoup(html.text, 'html.parser')
        # 获取带有电影链接的html段
        movie_html = list(obj_bs.findAll("div", {"class": "pl2"}))
        for part in movie_html:
            print(part.a.attrs["href"])
            print(n)
            n=n+1

print(find_user( cookie))



