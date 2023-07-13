array=[4,3,5,7,6,2,1,9,8,10]

holder=0

def selectionsort(array, holder):
    smallest=0
    arraylength=len(array)
    for y in range(0, arraylength):
        for x in range(y, arraylength):
            if(array[x]<array[smallest]):
                smallest=x
        holder=array[y]
        array[y]=array[smallest]
        array[smallest]=holder
        smallest=y+1    
    return array

selectionsort(array, holder)
for z in range(10):
    print(array[z])
