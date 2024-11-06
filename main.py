nums = [1,3,5,4,7]

max_length = 1
current_length = 1

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 1

print(max_length)

