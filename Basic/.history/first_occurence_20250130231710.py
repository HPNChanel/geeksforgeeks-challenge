
"""
Find the first occurrence of the string pat in the string txt. The function returns an integer denoting the first occurrence of the string pat in txt (0-based indexing).

Examples :

Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1
Explanation: Fr is not present in the string GeeksForGeeks as substring.
Input: txt = "GeeksForGeeks", pat = "For"
Output: 5
Explanation: For is present as substring in GeeksForGeeks from index 5 (0 based indexing).
Input: txt = "GeeksForGeeks", pat = "gr"
Output: -1
Explanation: gr is not present in the string GeeksForGeeks as substring.
"""
"""
* PSEUDO CODE
* Initialize index_string equals to 0
*     Iterating over given string txt to search for pattern pat
*         If the character of txt at ind_s equals to the first character of pattern:
*             Using two-pointers technique to solve:
*               Initialize ind_p(index_pattern) equals to 0
*                   Initialize temp_s (temporary string), assign ind_s to this
*                       Checking for string pat from current index i in the string txt
*                         If string pat is found, return the starting index
"""

def firstOccurence(txt, pat):
  ind_s = 0
  
  while ind_s < len(txt):
    if txt[ind_s] == pat[0]:
      ind_p = 0
      temp_s = ind_s
      
      while temp_s < len(txt) and txt[temp_s] == pat[ind_p]:
        ind_p += 1
        temp_s += 1
        
        if ind_p == len(pat):
          return ind_s
    ind_s += 1

print(firstOccurence("GeeksForGeeks", "Fr"))
print(firstOccurence("GeeksForGeeks", "For"))
print(firstOccurence("GeeksForGeeks", "gr"))