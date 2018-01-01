import requests
import builtwith
import random
def get_agent():
    UA_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
        "'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; U; IntelMac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"]
    return random.choice(UA_list)
cookie3='ll="108296"; bid=imGZGDnver8; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1513880481%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPD8sEabTyr6QuW1rsUJlJFfNMziKL08PEl071Kifz_CpkT2pOsDUvky1RycrtmtBo-cwI25KgSr32A8c4F-HJa%26wd%3D%26eqid%3Dc1417e0600005bfb000000045a3bfb9d%22%5D; _pk_id.100001.8cb4=1eb11aa368062b28.1513529859.6.1513880507.1513868740.; __utma=30149280.540834791.1513529863.1513880481.1514114570.14; __utmz=30149280.1514114570.14.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _vwo_uuid_v2=FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13; __utmv=30149280.14651; ct=y; dbcl2="146925119:8UFklI1xE30"; ck=MkYc; ue="877646746@qq.com"'
cookie2=  'ck=midm; __utmc=30149280; bid=4MkCJCpc990;'
' __utma=30149280.714093067.1510577422.1512480946.1512561835.4;'
' __utmz=30149280.1510577422.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; '
'll=108296; ps=y; dbcl2=170663415:1SxzYXxCPoE; __utmb=30149280.0.10.1512561835; '
'push_noty_num=0; push_doumail_num=0; __utmc=223695111;'
' _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1512561809%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D;'
' _pk_id.100001.4cf6=f414e971fcd4f788.1511518102.3.1512561978.1512480916.;'
' _pk_ses.100001.4cf6=*;'
' __utma=223695111.1064880032.1511518153.1512480946.1512561835.3;'
' __utmz=223695111.1511518153.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/;'
' __yadk_uid=sC5FTKHfpeiLyKd7wwi41h2JVxoLBNaF; __utmb=223695111.4.10.1512561835; __utmt=1'
cookies=[               'bid=hZdgjLJMNv4; _vwo_uuid_v2=AD40AA237919D79C67460DEFD37AFAA4|65f61f85190c51b2cfa95d3910cc2914; gr_user_id=2d7956ee-7cd2-4fad-8a7d-d0b2265ceeba; ll="118316"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1489750475%2C%22https%3A%2F%2Fwww.google.com.hk%2F%22%5D; ap=1; _pk_id.100001.4cf6=270eb4959a2a2414.1489750475.1.1489750559.1489750475.; _pk_ses.100001.4cf6=*; __utma=30149280.1851478845.1488968861.1489658025.1489750475.5; __utmb=30149280.0.10.1489750475; __utmc=30149280; __utmz=30149280.1489750475.5.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.721177542.1489750475.1489750475.1489750475.1; __utmb=223695111.0.10.1489750475; __utmc=223695111; __utmz=223695111.1489750475.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
                        'bid=PHjUxRzrHNk; _vwo_uuid_v2=56A954C0557184C73BBB3DF5C8D30C1D|409597a19056d473ebee60708893e9b8; ll="118221"; ps=y; ue="877646746@qq.com"; dbcl2="146925119:/crpdV7NiKQ"; ck=vkO3; ap=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1465624694%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DjUjRq0ldEsr3DVgcsr-2j6hhjW72VMHrsETjWL2QAee%26wd%3D%26eqid%3Dc07ebf420008142f00000003575b7a83%22%5D; __utmt=1; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=cbb9346c7bb2e22f.1465354092.4.1465624911.1465613335.; _pk_ses.100001.8cb4=*; __utma=30149280.2019919087.1465354115.1465612975.1465624696.4; __utmb=30149280.4.10.1465624696; __utmc=30149280; __utmz=30149280.1465612975.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.14692',
                        'bid=I0klBiKF3nQ; ll="118277"; gr_user_id=ffdf2f63-ec37-49b5-99e8-0e0d28741172; ap=1; _vwo_uuid_v2=8C5B24903B1D1D3886FE478B91C5DE97|7eac18658e7fecbbf3798b88cfcf6113; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1498305874%2C%22https%3A%2F%2Fbook.douban.com%2Ftag%2F%25E9%259A%258F%25E7%25AC%2594%3Fstart%3D20%26type%3DT%22%5D; _pk_id.100001.4cf6=4e61f4192b9486a8.1485672092.5.1498306809.1498235389.; _pk_ses.100001.4cf6=*',
         'll="118190"; bid=c3kC6ui9q28; _pk_id.100001.8cb4=4c5ed6a80ede35ed.1471684466.1.1471684546.1471684466.; _pk_ses.100001.8cb4=*; __utma=30149280.794301906.1471684473.1471684473.1471684473.1; __utmb=30149280.2.9.1471684473; __utmc=30149280; __utmz=30149280.1471684473.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; dbcl2="140658732:f1Vx65Uloqc"; ck=FGYf; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=0B4AF16F37C54670B861F7D7A7C5B679|5b7205084917bf0bf6bd9380a8224a9d',
                        'bid=a3MhK2YEpZw; ll="108296"; ps=y; ue="t.t.panda@hotmail.com"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1482650884%2C%22https%3A%2F%2Fwww.so.com%2Fs%3Fie%3Dutf-8%26shb%3D1%26src%3Dhome_so.com%26q%3Dpython%2B%25E8%25B1%2586%25E7%2593%25A3%25E6%25BA%2590%22%5D; _gat_UA-7019765-1=1; ap=1; __utmt=1; _ga=GA1.2.1329310863.1477654711; dbcl2="2625855:/V89oXS4WD4"; ck=EePo; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=40c3cee75022c8e1.1477654710.8.1482652441.1482639716.; _pk_ses.100001.8cb4=*; __utma=30149280.1329310863.1477654711.1482643456.1482650885.10; __utmb=30149280.19.10.1482650885; __utmc=30149280; __utmz=30149280.1482511651.7.6.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/alanzjl/article/details/50681289; __utmv=30149280.262; _vwo_uuid_v2=64E0E442544CB2FE2D322C59F01F1115|026be912d24071903cb0ed891ae9af65',
                        'bid="9buUE0ITek0"; ll="108288"; gr_user_id=e78c9c62-9a8b-40fe-b7a9-e5f5a8d14fa8; _ga=GA1.2.1570242051.1448263963; __utma=30149280.1570242051.1448263963.1462870413.1473487333.103; __utmz=30149280.1473487333.103.93.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=81379588.1438990260.1449738772.1462870413.1473487333.36; __utmz=81379588.1473487333.36.32.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; viewed="1943987_3269798_7906788_20270192_3112503_25879746_26284925_3740086_24669811_1090601"; _vwo_uuid_v2=CA88D0CE107B6F2D4891D9D1374B71A1|2933393f3143ea74829b216fadf9964e; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1478162962%2C%22https%3A%2F%2Fmovie.douban.com%2F%22%5D; _pk_id.100001.3ac3=23920bca8dce88e9.1449738773.63.1478164058.1476192364.',
    'bid=xQ0BMVjSem8; __utma=30149280.835324949.1486297712.1487313940.1487321509.4; __utmz=30149280.1487321509.4.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; ll="118130"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1487321934%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D39_qCZOrp9cDojY4vvLUS5DYN0eU4kifU3CGzStU3V7%26wd%3D%26eqid%3Dc0ddddb90001116a0000000258a69c0f%22%5D; _pk_id.100001.8cb4=ebaf729a854c56d8.1487245175.3.1487321957.1487314158.; _vwo_uuid_v2=1',
         'll="118196"; bid=evZLAlOEOig; __utma=30149280.19825895.1474635803.1484139127.1484160425.56; __utmz=30149280.1483778648.43.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;__utma = 223695111.1921859920.1474635809.1484139127.1484160425.45;__utmz = 223695111.1475944004.8.6.utmcsr = douban.com | utmccn = (referral) | utmcmd = referral| utmcct = /; _pk_ref.100001.4cf6 = %5B%22%22%2C%22%22%2C1484160423%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D;_pk_id.100001.4cf6 = 9c61c443617ff098.1474635810.45.1484160913.1484143311.;_vwo_uuid_v2 = F7FF27DA6C98B9BD15D6F260CC25B989|f1654bdbf661fc84cb743dc31aebfd6e;gr_user_id = 9a6c5ff8-a80a-4b91-a715-75f80c10d044;viewed = "1054685_26697350";dbcl2 = "119273185:REEk8LlBtVY";push_noty_num = 0;push_doumail_num = 0;__utmv = 30149280.11927;ap = 1;ck = puNv;_pk_ses.100001.4cf6 = *;__utmb = 30149280.0.10.1484160425;__utmc = 30149280;__utmb = 223695111.0.10.1484160425;__utmc = 223695111;ct = y',
                        '''
                         ll="108288"; bid=wKX07fA2ZYg; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1510021150%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; 
                         __yadk_uid=PweZIpbaUi0WN3tKwUO5zzbkeJA2utJv; _vwo_uuid_v2=D26FE17D6BEDFEF32CD1557D15909333|4dafd76f183ded26598d57fd840f7de7; 
                         ct=y; _pk_id.100001.4cf6=aaa017f932668599.1510021150.1.1510022335.1510021150.; __utma=30149280.1018690506.1503653394.1509086343.1510021148.9;
                         __utmc=30149280; __utmz=30149280.1510021148.9.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;
                         __utma=223695111.1567841269.1510021150.1510021150.1510021150.1; __utmc=223695111;
                         __utmz=223695111.1510021150.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/
                         ''',

                        ]
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Connection': 'keep-alive',
           'Cookie':  'll="108296"; bid=imGZGDnver7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1513880481%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPD8sEabTyr6QuW1rsUJlJFfNMziKL08PEl071Kifz_CpkT2pOsDUvky1RycrtmtBo-cwI25KgSr32A8c4F-HJa%26wd%3D%26eqid%3Dc1417e0600005bfb000000045a3bfb9d%22%5D; _pk_id.100001.8cb4=1eb11aa368062b28.1513529859.6.1513880507.1513868740.; __utma=30149280.540834791.1513529863.1513880481.1514114570.14; __utmz=30149280.1514114570.14.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _vwo_uuid_v2=FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13; __utmv=30149280.14651; ct=y; ue="664629747@qq.com"; dbcl2="147826859:cI6QqO2YFtE"; ck=LPAb',
           'Host': 'movie.douban.com',
           'Origin': 'https://movie.douban.com',
           'Referer': "https://www.douban.com/people/170279827/",
           'User-Agent': get_agent(),
           'Upgrade-Insecure-Requests': '1',
           'Cache-Control': 'max-age=0'
           }
url='https://movie.douban.com/people/66200606/collect'
r=requests.get(url,headers=headers)
print(r.text)
for  i in r.cookies:
    print (i)



