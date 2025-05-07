# Sangmin Lee                                           2025-05-06
# Lab: Week 15
# Description: This code solves the "Two Sum" problem using four different functions

# CITATION: URL: https://interviewing.io/questions/two-sum
# CITATION: PUBLISHER: Dominic Platt
# CITATION: ACCESSED: 5-6-2025

def twoSumLoops(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def twoSumDict(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in num_map:
            return [num_map[needed], i]
        num_map[num] = i
    return []

def twoSumLoopsAll(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append([i, j])
    return pairs

def twoSumDictAll(nums, target):
    pairs = []
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            pairs.append([num_map[target - num], i])
        num_map[num] = i
    return pairs

def main():
    numbers = [4, 5, 1, 8, 3, 2]
    target = 6

    print("twoSumLoops result:", twoSumLoops(numbers, target))
    print("twoSumDict result:", twoSumDict(numbers, target))
    print("twoSumLoopsAll result:", twoSumLoopsAll(numbers, target))
    print("twoSumDictAll result:", twoSumDictAll(numbers, target))

if __name__ == "__main__":
    main()
