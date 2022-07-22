n,m=map(int,input().split())
haves={i:input() for i in range(1,n+1)}
haves_2={v:k for k,v in haves.items()}
finds=[input() for _ in range(m)]

for find in finds:
    try:
        print(haves[int(find)])
    except ValueError:
        print(haves_2[find])
