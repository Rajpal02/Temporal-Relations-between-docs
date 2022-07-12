from os import listdir
from os import getcwd
from textwrap import indent
from bs4 import BeautifulSoup
import json
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def parse_files(path):
    files = listdir(path)
    
    parse = {}

    for file in files:
        if file.split('.')[-1] != 'json':
            print("Parsing file: " + file)
            with open(path + '/' + file, 'r') as f:
                soup = BeautifulSoup(f.read(), 'lxml')
                
            news_category = "".join(file.split('.')[:-1])
            news = extract_tags(soup, news_category)
            
            parse[news_category] = news
            
            json_file = path + '/' + news_category + '.json'
            
            with open(json_file, 'w+') as of:
                json.dump(news, of)
            print("Parsed " + news_category + " to: " + json_file)
    
    return parse

# def parse(file):
#     with open(file, 'r') as f:
#         soup = BeautifulSoup(f.read(), 'lxml')
        
#     file_name = "".join(file.split('.')[:-1])
#     news = extract_tags(soup, file_name)
    
#     json_file_name = path+'/'+file

    

def extract_tags(soup, file_name):
    data = []
    counter = 0
    for doc in soup.find_all('doc'):
        current = {}
        current['id'] = f"{file_name}-{counter}"
        current['meta'] = {}
        current['meta']['filename'] = doc['filename']
        current['meta']['id'] = doc['id']
        current['meta']['url'] = doc['url']
        current['text'] = []
        
        p_tags = doc.find_all('p')
        for p in p_tags:
            # current['text'].append(p.text.strip())
            current['text'] += tokenizer.tokenize(p.text.strip())
        
        data.append(current)
        counter += 1
    
    return data

#print(getcwd())
#parse_files('Group-7-Project/Project Code/data')