class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dict1 = {}

        for i in range(len(numbers)):
            find = target - numbers[i]
            if find not in dict1:
                dict1[numbers[i]] = i
            else:
                return [dict1[find] + 1,i +1] 


            

