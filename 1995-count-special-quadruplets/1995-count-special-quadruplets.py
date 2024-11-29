class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for t in range(k+1,len(nums)):
                        if (nums[i]+nums[j]+nums[k])==nums[t]:
                            count += 1
        return count