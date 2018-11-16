import  requests, re

def readPages(start, end):
    for page in range(start,end+1):
        url = "https://sh.lianjia.com/ershoufang/pg" + str(page) + "/"
        html = requests.get(url)
        # print(html.text)
        items = re.findall('<li class="clear LOGCLICKDATA" >(.*?)</li>',html.text,re.S)
        infos = []
        for item in items:
            info = {}
            link = re.findall('<div class="title"><a class="" href="(.*?)"',item, re.S)[0]
            totalprice = re.findall('<div class="totalPrice"><span>(.*?)</span>',item, re.S)[0]
            unitprice = re.findall('<div class="unitPrice" data-hid="\d+" data-rid="\d+" data-price="\d+"><span>(.*?)</span>',item, re.S)[0]
            info["totalprice"] = totalprice
            info["unitprice"] = unitprice
            info["link"] = link
            infos.append(info)
        print(infos)

if __name__ == "__main__":
    readPages(1,1)