s=input()
li=list(s)
for i in range (0,len(li),2):
    if (i < len(li)-1):
        li[i],li[i+1]=li[i+1],li[i]
s="".join(li)
print(s)
