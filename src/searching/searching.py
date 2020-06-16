# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, floor, ceiling):
    # Your code here
    if floor >= ceiling:
        return -1

    midpoint = (ceiling - floor) // 2 + floor
    if target == arr[midpoint]:
        return midpoint
    elif target < arr[midpoint]:
        return binary_search(arr, target, floor, midpoint + 1)
    elif target > arr[midpoint]:
        return binary_search(arr, target, midpoint - 1, ceiling)
    



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    
    #Get our start and end in place. Because this isn't supplied in the arguments, i don't think we can go recursive.
    start = 0
    end = len(arr) - 1
    
    #find out of the array is ascending or descending
    if arr[start] < arr[end]:
        ascending = True
        print("array is ascending")
    else:
        ascending = False

    #Loop until we find the target
    while start <= end:
        #Set the midpoint
        midpoint = (end - start) // 2 + start
        #If we found the target, return
        if target == arr[midpoint]:
            return midpoint
        #else let's move the midpoint
        elif target < arr[midpoint]:
            #check if it's ascending or descending, because that will change which variable we move
            if ascending:
                end = midpoint -1
            else:
                start = midpoint + 1
        elif target > arr[midpoint]:
            if ascending:
                start = midpoint + 1
            else:
                end = midpoint - 1
    return -1