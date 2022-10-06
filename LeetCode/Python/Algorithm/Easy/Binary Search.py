class Solution(object):
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        
		# search for target position
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return -1