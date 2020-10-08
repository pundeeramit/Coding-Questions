def getSecondLargest(arr):
    
    if type(arr) != list or len(arr) < 2:
        return -1
    
    largest, secondLargest = str(-(10**1024)), str(-(10*1024))
    
    for num in arr:
        if int(num) > int(largest):
            secondLargest = largest
            largest = int(num)
        elif int(num) < int(largest) and int(num) > int(secondLargest):
            secondLargest = num
    
    return -1 if secondLargest == str(-(10**1024)) else secondLargest
    
print(getSecondLargest(["3","-2"]))
print(getSecondLargest(["5","5","4","2"]))
print(getSecondLargest(["4","4","4"]))
print(getSecondLargest([]))
print(getSecondLargest(["-214748364801","-214748364802"]))
print(getSecondLargest('1234'))

