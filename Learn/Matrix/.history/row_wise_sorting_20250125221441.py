
"""
Given a 2D array, sort each row of this array and print the result.

Examples: 

Input :
77 11 22 3
11 89 1 12
32 11 56 7
11 22 44 33
Output :
3 11 22 77
1 11 12 89
7 11 32 56
11 22 33 44

Input :
8 6 4 5
3 5 2 1
9 7 4 2
7 8 9 5
Output :
4 5 6 8
1 2 3 5
2 4 7 9
5 7 8 9
"""

def sortRowWise(matrix):
  #* Loop for rows of matrix
  for i in range(len(matrix)):
    #* Loop for column of matrix
    for j in range(len(matrix[i])):
      #* Loop for comparison and swapping
      for k in range(len(matrix[i]) - j - 1):
        #* Using bubble sort
        if(matrix[i][k] > matrix[i][k + 1]):
          temp = matrix[i][k]
          matrix[i][k] = matrix[i][k + 1]
          matrix[i][k + 1] = temp
  
  for i in range()