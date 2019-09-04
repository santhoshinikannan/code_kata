z=int(input())
c=[]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(0,len(a)):
    x=a[i]+b[i]
    c.append(x)
for i in c:
    print(i,end=" ")
