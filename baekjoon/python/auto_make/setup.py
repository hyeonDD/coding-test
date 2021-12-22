from cx_Freeze import setup, Executable
 
buildOptions = dict(packages=["bs4","googletrans"], excludes = [])
 
exe = [Executable('baekjoon_parsing.py')]
 
setup(
    name='baekjoon_parsing',
    version='1.0.0',
    author='hdc',
    description = 'Baekjoon codingtest create auto',
    options = dict(build_exe = buildOptions),
    executables = exe
)