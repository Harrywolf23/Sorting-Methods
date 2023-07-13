import random

array = [4, 3, 5, 7, 6, 2, 1, 9, 8, 10]

def partition(array, left, right, p):
    pivot = array[p]
    array[p] = array[left]
    array[left] = pivot
    p = left
    left += 1

    while right != left:
        # Move left pointer until an element greater than pivot is found
        while array[left] <= pivot and right != left:
            left += 1

        # Move right pointer until an element less than or equal to pivot is found
        while array[right] > pivot and right != left:
            right -= 1

        # Swap the elements at left and right pointers
        holder = array[left]
        array[left] = array[right]
        array[right] = holder

    if array[left] > pivot:
        # Swap pivot with the element at the left pointer - 1 position
        holder = array[left - 1]
        array[left - 1] = pivot
        array[p] = holder
        return left - 1
    else:
        # Swap pivot with the element at the left pointer position
        holder = array[left]
        array[left] = pivot
        array[p] = holder
        return left

def quicksort(array, left, right):
    if right - left == 1:
        # Base case: If there are only two elements, swap them if necessary
        if array[left] > array[right]:
            holder = array[right]
            array[right] = array[left]
            array[left] = holder
        return

    elif right - left < 1:
        # Base case: If there are no elements or only one element, return
        return

    else:
        # Choose a random pivot index between left and right
        p = random.randrange(left, right)
        # Partition the array and get the updated pivot index
        p = partition(array, left, right, p)

        # Recursively sort the subarrays before and after the pivot
        quicksort(array, left, p - 1)
        quicksort(array, p + 1, right)

# Print the original array
print("Original array:", array)

# Sort the array using quicksort
quicksort(array, 0, len(array) - 1)

# Print the sorted array
print("Sorted array:", array)
