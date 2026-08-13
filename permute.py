class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(path , remaining):
            if not remaining:
              result.append(path)
            return
            for i in range(len(remaining)):
                next_path = path + [remaining[i]]
                next_remaining = remaining[:i] + remaining[i+1:]
                backtrack(next_path, next_remaining)
            
        backtrack([], nums)
        return result                           
    
nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))
solution = Solution()    
print(f"The permutations of the given numbers are: {solution.permute(nums)}")