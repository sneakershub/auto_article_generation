# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import time
import requests
import os
from selenium import webdriver
from pyfiles import accumulate_url
from pyfiles import extract_info
from pyfiles import create_post


df_ac = accumulate_url.accumulate("2019","05")
print('URL accumulation completed!')

#df = pd.read_csv("./db/process/release_db_accumulate_url.csv", index_col = 0, encoding = "utf_8_sig")
#windows
#df = pd.read_csv("¥db¥process¥release_db_accumulate_url.csv", index_col = 0, encoding = "utf_8_sig")
df_ex = extract_info.extract(df_ac)
print('Info extraction completed!')

#mac
#df_db = pd.read_csv("./db/process/release_db_extract_info.csv", index_col = 0, encoding = "utf_8_sig")
df_temp = pd.read_csv("./db/input/Post_template.csv", index_col = 0, encoding = "utf_8_sig")
"""
#windows
df_db = pd.read_csv("¥db¥process¥release_db_extract_info.csv", index_col = 0, encoding = "utf_8_sig")
df_temp = pd.read_csv("¥db¥input¥Post_template.csv", index_col = 0, encoding = "utf_8_sig")
"""
df_c = create_post.add_contents(df_ex,df_temp)

#df2 = pd.read_csv("./db/output/release_db_create_post.csv", index_col = 0, encoding = "utf_8_sig")
create_post.create_weekly_content(df_c,df_temp,'2019/05/13', '2019/05/21')
print('HTML export completed!')
