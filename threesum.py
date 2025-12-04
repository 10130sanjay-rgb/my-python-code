class Solution:
    def Threesum(self, num):
        num.sort()  # Sort the array
        result = []  # Store the triplets

        for i in range(len(num) - 2):  # Loop till third last element
            if i > 0 and num[i] == num[i - 1]:
                continue  # Skip duplicates

            left = i + 1 # inc from left 
            right = len(num) - 1 # dec from right 

            while left < right:
                total = num[i] + num[left] + num[right]

                if total == 0:
                    result.append([num[i], num[left], num[right]])

                    # Skip duplicates for left
                    while left < right and num[left] == num[left + 1]:
                        left += 1

                    # Skip duplicates for right
                    while left < right and num[right] == num[right - 1]:
                        right -= 1
                    # for move to next number 
                    left += 1 
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

# ✅ Create object and pass a list (not individual numbers)
sol = Solution()
print(sol.Threesum([-1, 0, 1, 2, -1, 4]))
# instent we can give param = [-1, 0, 1, 2, -1, -4]
#sol = Solution().threeSum(param)
#print(sol)