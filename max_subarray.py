#find subarray with largest sum and print it
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return arr[start:end + 1], max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
subarray, total_sum = max_subarray_sum(nums)

print(f"Max Subarray: {subarray}") 
print(f"Max Sum: {total_sum}")