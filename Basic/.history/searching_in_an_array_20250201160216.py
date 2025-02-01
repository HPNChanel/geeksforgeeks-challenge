
"""
Given an integer k and array arr. Your task is to return the position of the first occurrence of k in the given array and if element k is not present in the array then return -1.

Note: 1-based indexing is followed here.

Input: k = 16 , arr = [9, 7, 16, 16, 4]
Output: 3
Explanation: The value 16 is found in the given array at positions 3 and 4, with position 3 being the first occurrence.

Input: k=98 , arr = [1, 22, 57, 47, 34, 18, 66]
Output: -1
Explanation: k = 98 isn't found in the given array.
"""

"""
* PSEUDO CODE
* Initialize target index with value -1: target_idx
* Iterate through the loop, with loop variable: i
*   If k == arr[i]:
*       target_idx = i
"""

from typing import List

def search(k: int, arr: List[int]) -> int:
  target_idx = -1
  
  for i in range(len(arr)):
    if k == arr[i]:
      target_idx = (i + 1)
      break
  
  return target_idx

print(search())