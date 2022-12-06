def has_duplicates(list1,list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(has_duplicates([1,2,3,4,5],[5,6,7,8,9]))
print(has_duplicates([1,2,3,4,5],[6,7,8,9]))
