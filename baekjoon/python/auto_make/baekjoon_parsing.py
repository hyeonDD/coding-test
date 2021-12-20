import requests
from bs4 import BeautifulSoup
import openpyxl


def problem_search():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v5861995922 t38550 ath9b965f92 altpub'}
        # 어떤 브라우저로 웹에 접속 했는지 명시
    URL = 'https://www.acmicpc.net/problem/1021'
    # URL = f'https://www.acmicpc.net/problem/{problem_num}'
    html = requests.get(URL, headers=headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    
    datas = soup.select('#problem_description')
    # print (datas)
    for data in datas:
        # print (data.text)
        print (data.name)
        
        

    # return realtime_set

if __name__ == '__main__':
    realtime_set = problem_search()
    
