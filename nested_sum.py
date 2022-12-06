def nested_sum(t):
    total=0
    for j in t:
        if type(j) == list :
            total+= nested_sum(j)
        else:
            total = total+j
    return total
a=nested_sum([[1,2],[3],[4,5,6]])
print(a)
