class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        left = 0
        right = n-1
        pos = n-1

        while left <= right:
            left_val = nums[left]**2
            right_val = nums[right]**2
            if left_val  > right_val:
                res[pos] = left_val
                left+=1
            else:
                res[pos] = right_val
                right-=1
            pos-=1
        return res


