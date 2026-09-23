class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num

        while low <= high:
            mid = (low+high)//2
            p_sqr = mid* mid

            if p_sqr == num:
                return True
            elif p_sqr < num:
                low = mid +1
            else :
                high = mid - 1
        return False
