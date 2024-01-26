from bs4 import BeautifulSoup
import requests
import pandas as pd


with open("index2.html", 'r') as file: 
    html_content = file.read() 
    
souped_html = BeautifulSoup(html_content,"lxml")

print(html_content)

