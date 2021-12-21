pyinstaller -F baekjoon_parsing.py
rmdir /s /q .\__pycache__\
rmdir /s /q .\build\
del /q .\baekjoon_parsing.spec
move D:\code\github\coding_test\baekjoon\python\auto_make\dist\baekjoon_parsing.exe D:\code\github\coding_test\baekjoon\python\auto_make
rmdir /s /q .\dist\