def sortedSquares(nums):
    l = 0
    r = len(nums) - 1
    ans = len(nums) * [0]
    i = -1
    while r >= l:
        if abs(nums[l]) > abs(nums[r]):
            ans[i] = nums[l]*nums[l]
            l += 1
        else:
            ans[i] = nums[r] * nums[r]
            r -= 1
        i -= 1
    return ans
print(sortedSquares([-5,-3,-2,-1]))