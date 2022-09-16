a=int(input())
b=[]
k=1
for i in range(a):
    b.append((i+1))
    x=len(b)
    while (x-k)!=0 and x<=a:
        k+=1
        b.append((i+1))
    k=x
b=b[0:a]
print(*b)
