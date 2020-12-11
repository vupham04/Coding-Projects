# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalin = ''
        for i in range(len(s)):
            left = i
            right = i
            while left>0 and right<(len(s)-1) and s[left-1]==s[right+1]:
                left -= 1
                right += 1
            if(right>=left and (right-left+1)>len(maxPalin)):
                maxPalin = s[left:right+1]
                # aaaa
            left = i
            right = i
            if left>0 and s[left-1]==s[right]:
                left -=1
                while left>0 and right<(len(s)-1) and s[left-1]==s[right+1]:
                    left -= 1
                    right += 1
                if(right>=left and (right-left+1)>len(maxPalin)):
                    maxPalin = s[left:right+1]
        return maxPalin 