class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        while x < len(nums) - 1:
            if nums[x] == nums[x + 1]:
                del nums[x]
                continue
            x += 1
        return len(nums)
        