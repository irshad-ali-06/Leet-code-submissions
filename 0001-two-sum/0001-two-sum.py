class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict1 = {}

        for i in range(len(nums)):
            find = target - nums[i]
            if find not in dict1:
                dict1[nums[i]] = i
            else:
                return [dict1[find],i] 
