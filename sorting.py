x=[]
l=int(input("enter the length of the list"))
for i in range(l):
    y = int(input("Enter a values of list :"))
    x.append(y)
print(x)
x.sort()
print("ascending list"+str(x))
x.sort(reverse = True )
print("descending list"+str(x))
