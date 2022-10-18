#Solution for finding  index of two numbers summing to target with only one solution.


def twoSum(nums, target):
  for x in range(len(nums)):
    for j in range (x + 1,len(nums)):
      if (nums[j]) == target - nums[x]:
        return [x,j]

def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
        
# Better solutions to understand later

def twoSum(self, nums, target):
  h = {}
  for i, num in enumerate(nums):
      n = target - num
      if n not in h:
          h[num] = i
      else:
          return [h[n], i]


def twoSum(self, nums, target):
  dict={}
  for index, ele in enumerate(nums):
      if target- ele in dict:
          return dict[target- ele], index
      dict[ele]= index

