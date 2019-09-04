A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
D=list(map(int,input().split()))
d1 = C[0] - A[0]
d2 = D[0] - B[0]
d3 = B[1] - A[1]
d4 = C[1] - D[1]
if (d1 == d2 and d3 == d4):
	print("yes")
else:
	print("no")
