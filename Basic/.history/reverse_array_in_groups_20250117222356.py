
"""
Given an array arr of positive integers. Reverse every sub-array group of size k.

Note: If at any instance, k is greater or equal to the array size, then reverse the entire array. You shouldn't return any array, modify the given array in place.

Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
Input: arr[] = [5, 6, 8, 9], k = 5
Output: [9, 8, 6, 5]
Explnation: Since k is greater than array size, the entire array is reversed.
"""

"""
* PSEUDO CODE
* Initialize n as a size of arr
* Iterate arr from 0 to n with k step
*     Determine the end of the current sub-array, initialize left = i
*     Initialize right = min(i + k - 1, n - 1)
*     Make a loop to reverse element in the current sub-array (left < right)
*         Make arr[left] = arr[right], arr[right] = arr[left]
*         Add 1 to left and minus 1 from right
"""

def reverseInGroups(arr, k):
  n = len(arr)
  
  for i in range(0, n, k):
    left = i
    right = min(i + k - 1, n - 1)
    while left < right:
      arr[left], arr[right] = arr[right], arr[left]
      left += 1
      right -= 1
      
      
arr = [1, 2, 3, 4, 5]
k = 3
reverseInGroups(arr, k)
print(arr)

arr1 = [1, 2, 3, 4, 5]
k1 = 3

reverseInGroups(arr1, k1)
print(arr1)

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 3

# new_arr = arr[:k]
# new_arr.reverse()
# arr = new_arr + arr[k:]
