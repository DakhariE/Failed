#Solution for finding  index of two numbers summing to target with only one solution.


def twoSum(nums, target):
  compare = 0
  for x in range(len(nums)):
    compare = x
    for j in range (len(nums)):
      if x == j:
        continue
      if (nums[x] + nums[j]) == target:
        return [x,j]
        
# Better solutions to understand later
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index, ele in enumerate(nums):
            if target- ele in dict:
                return dict[target- ele], index
            dict[ele]= index