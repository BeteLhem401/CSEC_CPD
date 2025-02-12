c=list(input())

instraction=list(input())
length=len(instraction)
k=0
postion=1
for i in range(length):
    if c[k] == instraction[i]:
        postion+=1
        k+=1
print(postion)
