k,h=map(int,input().split())
numbers = list(map(int,input().split()))
count=0
for i in numbers:
    if i > h:
        count+=2
    else :
        count+=1
print(count)
