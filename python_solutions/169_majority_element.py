class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = {}

        for x in nums:
            if x not in numDict:
                numDict[x] = 1
            else:
                numDict[x] += 1
        
        for key, value in numDict.items():
            if value > len(nums) / 2:
                return key

        return 0
        