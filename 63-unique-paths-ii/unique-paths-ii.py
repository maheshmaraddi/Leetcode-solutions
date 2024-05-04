class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        m=len(obs)
        n=len(obs[0])
        # print(m,n)
        dp=[[0] * n for _ in range(m)]        
        if obs[0][0]!=1:
            dp[0][0]= 1
        if m==1:
            for i in range(1,n):
                if obs[0][i]!=1:
                    dp[0][i]=dp[0][i-1]
                else:
                    dp[0][i]=0


        if m>1:
            for i in range(m):
                for j in range(n):
                    if i==0 and j==0:
                        continue
                    else:
                        if obs[i][j]!=1:
                            if i==0:
                                dp[i][j]=dp[i][j-1]
                            if j==0:
                                dp[i][j]=dp[i-1][j]
                            else:
                                dp[i][j]= dp[i-1][j]+dp[i][j-1]   
                        else:
                            dp[i][j]=0
        return dp[m-1][n-1]
        