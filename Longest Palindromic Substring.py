class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        longest = ""
        
        for i in range(len(s)):
            # Check for odd length palindromes
            palindrome_odd = self.expand_around_center(s, i, i)
            if len(palindrome_odd) > len(longest):
                longest = palindrome_odd

            # Check for even length palindromes
            palindrome_even = self.expand_around_center(s, i, i + 1)
            if len(palindrome_even) > len(longest):
                longest = palindrome_even

        return longest

    def expand_around_center(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]
