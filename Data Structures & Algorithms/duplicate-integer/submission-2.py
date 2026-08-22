class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
            could create a set to contain unique items

            then iterate through and if already exists return false otherwise true
        '''
        new_set = set([])
        for num in nums:
            if num in new_set:
                return True
            else:
                new_set.add(num)
        return False