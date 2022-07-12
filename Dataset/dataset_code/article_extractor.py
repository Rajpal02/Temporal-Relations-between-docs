'''
Author: Guowen Liu
Date: 2022-03-25 18:17:57
LastEditors: Guowen Liu
LastEditTime: 2022-03-28 17:27:26
'''
from newspaper import Article
import requests
from lxml import  etree
import time
import pandas as pd
import csv
'''
Author: Guowen Liu
description: Return url of root directory
param {int} number
param {string} origin_url
return {list} root_url
Date: 2022-03-25 18:22:38
'''
def get_url_list(number,origin_url):
    root_url = []
    for i in range(1,number):
        root_url.append(origin_url+ str(i))
    return root_url


'''
Author: Guowen Liu
description: Get the url of sub article based on the root url
param {list} root_url
param {string} header
param {string} rules
return {list} article_url_list
Date: 2022-03-25 18:32:02
'''
def get_article_url(root_url,header,rules):
    article_url_list = []
    
    for url in root_url:
        resqonse=requests.get(url,headers = header)
        page_text=resqonse.text
        tree=etree.HTML(page_text)
        res = tree.xpath(rules)
        time.sleep(1)
        for suburl in res:
            article_url_list.append(suburl)
    return article_url_list

def save_csv(file_name,content,type):
    dict = {type:content}
    df = pd.DataFrame(dict)
    df.to_csv(file_name)
    return 


def weather_dataset_collections():
    rules = '//div[@class="teaser"]//figure/a/@href'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',}
    root_list = get_url_list(100,"https://www.dublinlive.ie/all-about/weather?pageNumber=")
    article_list = get_article_url(root_list,header,rules)
    save_csv("article_list.csv",article_list,'url')
    return



def create_csv(path):
    csv_head = ["category","title","authors","date","description","content"]

    return

def write_csv(path,data_row):
    with open(path,'a+')as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)
    return


def data_processes(datafile):
    final_dataset  = "Weather.csv"
    data = pd.read_csv(final_dataset)
    print(data)
    
    article_title = []
    article_authors = []
    article_date = []
    article_description = []
    article_content = []
    #csv_head = ['category','title','authors','date','description','content']
    article_category = []

    for index,row in data.iterrows():
        url = row['url']
        try:
            article = Article(url)
            article.download()
            article.parse()
           
        except IOError:
            print(str(row['id'])+" : failed  url: "+url)
            dict = {'category':article_category,'title':article_title,'authors':article_authors,'date':article_date,'description':article_description,'content':article_content}
            df = pd.DataFrame(dict)
            df.to_csv(final_dataset)
            return 
        else:
            article_title.append(article.title)
            article_authors.append(article.authors)
            article_date.append(article.publish_date)
            article_description.append(article.meta_description)
            article_content.append(article.text)
            article_category.append('WEATHER')
            print(str(row['id'])+" : Success  title: "+article.title)
    dict = {'category':article_category,'title':article_title,'authors':article_authors,'date':article_date,'description':article_description,'content':article_content}
    df = pd.DataFrame(dict)
    df.to_csv(final_dataset)
    return

if __name__ =="__main__":
    #weather_dataset_collections()
    data_processes("article_list.csv")