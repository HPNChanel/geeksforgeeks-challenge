
"""
You are given an integer n. You need to convert all zeroes of n to 5.

Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.

Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121.

"""

"""
* PSEUDO CODE
* Convert int n to string n
* For loop through string n:
*     if '0' in string n:
*         replace '0' to '5'
* Return integer part of string n
"""

def convertFive(n):
  n_str = str(n).replace('0', '5')
  
  return int(n_str)

print(convertFive(1004))
print(convertFive(121))