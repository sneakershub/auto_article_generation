# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

#mac
df = pd.read_csv("./db/process/release_db_accumulate_url.csv", index_col = 0, encoding = "utf_8_sig")
#windows
#df = pd.read_csv("¥db¥process¥release_db_accumulate_url.csv", index_col = 0, encoding = "utf_8_sig")

def store_title(x,y):
	title_parts = y.split(" ")
	#brand = (title_parts[0])
	#df.iloc[x,0] = brand
	model_name_list = title_parts[1:-1]
	model_name = " ".join(model_name_list)
	df.iloc[x,1] = model_name
	colorway = (title_parts[-1])
	df.iloc[x,2] = colorway

def store_details(x,y):
	d_count = 0
	for i in y:
		details_parts= i.text
		if(d_count == 0):
			brand_split = details_parts.split("(")[1]
			brand = brand_split.split(")")[0]
			df.iloc[x,0] = brand
			print(brand)
			d_count += 1
		elif(d_count == 1):
			d_count += 1
		elif(d_count == 2):
			if(("日" in str(details_parts)) == True):
				release_date = details_parts.replace("年","/").replace("月","/").replace("日","")
				df.iloc[x,3] = release_date
				print(release_date)
				d_count += 1
			else:
				d_count += 1
		elif(d_count == 3):
			price = details_parts
			df.iloc[x,4] = price
			print(price)
			d_count += 1
		elif(d_count == 4):
			item_code = details_parts
			df.iloc[x,5] = item_code
			print(item_code)
			d_count += 1
		else:
			print("More than 5 elements in Sneaker Details")
			d_count += 1

def store_contents(x,y):
	df.iloc[x,6] = str(y.text)

#Access individual article page and extract html
def extract_html(x):
	url = str(df.loc[:,"datasource_url"][x])
	html = urllib.request.urlopen(url=url)
	#Parse html using BeautifulSoup
	soup = BeautifulSoup(html,"html.parser")
	#Extract "brand" "model_name" "colorway" from html
	title = soup.find("p", attrs={"class": "page-title-en"}).text
	store_title(x,title)
	print(title)
	#Extract "price" "release_date" "item_code" from html
	details = soup.find_all("p", attrs={"class": "li-text"})
	store_details(x,details)
	#store_details(x,details)
	#Extract "content" from html
	contents = soup.find("div", attrs={"class": "article-content"})
	store_contents(x,contents)
	#store_contents(x,contents)

def extract():
	count = 0
	for i in df.loc[:,"datasource_url"]:
		extract_html(count)
		count += 1
	#mac
	df.to_csv("./db/process/release_db_extract_info.csv", encoding= "utf_8_sig")
	#windows
	#df.to_csv("¥db¥process¥release_db_extract_info.csv", encoding= "utf_8_sig")

if __name__ == "__main__":
	extract()

"""
for i in df.loc[:,"datasource_url"]:
	if(count == 0):
		extract_html(count)
		count += 1
	else:
		break
"""

"""
#Extract "raffle_info" from html

raffle_url = soup.find_all("a", attrs={"class": "shop-box clearfix"})
raffle_shop = soup.find_all("a", attrs={"class": "name-text"})

print(raffle_url)
print(raffle_shop)
"""
