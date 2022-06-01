## https://leetcode.com/problems/jewels-and-stones/
# 47ms, 13.9MB
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for j in jewels:
            ans += stones.count(j)
        return ans
