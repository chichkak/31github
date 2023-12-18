nums = [2,3,1,2,4,3]
target = 7
left = 0
total = 0
res = float('inf')
for i in range(len(nums)):
    total += nums[i]
    while total >= target:
        res = min (i - left + 1, res)
        total -= nums[left]
        left += 1

print (0 if res == float('inf') else res)