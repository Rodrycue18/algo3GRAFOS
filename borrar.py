import sys

def borrar():
    n = int(sys.stdin.readline())
    
    if n == 0:
        print(0)
        return

    s = sys.stdin.readline().strip()
    
    dp = [[0] * n for _ in range(n)]

    #casos base
    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            dp[i][j] = 1 + dp[i][j-1]
            
            for k in range(i, j):
                if s[k] == s[j]:
                    if k + 1 == j:
                        dp[i][j] = min(dp[i][j], dp[i][k])
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j-1])
                        
    print(dp[0][n-1])

borrar()