from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


with open("index2.html", 'r', encoding='utf-8') as file: 
    html_content = file.read() 
    
souped_html = BeautifulSoup(html_content,"lxml")
three_fav = souped_html.find_all("h4")
list_first_fav = souped_html.find_all('li',class_="first-bullet")
list_second_fav = souped_html.find_all('li',class_="second-bullet")
list_third_fav = souped_html.find_all('li',class_="third-bullet")

# for favourites in three_fav:
#     print(favourites.text.strip())

# for each_fav in list_first_fav:
#     print(each_fav.text.strip())

# for each_fav in list_second_fav:
#     print(each_fav.text.strip())

# for favourites in three_fav:
#     print(favourites.text.strip())


df = pd.DataFrame({
    "Favourites":[head_fav.text.strip() for head_fav in three_fav],
    "1st Fav":[first_fav.text.strip()for first_fav in list_first_fav],
    "2nd Fav":[second_fav.text.strip() for second_fav in list_second_fav],
    "3rd Fav":[third_fav.text.strip() for third_fav in list_third_fav]
}).T

print(df)
df.to_excel("Three_favourites.xlsx",index=False)