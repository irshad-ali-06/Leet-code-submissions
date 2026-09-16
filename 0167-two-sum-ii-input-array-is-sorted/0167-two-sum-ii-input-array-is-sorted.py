class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        sum = 0
        n = len(numbers)
        left = 0
        right = n-1

        while left < right:
            sum = numbers[left]+numbers[right]
            if sum == target:
                return [left+1, right +1]
            if sum < target:
                left+=1
            else:
                right-=1

            

