
"""
Given an array nums of positive integers of size N. Find all distinct digits present in nums.

Input: nums = [131, 11, 48]
Output: 1 3 4 8
Explanation: 1, 3, 4, and 8 are only distinct
digits that can be extracted from the numbers
of the array.

Input: nums = [111, 222, 333, 4444, 666]
Output: 1 2 3 4 6
Explanation: 1, 2, 3, 4, and 6 are only distinct
digits that can be extracted from the numbers
of the array.
"""

"""
* PSEUDO CODE 1
* Initialize a set to store distinct element
* Iterate through element in original list(convert it to string)
*     Iterate through element in element
*         append to the set
* Convert this set to list
"""

# def common_digits(nums):
#   nums_set = set()
  
#   for i in nums:
#     for j in str(i):
#       nums_set.add(int(j))
  
#   return sorted(list(nums_set))

# print(common_digits([131, 11, 48]))
# print(common_digits([111, 222, 333, 4444, 666]))


"""
* PSEUDO CODE 2
* Create a set to store distinct digits
* Iterate over each number in the array
*     Convert the number to a string and add each digit to the set
* Convert the set to a sorted list of integers
* Return the result(set)
"""

def common_digits(nums):
  distinct_digits = set()
  
  for num in nums:
    distinct_digits.update(str(num))  #! Lưu ý khi sử dụng: khi sử dụng set, các phần tử dưới dạng chuỗi sẽ được phân tách thành các ký tự riêng lẻ 
  
  result = sorted(int(digit) for digit in distinct_digits)
  
  return list(result)

print(common_digits([131, 11, 48]))
print(common_digits([111, 222, 333, 4444, 666]))
