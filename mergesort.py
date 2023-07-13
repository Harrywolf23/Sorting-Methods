list = [4, 3, 5, 7, 6, 2, 1, 9, 8, 10]

# Function to merge two sorted halves of a list
def merge(list, left, right):
    sorted = []  # Temporary list to store sorted elements
    i = left  # Starting index of the left half
    mid = (left + right) // 2  # Midpoint index to divide the list into halves
    j = mid + 1  # Starting index of the right half

    # Merge elements from both halves into sorted list
    while i < mid + 1 and j < right + 1:
        if list[i] <= list[j]:
            sorted.append(list[i])
           
            i = i + 1
        else:
            sorted.append(list[j])
            j = j + 1
    #for x in range(len(sorted)):
        #print("temporary array: ",sorted[x])
    #print()
    # Add remaining elements from the right half, if any
    while j < right + 1:
        sorted.append(list[j])
        j = j + 1

    # Add remaining elements from the left half, if any
    while i < mid + 1:
        sorted.append(list[i])
        i = i + 1

    # Copy sorted elements back to the original list
    for x in range(len(sorted)):
        list[left + x] = sorted[x]

# Function to recursively divide and merge the list
def mergesort(list, left, right):
    mid = (left + right) // 2  # Calculate the midpoint index

    # Base case: if there is only one element in the sublist
    if right==left:
        print("base case:",left)
        print()
        return
    else:
        print("start of else:", "left:",left,"right:", right)
        print()
        # Recursive calls to divide the list into two halves
        mergesort(list, left, mid)
        #stack is created, so the mergesort happens inside itself, making the left and right smaller and smaller until the basecase is reached
        mergesort(list, mid + 1, right)
        # Merge the sorted halves
        merge(list, left, right)
        print("end of the else:",left, right)
# Call mergesort function to sort the list
mergesort(list, 0, len(list) - 1)

# Print the sorted list
for x in range(len(list)):
    print(list[x])

