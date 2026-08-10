class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        if(k>n):
            return False
        s1Count = [0]*26
        window = [0]*26

        for i in range(k):
            s1Count[ord(s1[i])- ord('a')] += 1
            window[ord(s2[i])- ord('a')] += 1

        if s1Count == window:
            return True
        
        for i in range(k,n):
            window[ord(s2[i-k])-ord('a')] -= 1
            window[ord(s2[i])-ord('a')] += 1

            if window == s1Count:
                return True

        return False