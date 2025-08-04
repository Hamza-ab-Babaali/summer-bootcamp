def isIsomorphic(s, t):
        dct_s={}
        dct_t={}
        for i in range(len(s)):
            chars=s[i]
            chart=t[i]
            if chars in dct_s and dct_s[chars]!=chart:
                     return False

            
            if chart in dct_t and dct_t[chart]!=chars:
                     return False

            dct_s[chars]=chart
            dct_t[chart]=chars

        return True
            
print(isIsomorphic("foo","bar"))