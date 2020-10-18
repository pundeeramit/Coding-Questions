# First and Last Position of X in Sorted Array
#
# Input: arr=[2,3,6,7,7,8,8,8,12]
# Output: [5, 7]    
#
#
def first_pos(arr, val):
    low, high = 0, len(arr)-1
    f_pos = len(arr)
    
    while(low <= high):
        mid = low + int((high-low)/2)
        
        if arr[mid] >= val:
            f_pos = mid
            high = mid-1
        else:
            low = mid+1
        
    return f_pos
    


def main():
    arr=[2,3,6,7,7,8,8,8,12]
    print(arr)
    
    val = 8
    #Search val 8
    print("Search 8")
    f_pos = first_pos(arr, val)
    e_pos = first_pos(arr, val+1) - 1
    
    if f_pos <= e_pos:
        print((f_pos,e_pos))
    else:
        print((-1,-1))
    
    #Search val 12  
    print("Search 12")
    
    f_pos = first_pos(arr, 12)
    e_pos = first_pos(arr, 12+1) - 1


    if f_pos <= e_pos:
        print((f_pos,e_pos))
    else:
        print((-1,-1))
    
    #Search val 15
    print("Search 15")
    
    f_pos = first_pos(arr, 15)
    e_pos = first_pos(arr, 15+1) - 1


    if f_pos <= e_pos:
        print((f_pos,e_pos))
    else:
        print((-1,-1))
    

main()