
"""
Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

Input: arr[] = [1, 2, 3, 4], x = 3
Output: 2
Explanation: There is one test case with array as [1, 2, 3 4] and element to be searched as 3. Since 3 is present at index 2, the output is 2.


Input: arr[] = [10, 8, 30, 4, 5], x = 5
Output: 4
Explanation: For array [1, 2, 3, 4, 5], the element to be searched is 5 and it is at index 4. So, the output is 4.


Input: arr[] = [10, 8, 30], x = 6
Output: -1
Explanation: The element to be searched is 6 and its not present, so we return -1.
"""

"""
* PSEUDO CODE

* Iterate through value in arr with value i
*   if arr[i] == x:
*     return i
*   else return -1
"""

def linear_search(arr, x):
  index = 0
  for i in range(len(arr)):
    if arr[i] == x:
      index = i
      break
    else:
      index = -1
  
  return index

arr = [10, 8, 30]
x = 5
print(linear_search(arr, x))
