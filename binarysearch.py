def binarySearch(arr, start, end, target):
    if(end < start):
        return "the list is not sorted"
   
    mid = round((end - start)/2 + start)
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, start, mid - 1, target)
    elif arr[mid] < target:
        return binarySearch(arr, mid + 1, end, target)

sampleArray = [2, 5, 6, 8, 12, 33, 52]

print(binarySearch(sampleArray, 0, len(sampleArray), 9))