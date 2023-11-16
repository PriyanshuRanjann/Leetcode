class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=s.lower()
        new_str=""
        for letter in x:
            if letter.isalnum():
                new_str+=letter
                
        if new_str==new_str[::-1]:
            return True
        else:
            return False
                
        