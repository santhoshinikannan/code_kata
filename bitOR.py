N = int(input())
c = list(map(int,input().split()))
b = c[0]
for i in range(1,N):
	b = b | c[i]
print(b)
