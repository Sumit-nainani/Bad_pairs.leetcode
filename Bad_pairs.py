# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
# Return the total number of bad pairs in nums


# approach:
#     so problem is like j-nums[j] != i-nums[i]
#     so we will store j-nums[j] for each index in a dictionary
#     for one value of j-nums[j] there will be n*(n-1)/2 pairs where n is count of this value 
#     so we calculate all the pair where j-nums[j] == i-nums[i]
#     the answer would be total pairs - equal pairs

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ct=0
        n=len(nums)
        a=n*(n-1)//2
        dict={}
        for i in range(n):
            if dict.get(i-nums[i])==None:
                dict[i-nums[i]]=1
            else:
                dict[i-nums[i]]+=1
        
        for value in dict.values():
            x=int(value*(value-1)//2)
            ct += x

        return a-ct
