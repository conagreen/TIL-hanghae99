# 지니뮤직의 1~50위 곡 스크래핑 (순위 / 곡 제목 / 가수)

import requests 
from bs4 import BeautifulSoup 

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

all_music = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in all_music:
    rank = music.select_one('td.number').text[0:2].strip()
    title = music.select_one('td.info > a.title.ellipsis').text.strip()
    artist = music.select_one('td.info > a.artist.ellipsis').text.strip()

    print(rank, title, artist)