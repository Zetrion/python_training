# nums = [1,2,3,1]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]:
#             print(True)
#             break
#     else:
#         continue
#     break   
# else:
#     print(False)



l1 = [1, 2, 3, 4, 5, 1, 2]
duplicates = set()
for x in l1:
    if l1.count(x) > 1:
        duplicates.add(x)
print("Duplicates:", duplicates)

