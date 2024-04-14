# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li0, ri2 = 0, len(nums)-1
        for i in range(len(nums)):
            print(nums, i, nums[i], li0, ri2)

            while nums[i] in (0, 2):
                if nums[i] == 0:
                    if i < li0:
                        break
                    while (i > li0) and (nums[li0] == 0):
                        li0 += 1
                    if i == li0:
                        li0 += 1
                        break
                    else:
                        nums[i], nums[li0] = nums[li0], nums[i]
                        li0 += 1
                if nums[i] == 2:
                    if i > ri2:
                        break
                    while (i < ri2) and (nums[ri2] == 2):
                        ri2 -= 1
                    if i == ri2:
                        ri2 -= 1
                        break
                    else:
                        nums[i], nums[ri2] = nums[ri2], nums[i]
                        ri2 -= 1


# Solution 2
# Dutch national flag algorithm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # The idea behind the algorithm is to keep all the 0s before the zero pointer,
        # all the 2s after the two pointer,
        # and all the 1s between the zero and two pointers.
        zero, one, two = 0, 0, len(nums)-1
        while one <= two:
            if nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            elif nums[one] == 2:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1
            else:
                one += 1
        
