str1=input().lower()
str2=input().lower()
ans= 0
for i in range(len(str1)):
    asci=ord(str1[i])
    asci2=ord(str2[i])
    if asci > asci2:
        ans=1
        break
    elif asci < asci2:
        ans=-1
        break
    else:
          continue
print(ans)
 
