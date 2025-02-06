b=int(input())
a=input()
count=0
c=0
for i in range(b):
    if a[i] == 'A':
        count+=1
    else:
        c+=1
if count > c:
    print('Anton')
elif c > count:
    print('Danik')
else:
    print('Friendship')
