class Solution:
    def isAlphanumeric(self,c):
        c = ord(c)
        if(97<=c<=122 or 65<=c<=90 or 48<=c<=57):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1
        s = s.lower()

        while i< j:

            if not self.isAlphanumeric(s[i]):
                i+=1
            elif not self.isAlphanumeric(s[j]):
                j-=1
            elif s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
