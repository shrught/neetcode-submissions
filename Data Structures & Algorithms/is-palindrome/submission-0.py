class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        head, tail = 0, len(s) - 1

        while tail > head:
            if s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        
        return True
            

        
        