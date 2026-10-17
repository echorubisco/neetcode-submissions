class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        chars = ''.join(i for i in s.lower() if i.isalnum())
        if len(chars) == 1:
            return True
        i,j = 0,len(chars)-1
        while i<j:
            if chars[i] == chars[j]:
                i += 1
                j -= 1
            else:
                return False
        return True