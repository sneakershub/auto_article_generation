# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:05:23 2019

@author: seita
"""
from pathlib import Path
import time
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver


def search_img(name, limit):
    search_img_sn(name, limit)
    search_img_hn(name, limit)
    search_img_b(name, limit)
#    else:
#        
        
if __name__ == "__main__":
   search_img('Air Max 720', 5)

def search_img_b(shoename, searchlimit):
#    Get images from Bing image search
#    c_path = os.getcwd()
#    if os.name == 'NT':
#        driver_path = c_path + '\chromedriver_win\chromedriver.exe'
#    else:
#        driver_path = c_path + '\chromedriver_mac\chromedriver.exe'
#    print(driver_path)
#    driver = webdriver.Chrome(executable_path=driver_path)
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    word = shoename
    url = 'https://www.bing.com/?scope=images&q={}'.format(word)
    # 保存するディレクトリ
    out_path = Path('images')
    out_path.mkdir(exist_ok=True)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    img_tags = soup.find_all('img', attrs={'src': True, 'class': 'mimg'})
    loop = searchlimit*2
    try: 
        for i, img_tag in enumerate(img_tags):
            save_name = '{}_{}.jpg'.format(word, loop)  # 保存するファイル名
            save_path = out_path / save_name  # 保存するパス
        
            img_url = 'https://www.bing.com' + img_tag['src']
            if img_tag['src'].startswith('/th?'):
                save_image(img_url, save_path)
            if img_tag['src'].startswith('data:'):
                inds = img_tag['src'].index('/9j/')
                input64 = img_tag['src'][inds:]
                base64toImg(input64, url, save_path)
            time.sleep(0.3)
            if loop == searchlimit*3:
                break
            loop += 1    
    except Exception as e:
        print(e)
    driver.close()

    
def search_img_hn(shoename, searchlimit):
#    Get images from Highsnobiety
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    word = shoename
    url = 'https://www.highsnobiety.com/?s={}'.format(word)
    # 保存するディレクトリ
    out_path = Path('images')
    out_path.mkdir(exist_ok=True)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    img_tags = soup.find_all('img', attrs={'srcset': True})
#    print(list(enumerate(img_tags)))
    loop = searchlimit
    try:
        for i, img_tag in enumerate(img_tags):
            save_name = '{}_{}.jpg'.format(word, loop)  # 保存するファイル名
            save_path = out_path / save_name  # 保存するパス
            img_url_list = img_tag['srcset']
            ind_start =  img_url_list.index('800w')
            ind_end =  img_url_list.index('1000w')
            img_url = img_url_list[ind_start+6:ind_end-1]
            print(img_url)
            save_image(img_url, save_path)
    #        if img_tag['src'].startswith('/th?'):
    #            save_image(img_url, save_path)
    #        if img_tag['src'].startswith('data:'):
    #            inds = img_tag['src'].index('/9j/')
    #            input64 = img_tag['src'][inds:]
    #            base64toImg(input64, url, save_path)
            time.sleep(0.3)
            if loop == searchlimit*2:
                break
            loop += 1
    except Exception as e:
        print(e)
    driver.close()

    
def search_img_sn(shoename, searchlimit):
#    Get images from Sneakernews
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    word = shoename
    url = 'https://sneakernews.com/?s={}'.format(word)
    # 保存するディレクトリ
    out_path = Path('images')
    out_path.mkdir(exist_ok=True)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    soup_1 = soup.find('section', class_= 'search-result-main')
    img_tags = soup_1.find_all('img', attrs={'src': True})
#    print(list(enumerate(img_tags)))
    loop = 1
    try:
        for i, img_tag in enumerate(img_tags):
            save_name = '{}_{}.jpg'.format(word, loop)  # 保存するファイル名
            save_path = out_path / save_name  # 保存するパス
            img_url = img_tag['src']
            ind = len(img_url)-19
            img_url = img_url[0:ind]
            print(img_url)
            save_image(img_url, save_path)
            time.sleep(0.3)
            if loop == searchlimit:
                break
            loop += 1
    except Exception as e:
        print(e)
    driver.close()

def save_image(url, path):
    print("save {} as {}".format(url, path))
    res = requests.get(url)
    if res.status_code == 200:
        open(path, 'wb').write(res.content)
        
def base64toImg(img_base64, url, path):
    import cv2
    import base64
    import numpy as np

    #画像保存先
    image_file = "{}.jpg".format(path)
    #バイナリデータ <- base64でエンコードされたデータ  
    img_binary = base64.b64decode(img_base64)
    jpg=np.frombuffer(img_binary,dtype=np.uint8)
    
    #raw image <- jpg
    img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
    print("save {} as {}".format(url, path))
    cv2.imwrite(image_file,img) 






