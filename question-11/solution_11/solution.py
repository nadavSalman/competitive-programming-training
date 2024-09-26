class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if 0 <= x < 9:
            return True
        elif x < 0 or x % 10 == 0:
            return False
       
        dest = 0
        while dest < x :
            dest = dest * 10 + x % 10
            x = int(x /10)

        if x == dest or x == int(dest/10):
            return True

        return False