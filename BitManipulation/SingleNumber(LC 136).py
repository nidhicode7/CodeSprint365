#Find Unique Element in an Array
#Problem: Given an array where every element appears twice except for one, find the element that appears only once.
#Concept: XOR operation

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in range (0,len(nums)):
            res^=nums[i]
        return res
        
