
"""
Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.

If the second largest element does not exist, return -1.

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.


Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.


Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 there is no second largest element.
"""

"""
? There are 3 best ways to solve this problem
! Solution 1: Using sorting
"""

"""
* PSEUDO CODE
* Initialize variable `n`, stores as length of this arr
* Sort the array in non-decreasing order
* Iterate through the array, from the second element of the array, from the right part to -1(imagine the begining)
*     if arr[i] is not equal to arr[n - 1](the largest value):
*         return arr[i]
* Return -1 if cannot find any suitable element  
"""

# def second_largest_ver_1(arr):
#   n = len(arr)
  
#   arr.sort()
  
#   for i in range(n - 2, -1, -1):
#     if arr[i] != arr[n - 1]:
#       return arr[i]
  
#   return -1

# print(second_largest_ver_1([12, 35, 1, 10, 34, 1]))
# print(second_largest_ver_1([10, 5, 10]))
# print(second_largest_ver_1([10, 10, 10]))


#! Solution 2: Two pass search
"""
* PSEUDO CODE
* Find the largest of the array first(using loop or max() function)
* Initialize a variable, store the second largest element of array, default = -1
* Iterate through array, with iterator i
*     if i != max_value and i > second_largest:
*         second_largest = i
* Return second_largest
"""
# def second_largest_ver_2(arr):
#   max_value = max(arr)
  
#   second_largest_value = -1
  
#   for i in arr:
#     if i != max_value and i > second_largest_value:
#       second_largest_value = i
  
#   return second_largest_value

# print(second_largest_ver_2([12, 35, 1, 10, 34, 1]))
# print(second_largest_ver_2([10, 5, 10]))
# print(second_largest_ver_2([10, 10, 10]))

#! Solution 3: One Pass Search
"""
* PSEUDO CODE
* Initialize second_largest and largest to store the second largest and largest element of array, default assign it to -1
* Iterate through arr, with iterator `i`:
*     if arr[i] > largest:
*         update the second largest with largest and largest with arr[i]
*     else if arr[i] < largest and arr[i] > second largest:
*         update the second largest with arr[i]
* Return second largest element
"""

def second_largest_ver_3(arr):
  second_largest = -1
  largest = -1
  
  for i in arr:
    if i > largest:
      second_largest = largest
      largest = i
    elif i < largest and i > second_largest:
      second_largest = i
  
  return second_largest

print(second_largest_ver_3([12, 35, 1, 10, 34, 1]))
print(second_largest_ver_3([10, 5, 10]))
print(second_largest_ver_3([10, 10, 10]))
