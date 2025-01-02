
"""
Given an array arr, rotate the array by one position in clockwise direction.


Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.

Input: arr[] = [9, 8, 7, 6, 4, 2, 1, 3]
Output: [3, 9, 8, 7, 6, 4, 2, 1]
Explanation: After rotating clock-wise 3 comes in first position.

"""

def rotate(arr):
  arr.insert(0, arr.pop())
  return arr

arr = [1, 2, 3, 4, 5]
print(rotate(arr))
# ele = arr.pop()
# print(ele)
# print(arr)