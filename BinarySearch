class Solution:
    def search(self, nums: List[int], target: int):
        lo, hi = 0, len(nums)-1
        while lo<=hi:
            mid= (lo+hi)//2
            m= nums[mid]
            if target==m:
                return mid
            elif target>m:
                lo= mid+1
            else:
                hi= mid-1
        return -1
