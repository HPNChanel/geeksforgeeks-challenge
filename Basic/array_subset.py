
"""
Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.


Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]
"""

"""
* PSEUDO CODE


"""

def isSubset(a, b):
  set_a = set(a)
  return all(i in set_a for i in b)

print(isSubset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))
print(isSubset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))
print(isSubset([10, 5, 2, 23, 19], [19, 5, 3]))
