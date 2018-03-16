from urllib import request
from bs4 import BeautifulSoup
import csv


class Craw(object):

    def __init__(self, page):
        print('hello')
        print("当前需要爬取的总页面为%d，正在爬取中..."%page)

    def url_manager(self):
        root_url = 'http://python.jobbole.com/category/basic/page/'
        i = 1
        url_list = []
        while i <= int(page):
            self.url = root_url + str(i)
            url_list.append(self.url)
            i = int(i) + 1
            #print(self.url)
        return url_list

    def spider(self, list_url):
        for url in list_url:
            try:
                # 请求
                request1 = request.Request(url)
                # 响应
                response = request.urlopen(request1)
                # 获取内容
                cont = response.read().decode("utf-8")
                # 获取标题
                soup = BeautifulSoup(cont, 'html.parser')
                s1 = soup.find_all('a', {'class': 'archive-title'})
                result_title = [a['title'] for a in s1]
                result_url = [a['href'] for a in s1]
                # 获取内容简介
                s2 = soup.find_all("span", {'class': "excerpt"})
                result_summary = [span.get_text() for span in s2]
                # 输出
                result_set = map(list, zip(result_title, result_summary, result_url))
                csvFile = open('output.csv', 'a')
                writer = csv.writer(csvFile)
                for data in result_set:
                    writer.writerow(data)
                csvFile.close()
                print("Sucessful...")
            except:
                print("error")


if __name__ == "__main__":
    page = int(input('请输入想要爬取网页的总页面数：'))
    craw = Craw(page)
    list_url = craw.url_manager()
    craw.spider(list_url)
