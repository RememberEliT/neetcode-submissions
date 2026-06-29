class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen = {}
        for index,num in enumerate(nums):
            num_needed = target - num
            if num_needed in already_seen:
                return [already_seen[num_needed], index]

            already_seen[num] = index
            
            