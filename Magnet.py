n=int(input())
magnet=[]
for i in range(n):
    mag=int(input())
    magnet.append(mag)
count=1
for i in range(n-1):
    if magnet[i] == magnet[i+1]:
        continue
    else:
        count+=1
print(count)
