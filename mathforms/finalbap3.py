nums = [1, 2, 4, 7, 9]
target = 2
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