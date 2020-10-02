# Given a set with distinct elements, find all of its distinct subsets
#
# Input: [1, 5, 3]
# Output: [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]    
#
#
# T.Complexity: O(N*(2^N))
# S.Complexity: O(2^N)
def find_subsets(nums):
    subsets = []
    
    subsets.append([])
    
    for current_num in nums:
        n = len(subsets)
        for i in range(n):
            sset = list(subsets[i]) # creates new list 
            sset.append(current_num)
            subsets.append(sset)
    return subsets


def main():
    print("Subsets of [1,5] : ", str(find_subsets([1,5])) )
    
    print("Subsets of [1,5, 3] : ", str(find_subsets([1,5,3])) )
    
    
main()