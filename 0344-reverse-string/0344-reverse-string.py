class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i =0
        j = len(s)-1

        while i< j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
        #while i<j    
            #for i in range(n):
                #for j in range():
                    #swap