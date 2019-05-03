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
accumulate_url.accumulate("2019","04")

from pyfiles import extract_info
df = pd.read_csv("./db/process/release_db_accumulate_url.csv", index_col = 0, encoding = "utf_8_sig")
#windows
#df = pd.read_csv("¥db¥process¥release_db_accumulate_url.csv", index_col = 0, encoding = "utf_8_sig")
extract_info.extract()

from pyfiles import create_post
#mac
df_db = pd.read_csv("./db/process/release_db_extract_info.csv", index_col = 0, encoding = "utf_8_sig")
df_temp = pd.read_csv("./db/input/Post_template.csv", index_col = 0, encoding = "utf_8_sig")
"""
#windows
df_db = pd.read_csv("¥db¥process¥release_db_extract_info.csv", index_col = 0, encoding = "utf_8_sig")
df_temp = pd.read_csv("¥db¥input¥Post_template.csv", index_col = 0, encoding = "utf_8_sig")
"""
create_post.add_contents()

df2 = pd.read_csv("./db/output/release_db_create_post.csv", index_col = 0, encoding = "utf_8_sig")
create_post.create_weekly_content('2019/04/22', '2019/04/28')
