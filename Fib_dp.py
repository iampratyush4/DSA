def  fib(n,dp):
    if n==0 or n ==1:
        return n
    elif dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=fib(n-1,dp)+fib(n-2,dp)
        return dp[n]
    
dp=[-1]*8
print(fib(7,dp))
# ends here okayyY