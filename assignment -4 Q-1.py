def permuteUnique(nums):
    def backtrack(start):
        if start == n:
            res.append(nums[:])
        visited = set()
        for i in range(start, n):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start+1)
            nums[start], nums[i] = nums[i], nums[start]
    
    n = len(nums)
    res = []
    backtrack(0)
    return res
nums = [1,1,2]
print(permuteUnique(nums))
