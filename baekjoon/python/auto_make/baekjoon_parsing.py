import requests
from bs4 import BeautifulSoup
import os
import sys
from googletrans import Translator

path= os.path.dirname(os.path.abspath(__file__))
problem_num = int(sys.stdin.readline())


class autoBaekjoon:
    def __init__(self) -> None:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}        
        URL = f'https://www.acmicpc.net/problem/{problem_num}'
        html = requests.get(URL, headers=headers)
        self.soup = BeautifulSoup(html.content, 'html.parser')

    def parsing(self, id):                
        datas = self.soup.select(f'{id}')        
        return [i.text for i in datas]
    
    def mkdir(self,title_name):
        translator = Translator()
        directory = translator.translate(f"{title_name}", src="ko", dest="en").text.lower().replace(" ","_").replace("'","").replace("[","").replace("]","")
        
        try:
            if not os.path.exists(f"{path}\{directory}"):
                os.makedirs(f"{path}\{directory}")
            with open(f"{path}\{directory}\{directory}.py", "w") as f:
                pass
        except OSError:
            print ('Error: Creating directory. ' +  directory)        

if __name__ == '__main__':
    auto = autoBaekjoon()
    title = auto.parsing("#problem_title") # 문제
    auto.mkdir(title) # 문제 영어로 번역 공백은 _ 처리
    description = auto.parsing("#problem_description") # 설명
    ex_input = auto.parsing("#problem_input") # 입력
    ex_output = auto.parsing("#problem_output") # 출력
    sample_data = auto.parsing(".sampledata") # 예제 입,출력
    
    with open(f"{path}\README.md", "w", encoding="utf-8") as f:
        f.write("# ")
        for i in title:
            f.write(i)

        f.write("\n\n## 문제\n")
        for i in description:
            f.write(i)

        f.write("\n## 입력\n")
        for i in ex_input:
            f.write(i)

        f.write("\n## 출력\n")
        for i in ex_output:
            f.write(i)

        cnt = 1
        for i in range(len(sample_data)):
            if i % 2 == 0:
                f.write(f"\n### 예제 입력{cnt}\n\n")
                f.write("```\n")
                f.write(sample_data[i])
                f.write("```\n")
            else :
                f.write(f"\n### 예제 출력{cnt}\n\n")
                f.write("```\n")
                f.write(sample_data[i])
                f.write("```\n")
                cnt += 1
        
        f.write(f"""\n### 링크\n<a href="https://www.acmicpc.net/problem/{problem_num}" target="_blank">{problem_num}</a>""")
        







    
