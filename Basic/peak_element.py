
"""
Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.


Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6]. 
Input: arr = [1, 2, 3]
Output: true
Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element, so it has negative infinity to its right.
"""

"""
* PSEUDO CODE

* Initialize left and right pointers to 0 and length of arr - 1
* While left is less than or equal to right:
*     Initialize mid as (left + right) // 2
*     Check if mid is a peak element
*         If true, return mid
*     If the left neighbor is greater, move to the left half
*         right = mid - 1
*     Otherwise, move to the right half
*         left = mid + 1
* Return -1 if no peak element is found
"""

def find_peak(arr):
  left, right = 0, len(arr) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    #* Check if mid is a peak element
    if(mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
      return mid
    
    #* Move to the left half if the left neighbor is greater
    if mid > 0 and arr[mid - 1] > arr[mid]:
      right = mid - 1
    else:  #* Move to the right half otherwise
      left = mid + 1

print(find_peak([1, 2, 3]))
print(find_peak([1, 2, 4, 5, 7, 8, 3]))
print(find_peak([10, 20, 15, 2, 23, 90, 80]))
