# Write your code here :-)
for x in range(1,101):
    if x%2==0:
       print(x)
       print("these are the even numbers")
    for x in range(1,101):
        if x%2!=0:
            print(x)
            print("these are the odd numbers")
    for number in range(1,101):
            count=0
            for i in range(2,(number//2+1)):
                if number%i==0:
                    count=count+1
                    break
            if count==0 and number!=1:
                    print("%d" %number,end=" ")
                    print("these are the prime numbers")
