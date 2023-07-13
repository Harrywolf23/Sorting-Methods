array=[10,3,5,7,6,2,1,9,8,4]

holder=0

def bubblesort(array, holder):  
    arraylength=len(array)
    for x in range(0, arraylength):
        for y in range(0, arraylength-1):
            if(array[y]>array[y+1]):
                holder=array[y+1]
                array[y+1]=array[y]
                array[y]=holder
    return array

bubblesort(array, holder)
for z in range(10):
    print(array[z])

#barely used just good to know; similar to insertion sort