X = [[1,2,3],
    [2,3,1],
    [3,1,2]]

Y = [[5,4,6],
    [6,5,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
  for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)
