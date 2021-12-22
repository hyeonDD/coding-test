import requests
from bs4 import BeautifulSoup
import os
import sys
from googletrans import Translator

path= os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) != 2:
    print("실행방법 .\\baekjoon_parsing.exe 문제번호")
    sys.exit()

problem_num = sys.argv[1]
# problem_num = int(input())


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
        directory_name = translator.translate(f"{title_name}", src="ko", dest="en").text.lower().replace(" ","_").replace("'","").replace("[","").replace("]","")
        
        try:
            if not os.path.exists(f"{path}\{directory_name}"):
                os.makedirs(f"{path}\{problem_num}")
            with open(f"{path}\{problem_num}\{directory_name}.py", "w") as f:
                pass
        except OSError:
            print ('Error: already directory exist.' +  directory_name)

    def mkreadme(self,title,description,ex_input,ex_output,sample_data):
        with open(f"{path}\{problem_num}\README.md", "w", encoding="utf-8") as f:
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
        


if __name__ == '__main__':
    auto = autoBaekjoon()
    title = auto.parsing("#problem_title") # 문제
    auto.mkdir(title) # 문제 파일이름 번역 공백은 _ 처리
    description = auto.parsing("#problem_description") # 설명
    ex_input = auto.parsing("#problem_input") # 입력
    ex_output = auto.parsing("#problem_output") # 출력
    sample_data = auto.parsing(".sampledata") # 예제 입,출력
    auto.mkreadme(title,description,ex_input,ex_output,sample_data) # readme 파일 생성    







    
