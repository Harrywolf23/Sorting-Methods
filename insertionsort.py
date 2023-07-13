array=[4,3,5,7,6,2,1,9,8,10]

holder=0

def insertionsort(array, holder):
    arraylength=len(array)
    for x in range(1, arraylength):
        while(array[x-1]>array[x]):
            holder =array[x-1]
            array[x-1]=array[x]
            array[x]=holder
            if(x>1):
                x=x-1
    return array
insertionsort(array, holder)
for y in range(10):
    print(array[y])

#insertionsort for mostly sorted lists is faster than quick sort, either than that, quick sort is better