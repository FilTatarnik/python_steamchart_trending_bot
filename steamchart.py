# open browser
# go to url bar
# type steamcharts.com  
# screen cap the tranding games
# name picture SteamChartTrend0XX
# save picture somewhere on harddrive
# post picture to certain text channel in discord in personal discord, The Channel
# Profit

##This script uses requests.get(url) to send a GET request to the steamcharts.com website, and stores the response in the response variable. Then it uses the BeautifulSoup function to parse the HTML content of the website and store it in the soup variable.

##Then it uses the find method

import requests
from bs4 import BeautifulSoup

url = 'https://steamcharts.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

trending_table = soup.find('table', class_='common-table')

for row in trending_table.find_all('tr'):
    game_name = row.find('td', class_='game-name')
    if game_name:
        print(game_name.text)

print(game_name.text)