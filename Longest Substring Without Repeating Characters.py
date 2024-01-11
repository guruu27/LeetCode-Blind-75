class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char= set()
        result=0
        x=0
        for y in range(len(s)):
            while s[y] in char:
                char.remove(s[x])
                x+=1
            char.add(s[y])
            result= max(result, y-x+1)
        return result
