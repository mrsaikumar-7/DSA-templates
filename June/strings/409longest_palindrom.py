class Solution:
    def longestPalindrome(self, s: str) -> int:
        f = collections.Counter(s)
        odd = 1
        ans = 0
        print(f)
        for k,v in f.items():
            if v%2 == 1 and odd>0:
                odd -= 1
                ans+=v
            elif v%2==1 :
                ans+=v-1
            else:ans+=v
        return ans
        