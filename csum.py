def csum(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1])
    for x in range(0,length+1)]
    return cu_list[1:]
lists = [1,2,3,4,5]
print(csum(lists))
