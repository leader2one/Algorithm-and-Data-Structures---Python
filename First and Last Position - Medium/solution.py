class Solution:
    def getfirst(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid]==target:
                if mid == 0 or nums[mid-1]!= target and mid-1>=0:
                    return mid
                right = mid-1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1
    
    def getlast(self,nums,target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid]==target:
                if mid == len(nums)-1 and mid+1 <= len(nums) or nums[mid+1]!= target:
                    return mid
                left = mid+1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.getfirst(nums,target)
        r = self.getlast(nums,target)
        return [l,r]