# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:49:09 2019

@author: seita
"""

#import urllib.request
import pandas as pd

##mac
#df_db = pd.read_csv("./db/process/release_db_extract_info.csv", index_col = 0, encoding = "utf_8_sig")
#df_temp = pd.read_csv("./db/input/Post_template.csv", index_col = 0, encoding = "utf_8_sig")
"""
#windows
df_db = pd.read_csv("¥db¥process¥release_db_extract_info.csv", index_col = 0, encoding = "utf_8_sig")
df_temp = pd.read_csv("¥db¥input¥Post_template.csv", index_col = 0, encoding = "utf_8_sig")
"""

def create_single_content(df_db,df_temp,ind):
    Name = df_db.loc[ind,'brand'] + ' ' + df_db.loc[ind,'model_name']
    Price = df_db.loc[ind,'price']
    Article = df_temp.loc['NAME','Content'].format('{"level":3}',Name) + '\n'\
    + df_temp.loc['IMG','Content'] + '\n'\
    + df_temp.loc['PRICE','Content'].format(Price) + '\n'\
    + df_temp.loc['MAIN','Content'] + '\n'\
    + df_temp.loc['LINK','Content'] + '\n'

    df_db.loc[ind,'Post_Content'] = Article

def add_contents(df_c,df_tmp):
    df_c['Post_Content'] = 0
    ind = 0
    for i in df_c['Post_Content']:
        create_single_content(df_c,df_tmp,ind)
        ind += 1
    #mac
    df_c.to_csv("./db/output/release_db_create_post.csv", encoding = "utf_8_sig")
    return df_c
    #windows
    #df_db = pd.read_csv("release_db_out_4.csv", index_col = 0, encoding = "utf_8_sig")

if __name__ == "__main__":
   add_contents()
#
#df2 = pd.read_csv("./db/output/release_db_create_post.csv", index_col = 0, encoding = "utf_8_sig")

def create_weekly_content(df2,df_temp, start, end):
    from pyfiles import get_imgs
    df2['release_date'] = pd.to_datetime(df2['release_date'])
    df2.sort_values(by=['release_date'], ascending = True, inplace = True)
    filt1 = (df2['release_date'] >= start)
    filt2 = (df2['release_date'] <= end)
    df_filtered = df2[filt1 & filt2]
    df_filtered.reset_index(inplace = True)
    row = 0
    Article = df_temp.loc['HEADER','Content'] + '\n'
    c_date = pd.to_datetime(start) - pd.offsets.Day()
    while row < len(df_filtered['Post_Content']):
#    for i in df_filtered['Post_Content']:
        if c_date == df_filtered.loc[row,'release_date']:
            Article = Article + df_filtered.loc[row,'Post_Content'] + '\n'
            name = df_filtered.loc[row,'brand'] + ' ' + \
            df_filtered.loc[row,'model_name'] + ' ' + df_filtered.loc[row,'colorway']
            print(name)
            get_imgs.search_img(name, 3)
            row += 1
        elif  c_date < df_filtered.loc[row,'release_date']:
            c_date += pd.offsets.Day() 
            if c_date == df_filtered.loc[row,'release_date']:
                strdate = c_date.strftime('%m/%d')
                Article = Article + df_temp.loc['DATE','Content'].format(strdate) + '\n'
    f = open('./db/output/Article.txt', 'w', encoding = "utf_8_sig") # 書き込みモードで開く
    f.write(Article) # 引数の文字列をファイルに書き込む
    f.close() #\


if __name__ == "__main__":
    create_weekly_content('2019/04/22', '2019/04/28')
