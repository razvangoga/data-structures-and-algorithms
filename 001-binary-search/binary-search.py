# usage info 
#       if we already know that the array in which we are going to search is already ordered by the search key, 
#       using binary search yealds the result faster than using a linear iterative approach
#       Complecity is O(n) for linear vs O(logn) for binary

import banks

search_for = 'idea bank'

def print_result(found_index, operation_count):
    print ("Found element at index %d after %d checks for %d items" % (found_index, operation_count, len(banks.sample_data)))

def iterative_search(arr, x):
    for i in range(len(arr)):
        if arr[i][0] == x:
            print (arr[i])
            print_result(i, i+1)

binary_operations_count = 0              
def binary_search_recursive (arr, l, r, x):
 
    global binary_operations_count
    binary_operations_count += 1
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid][0] == x:
            return mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid][0] > x:
            return binary_search_recursive(arr, l, mid-1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, mid+1, r, x)
 
    else:
        # Element is not present in the array
        return -1

def binary_search_iterative(arr, l, r, x):
 
    while l<=r:
 
        mid = l + (r - l)//2;
         
        # Check if x is present at mid
        if arr[mid][0] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid][0] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
     
    # If we reach here, then the element was not present
    return -1


print('Iterative search')      
iterative_search(banks.sample_data, search_for)

print('Binary search - recursive')
found_index = binary_search_recursive(banks.sample_data, 0, len(banks.sample_data)-1, search_for)
print(banks.sample_data[found_index])
print_result(found_index, binary_operations_count)

print('Binary search - iterative')
found_index = binary_search_iterative(banks.sample_data, 0, len(banks.sample_data)-1, search_for)
print(banks.sample_data[found_index])
print_result(found_index, binary_operations_count)