from lxml import etree
import requests


def get_data(url,headers):
    # 第一个坑：注释信息
    return requests.get(url=url,headers=headers).text.replace("<!--","").replace("-->","")

def paser_page(result):
    paser_page = etree.HTML(result)
    elements = paser_page.xpath('//a[@class="j_th_tit "]')
    for ele in elements:
        print(ele.xpath("./text()"))
    next_page = paser_page.xpath('//a[contains(text(),"下一页")]/@href')
    return next_page

def run():
    url = "https://tieba.baidu.com/f?kw=刺激id&ie=utf-8&pn=0"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    while True:
        result = get_data(url=url, headers=headers)
        try:
            next_page = paser_page(result)[0]
        except:
            break
        else:
            url = "https:" + next_page

if __name__ == '__main__':
    run()
