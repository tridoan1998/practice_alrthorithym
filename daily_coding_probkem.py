class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tempsum, arr = 0, []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(i + 2, len(nums)):
                    tempsum = nums[i] + nums[j] + nums[k]
                    if tempsum == 0:
                        arr.append([nums[i], nums[j], nums[k]])
        return arr


"""

For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
For “BBBB” the longest substring is “B”, with length 1.
For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7



time complexity: O(N)
space complexity: O(1)
data strucute: 
technique:
variable needed: 


thought process:
edge cases: all the same char => return length 1
empty string, string with number, special character 




"""


class LinkedList:
    class Node:
        def __init__(self, data);

        self.data = data


def __init__(self):
    self.head = None


def longest_substring(head):


