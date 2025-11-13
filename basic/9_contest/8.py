def solve(nums: list) -> str:
    if not nums:
        return '0'

    max_val = max(nums)
    candidates = []

    first_max_index = nums.index(max_val)

    for i in range(first_max_index + 1, len(nums) - 1):
        if nums[i] % 10 == 5 and nums[i] > nums[i + 1]:
            candidates.append(nums[i])

    if not candidates:
        return '0'

    best_candidate = max(candidates)

    position = 1
    for num in nums:
        if num > best_candidate:
            position += 1

    return str(position)

input()
numbers = list(map(int, input().split()))
print(solve(numbers))
