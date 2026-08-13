def rob(self, nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]

print("Enter the amounts of money in each house separated by spaces:")
nums = list(map(int, input().split()))
print(f"The maximum amount of money that can be robbed is: {rob(None, nums)}")