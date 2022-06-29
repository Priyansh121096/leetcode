def cherryPickup(g) -> int:
        print('------------')
        R, C = len(g), len(g[0])
        dp = [[[0, 0] for _ in range(C)] for _ in range(R)]
        max0 = max1 = 0
        
        for i in range(R):
            for j in range(C):
                x = g[i][j]
                if i == 0:
                    if j == 0:
                        dp[i][j][0] = x
                    elif j == C-1:
                        dp[i][j][1] = x
                else:
                    if j > i and j < C-1-i:
                        pass
                    else:
                        a0 = dp[i-1][j][0]
                        l0 = dp[i-1][j-1][0] if j > 0 else 0
                        r0 = dp[i-1][j+1][0] if j < C-1 else 0
                        m0 = max(a0, l0, r0)
                        
                        a1 = dp[i-1][j][1]
                        l1 = dp[i-1][j-1][1] if j > 0 else 0
                        r1 = dp[i-1][j+1][1] if j < C-1 else 0
                        m1 = max(a1, l1, r1)
                        
                        if m0 >= m1:
                            dp[i][j][0] = m0 + x
                            
                            if m0 == a0:
                                dp[i][j][1] = max(l1, r1)
                            elif m0 == l0:
                                dp[i][j][1] = max(a1, r1)
                            else:
                                dp[i][j][1] = max(a1, l1)
                        else:
                            dp[i][j][1] = m1 + x
                            
                            if m1 == a1:
                                dp[i][j][0] = max(l0, r0)
                            elif m1 == l1:
                                dp[i][j][0] = max(a0, r0)
                            else:
                                dp[i][j][0] = max(a0, l0)
                            
                            
                if i == R-1:
                    max0 = max(max0, dp[i][j][0])
                    max1 = max(max1, dp[i][j][1])
                                            
        print(dp)
        return max0 + max1

if __name__ == "__main__":
    print(cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
    print(cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))