
"""
You are given a string s, and your task is to reverse the string.

Input: s = "Geeks"
Output: "skeeG"
Input: s = "for"
Output: "rof"
Input: s = "a"
Output: "a"
"""

"""
* PSEUDO CODE
* start from the end to the beginning of the string
"""

def reverseString(s: str) -> str:
  return s[::-1]

print(reverseString("Geeks"))
print(reverseString("for"))
print(reverseString("a"))