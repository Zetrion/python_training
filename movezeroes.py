def movezeroes(nums):
   
    last_non_zero_found_at = 0

    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero_found_at] = nums[current]
            last_non_zero_found_at += 1

    for i in range(last_non_zero_found_at, len(nums)):
        nums[i] = 0
        
print("Enter the numbers in the list separated by space:")
nums = list(map(int, input().split()))        
movezeroes(nums)
print("The list after moving zeroes to the end is:", nums)