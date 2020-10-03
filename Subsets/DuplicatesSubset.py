# Given a set of numbers that might contain duplicates, find all of its distinct subsets
#
# Input: [1, 3, 3]
# Output: [[], [1], [3], [1,3], [3,3], [1,3,3]]    
#
#
# T.Complexity: O(N * (2^N))
# S.Complexity: O(2^N)
def find_subsets(nums):
    list.sort(nums)
    subsets = []
    
    startIndex, endIndex = 0, 0
    subsets.append([])
    for i in range(len(nums)):
        startIndex = 0
        
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex+1
        endIndex = len(subsets)-1
        
        for j in range(startIndex, endIndex + 1):
            subset = list(subsets[j])
            subset.append(nums[i])
            subsets.append(subset)
    return subsets
    
 
def main():
    print("Here is the list of subsets [1,3,3] : " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets [1,5,3,3] : " + str(find_subsets([1, 5, 3, 3])))

main()