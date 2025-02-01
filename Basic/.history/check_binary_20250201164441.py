
"""
Given a non-empty sequence of characters s, return true if sequence is Binary, else return false.

Input: s = "101"
Output: true
Explanation: Since string contains only '0' and '1', output is true.

Input: s = "75"
Output: false
Explanation: Since string contains digits other than '0' and '1', output is false.
"""

def isBinary(s):
  count = 0
  
  for c in s:
    if c == '0' or c == '1':
      count += 1
  
  if count == len(s):
    return True
  
  return False

print(isBinary('102'))
print(isBinary('75'))