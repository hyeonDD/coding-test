import sys
n = int(sys.stdin.readline())

while n:
    n -= 1
    printer, printer_num = map(int,sys.stdin.readline().split())

    li_printer = [i for i in map(int,sys.stdin.readline().split())]

    num = 1
    for i in li_printer[:printer-1]:        
        if li_printer[printer-1] == i or printer_num > i:
            num += 1
    print(num)

    




