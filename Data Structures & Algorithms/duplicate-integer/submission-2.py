class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst={}
        for num in nums:
            lst[num]=lst.get(num,0)+1
            if lst[num]>1:
                return True

        return False
