# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 80ms, 14.3MB
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        sidx = 0
        eidx = 0
        info = {}
        for i in range(len(s)):
            eidx = i
            if sidx == eidx:
                ans = max(ans, 1)
                info[s[i]] = i
                continue
            
                
            if s[eidx] in s[sidx:eidx]:
                ans = max(ans, (eidx-sidx))
                sidx = info[s[eidx]] + 1
                info[s[eidx]] = i 
                
            else:
                if i == (len(s) - 1) :
                  ans = max(ans, (eidx-sidx+1))
                info[s[i]] = i

        return ans
