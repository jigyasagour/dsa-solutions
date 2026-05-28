class Solution(object):
    def containsDuplicate(self, nums):
        arr = set()
        for i in nums:
            if i in arr:
                return True 
            arr.add(i)
        return False        ///