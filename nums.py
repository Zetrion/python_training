n=int(input("Enter total numbers:"))
nums=list(map(int,input(f"Enter  numbers in the list").split()))

exp_sum_sq=n*(n+1)*(2*n+1)//6
exact_sum_sq=sum([i*i for i in nums])
exp_sum=n*(n+1)//2
exact_sum=sum(nums)
difference=exp_sum-exact_sum
sq_difference=exp_sum_sq-exact_sum_sq
summ=sq_difference//difference
missing=(difference+summ)//2
duplicate=summ-missing
print(missing)
print(duplicate)