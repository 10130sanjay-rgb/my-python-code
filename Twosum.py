class Solution:
    def twoSum(self, nums=(2, 5, 6, 7), target=7):
        required = {}  #disctonry
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i

# Create an instance and call the method
sol = Solution()
print(sol.twoSum())