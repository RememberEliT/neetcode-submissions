class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = []
        for num in nums:
            if not num in already_seen:
                already_seen.append(num)
            else:
                return True
        return False