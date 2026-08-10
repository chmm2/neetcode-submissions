class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        
        freq = {chr(i): 0 for i in range(ord('A'), ord('z') + 1)}

        for i in range(len(t)):
            freq[t[i]]+=1
        
        l,r = 0,0
        count = 0
        minLength = float("infinity")
        minIndex = 0

        while r<len(s):
            
            if freq[s[r]] > 0:
                count+=1

            freq[s[r]]-=1
            while count==len(t):
                if r-l+1<minLength:
                    minLength = r-l+1
                    minIndex = l

                freq[s[l]]+=1
                if freq[s[l]] > 0:
                    count-=1
                l+=1                
            r+=1
        return s[minIndex : minIndex + minLength] if minLength != float("infinity") else ""
