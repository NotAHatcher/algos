def twoSum(nums,target):
    s = set(nums)
    for i in range(len(nums)):
        if (target - nums[i]) in s:
            if i != nums.index(target - nums[i]):
                return [i, nums.index(target - nums[i])]

