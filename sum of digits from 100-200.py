list=[]
for i in range(100,201):
    i=str(i)
    sum=0
    for j in i:
        j=int(j)
        sum=sum+j
    if sum%2==0:
        list.append(i)
print('All Integers Within The Range 100-200 Whose Sum Of Digits Is An Even Number is =',list)
