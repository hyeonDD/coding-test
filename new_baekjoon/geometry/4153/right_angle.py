# print(25+144,13**2)
def is_triangle(x,z):
    if x==z:
        return "right"
    return "wrong"
while True:
    a=list(map(int,input().split()))
    if a[0]==0 and a[1]==0 and a[2]==0:
        break
    z=max(a)**2
    a.remove(max(a))
    x=a[0]**2+a[1]**2    
    print(is_triangle(x,z))