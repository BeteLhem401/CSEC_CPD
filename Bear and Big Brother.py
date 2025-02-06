L,b=map(int,input().split())
year=0
while not L > b:
        L=L*3
        b=b*2
        year+=1
print(year)
