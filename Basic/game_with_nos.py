
"""
You are given an array arr[], and you have to re-construct an array arr[].
The values in arr[] are obtained by doing Xor of consecutive elements in the array.

Input : n=5, arr[ ] = {10, 11, 1, 2, 3}
Output : 1 10 3 1 3
Explanation:
At index 0, arr[0] xor arr[1] = 1
At index 1, arr[1] xor arr[2] = 10
At index 2, arr[2] xor arr[3] = 3
...
At index 4, No element is left So, it will remain as
it is.
New Array will be {1, 10, 3, 1, 3}.
"""

"""
* PSEUDO CODE

* declare new xor arr 
* for i in range from 0 to n:
*   if i is equal to array's length(n - 1)
*     append arr[i] to new xor arr
*   append arr[i] XOR arr[i+1] to new xor arr
* return new xor arr
"""
def game_with_number(arr, n):
  new_xor_arr = []

  for i in range(n):
    if i == (n - 1):
      new_xor_arr.append(arr[i])
      break
      
    new_xor_arr.append(arr[i] ^ arr[i + 1])
    
  
  return new_xor_arr


print(game_with_number([10, 11, 1, 2, 3], 5))
