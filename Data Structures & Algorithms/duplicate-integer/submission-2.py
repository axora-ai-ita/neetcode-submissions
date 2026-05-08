class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict();
        for n in nums:
            if n in d:
                return True
            elif n not in d:
                d[n] = 1
        return False