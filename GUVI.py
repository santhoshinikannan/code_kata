a,b=map(int,input().split())
c=list(map(int,input().split()))
c= [c [(i-b) % len(c)] for i,x in enumerate(c)]
print(*c)
