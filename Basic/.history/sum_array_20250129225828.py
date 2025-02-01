
"""
Given an array arr[] of integers, change the given array such that at any index i it contains the sum of all elements except itself. Simple way arr[i] should be arr[0] + arr[1] ... arr[i-1] + arr[i+1] ... arr[n-1].

Input: [3, 6, 4, 8, 9]
Output: [27, 24, 26, 22, 21]
Explanation: For the sum array, at i=0 we have 6+4+8+9. At i=1, 3+4+8+9. At i=2, we have 3+6+8+9. At i=3, we have 3+6+4+9. At i = 4, we have 3+6+4+8. So S is 27 24 26 22 21.

Input: [0, 0, 1]
Output: [1, 1, 0]
Explantion: At i = 0 sum = 0 + 1 = 1, At i = 1 sum = 0 + 1 = 1, At i = 2 sum = 0 + 0 = 0. 
"""

"""
* PSEUDO CODE
* Initialize an array contain sum of elements
* Using list comprehension:
*     In each iteration, return (sum all of the elements) minus this element
"""

def sumArray(arr):
  sum
  sum_arr = [sum(arr) - arr[i] for i in range(len(arr))]
  return sum_arr
  # sum_val = 0
  
  # for i in range(len(arr)):
  #   sum_val = sum(arr) - arr[i]
  #   sum_arr.append(sum_val)
  #   sum_val = 0
  
  # return sum_arr


print(sumArray([3, 6, 4, 8, 9]))