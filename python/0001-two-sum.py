class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictm={}
        for i in range(len(nums)):
            sub=target - nums[i]
            if sub in dictm:
                return [dictm[sub],i]
            dictm[nums[i]]=i
