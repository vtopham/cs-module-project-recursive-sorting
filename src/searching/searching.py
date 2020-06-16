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
        return binary_search(arr, target, midpoint, ceiling - 1)
    



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
