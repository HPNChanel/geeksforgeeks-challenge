
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
* Initialize a new arr, set it from the beginning to k-th of array
* Reverse it
* Use slicing technique to combine it
"""

def reverseInGroups(arr, k):
  new_arr = arr[:k]
  new_arr.reverse()
  new_arr += arr[k:]
  
  return new_arr

print(reverseInGroups([1, 2, 3, 4, 5], 3))
print(reverseInGroups([5, 6, 8, 9], 5))

# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 3

# new_arr = arr[:k]
# new_arr.reverse()
# arr = new_arr + arr[k:]
