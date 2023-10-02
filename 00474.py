# https://leetcode.com/problems/ones-and-zeroes/
# 474. Ones and Zeroes

# Came up with DP myself.

# Solution 1 (AC)
# TC: O(Smn); SC: O(Smn)
from collections import Counter
from typing import List

def findMaxForm(strs: List[str], m: int, n: int) -> int:
    a = [[[0 for _ in range(n+1)] for __ in range(m+1)] for ___ in range(len(strs))]
    counts = [Counter(s) for s in strs]
    
    for x in range(len(strs)):
        for i in range(len(a[0])):
            for j in range(len(a[0][0])):
                # x = index of str
                # i = number of 0s left
                # j = number of 1s left
                
                if i == 0 and j == 0:
                    # If we have no 0s and 1s; answer is 0.
                    continue
                    
                c = counts[x]
                
                if x == 0:
                    if i >= c['0'] and j >= c['1']:
                        # There are enough 0s and 1s; include this string.
                        a[x][i][j] = 1
                else:
                    if i < c['0'] or j < c['1']:
                        # There are not enough 0s and 1s left to accommodate
                        # this string; exclude this.
                        a[x][i][j] = a[x-1][i][j]
                    else:
                        # This string can be included. Figure out whether 
                        # including the string will increase the subset length
                        # or not.
                        a[x][i][j] = max(
                            1 + a[x-1][i-c['0']][j-c['1']],
                            a[x-1][i][j]
                        )

    return a[len(a)-1][m][n]               
                    
print(findMaxForm(["10","0001","111001","1","0"], 5, 3))