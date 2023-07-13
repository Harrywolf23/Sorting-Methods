import random

array = [4, 3, 5, 10, 6, 2, 1, 9, 8, 7]

def partition(array, left, right):
    pivot = array[right]
    for j in range(left, right):
        if array[j] <= pivot:
            # Swap elements
            temp = array[left]  
            array[left] = array[j]
            array[j] = temp
            left += 1
            print("left pre swap:",left)
            print()
            print("swapping:", array)
            print()

    #if you move everything on the right to the left that is smaller, then the remaining elements on the right will be > then partition
    
    #this makes the final swap, moving pivot into its correct location between the elements < and the elements >
    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    print("swapping pivot w left:",array)

    return left  # Return the index of the pivot


def quicksort(array, left, right):
    if left < right:
        #gets the pivot index
        p = partition(array, left, right)
        print("new partition:", p)
        quicksort(array, left, p - 1)
        quicksort(array, p + 1, right)

# Print the original array 
print("Original array:", array)

# Sort the array using quicksort
quicksort(array, 0, len(array) - 1)

# Print the sorted array
print("Sorted array:", array)
