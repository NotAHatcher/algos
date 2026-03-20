def findMaxAverage(nums,k):
    l = 0
    r = k-1
    s = sum(nums[0:r+1])
    print(s)
    max_s = s
    while r < len(nums) - 1:
        r += 1
        s -= nums[l]
        l += 1
        s += nums[r]
        print(s)
        max_s = max(s,max_s)
    return max_s / k
print(findMaxAverage([1,12,-5,-6,50,3],4))