def solve(matrix):
   m = len(matrix)
   if m == 1: return matrix[0][0]

   count = 0
   for i in range(m):
      count += matrix[i][i]
      count += matrix[i][-1 - i]

   if m % 2 == 1: count -= matrix[m // 2][m // 2]

   return count

matrix = [[1,5,3,6],[8,1,3,2],[3,8,2,3],[2,1,7,3],]
print(solve(matrix))
