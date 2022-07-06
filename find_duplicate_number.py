# Given an array of integers nums containing n + 1 integers
# where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums
# and uses only constant extra space.
#
# Input: nums = [1,3,4,2,2]
# Output: 2


def findDuplicate(nums):
    slow, fast = 0, 0

    # finding the first position the pointers intersect in
    while True:
        # incrementing 2 pointers
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # putting another slow pointer at the beginning of the array
    slow2 = 0

    # intersecting the 2 slow pointers until they intersect
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            break
    return slow