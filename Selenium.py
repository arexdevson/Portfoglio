# to generate the .exe file we used pip install pyinstaller
# and to transform it to the executable we use pyinstaller --onefile (name of the python file)
#on the terminal

#before that i need to be on the same directory of my python file
#(venv) PS G:\Meu Drive\Registros\Geral\PycharmProjects\streamlit\.streamlit> cd..
#(venv) PS G:\Meu Drive\Registros\Geral\PycharmProjects\streamlit> cd..
#(venv) PS G:\Meu Drive\Registros\Geral\PycharmProjects> cd python_automação
#(venv) PS G:\Meu Drive\Registros\Geral\PycharmProjects\python_automação>
#(venv) PS G:\Meu Drive\Registros\Geral\PycharmProjects\python_automação> cd FreeCodeAutomation_Python
#(venv) PS G:\Meu Drive\Registros\Geral\PycharmProjects\python_automação\FreeCodeAutomation_Python>

#my executable is going to be on the dist file
#Automate the news - finding element

# gerenciado do google - ele atualiza os drives pra usar sem eu ter que ficar baixando
import pandas as pd
from webdriver_manager import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # serviço pra realizar o gerenciamento
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
import os
import sys
from time import sleep
from pyautogui import alert

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

servico = Service(ChromeDriverManager().install())

#headless mode

url = 'https://thesun.co.uk/sport/football/'
driver = webdriver.Chrome(service=servico)
driver.get(url)

#when we open the google chrome and go to the Inspecionar we can press ctrl+f to create/search for a xpath

#doing so i've created this xpath
#//a[@Class="teaser-anchor"]

#double slash, the tag that i'm searching, class and name

sleep(10)

containers = driver.find_elements(by="xpath",value='//div[@Class="teaser__copy-container"]')

#creating lists that will be appended with the data info
titles = []
subtitles=[]
links=[]
#containers will generate a python list with all the divs information

sleep(2)
# and this for loop is doing the search on each containers about the title
#using the . below it means that he can use the container path
for container in containers:
    title = container.find_element(by="xpath",value='./a/h3').text
    subtitle = container.find_element(by="xpath",value='./a/p').text
    link = container.find_element(by="xpath",value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
#automate the news: exporting data to a csv file

file_name = f'csv_selenium {month_day_year}.csv'

df = pd.DataFrame({'Title':titles,'Subtitle':subtitles,'Links':links})
df.to_csv(file_name,index=False)


sleep(3)

alert('Done!!')

driver.quit()
