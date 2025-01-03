
"""
Given an array arr. The task is to find the largest element in the given array. ]

Input: arr[] = [10, 20, 4]
Output: 20
Explanation: Among 10, 20 and 4, 20 is the largest. 


Input: arr[] = [20, 10, 20, 4, 100]
Output: 100
"""

"""
? There are so many ways to solve this exercise, but this 2 ways are easy to understand
* PSEUDO CODE 1
* Initialize a variable, like max_value, assign it to the first element of array(or assign it to 0)
* Iterate through arr, with iterator i
*   if i > max_value:
*     Assign max_value to i
* return max_value
"""

# def largest_ele_ver_1(arr):
#   max_value = arr[0]
#   for i in arr:
#     if i > max_value:
#       max_value = i
  
#   return max_value

# print(largest_ele_ver_1([10, 20, 4]))
# print(largest_ele_ver_1([20, 10, 20, 4, 100]))

"""
* SOLVE 2
* Use max() function
"""
def largest_ele_ver_2(arr):
  return max(arr)

print(largest_ele_ver_2([10, 20, 4]))
print(largest_ele_ver_2([20, 10, 20, 4, 100]))
