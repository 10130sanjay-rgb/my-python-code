class Solution:
    def isPalindrome(self, num):
        if num < 0:
            return False

        div = 1
        while num >= 10 * div:
            div *= 10

        while num:
            if num // div != num % 10:
                return False
            num = (num % div) // 10
            div //= 100

        return True

# Create object and test with 121
sol = Solution()
print(sol.isPalindrome(121))  # Output: True