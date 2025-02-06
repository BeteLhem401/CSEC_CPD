n=int(input())
count=0
for i in range(n) :
    view=list(map(int,input().split()))
    if view.count(1) >= 2:
        count+=1
print(count)
