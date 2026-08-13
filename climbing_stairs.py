def climbingStairs(n: int) -> int:
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

st = int(input("Enter the number of stairs: "))
print(f"The number of distinct ways to climb {st} stairs is: {climbingStairs(st)}.")