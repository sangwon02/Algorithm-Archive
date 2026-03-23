import sys
input = sys.stdin.readline

def lcs(st1, st2):
    st1_len, st2_len = len(st1), len(st2)
    dp = [[0] * (st2_len + 1) for _ in range(st1_len + 1)]

    for i in range(0, st1_len):
        for j in range(0, st2_len):
            
            if st1[i] == st2[j]: 
                dp[i+1][j+1] = dp[i][j] + 1
                
            else: 
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    return dp[st1_len][st2_len]


st1 = input().rstrip()
st2 = input().rstrip()

print(lcs(st1, st2))