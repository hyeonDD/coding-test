# (100~1~|01)~
import sys
import re

input=sys.stdin.readline

string=input().rstrip()

p = re.compile('(100+1+|01)+')
is_match = p.fullmatch(string)

if is_match:
    print("SUBMARINE")
else:
    print("NOISE")
