# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

def accumulate(x,y):
	#mac
	df = pd.read_csv("./db/input/release_db_input.csv")
	#windows
	#df = pd.read_csv("¥db¥input¥release_db_input.csv")
	#Access this month's sneakers's list page and extract html
	url = "https://snkrdunk.com/calendars/" + str(x) + "-" + str(y) + "/"
	html = urllib.request.urlopen(url=url)
	#Parse html using BeautifulSoup
	soup = BeautifulSoup(html,"html.parser")
	#Extract all links
	href_head = "https://snkrdunk.com"
	href_tails = soup.find_all("a", attrs={"class": "opacity-link", "target": "_blank"})
	count = 0
	for href_tail in href_tails:
		if(len(href_tails) - 5 <= count <= len(href_tails)):
			count += 1
		elif((count % 4 == 0) and (count // 4 != 0)):
			link = href_head + href_tail.get("href")
			new_row = pd.Series([0,0,0,None,0,0,0,0,0,link,0,0,0],  index = df.columns)
			df = df.append(new_row, ignore_index = True)
#			print(link)
			count += 1
		else:
			count += 1
            

	#mac
	return df
	#windows
	#df.to_csv("¥db¥process¥release_db_accumulate_url.csv")

if __name__ == "__main__":
	accumulate("2019","05")
