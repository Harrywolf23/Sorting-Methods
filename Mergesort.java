package Sorting;
public class Mergesort {
    /**
     * Merge Sort algorithm:
     * - Divides the array into two halves until each subarray contains one element (or empty).
     * - Recursively merges the sorted subarrays to produce larger sorted subarrays until the entire array is sorted.
     */
    public static void mergeSort(int[]array){
        if(array.length<=1){
            return;
        }
        int length = array.length;
        int mid = length/2;

        //creation of the temporary arrays
        int [] left=new int[mid];
        int [] right = new int[length-mid];
        for(int i = 0; i<mid; i++){
            left[i]=array[i];
        }
        for(int e = mid; e<length; e++){
            right[e-mid]=array[e];
        }
        mergeSort(left); //doing mergeSort on the left
        mergeSort(right); //doing mergeSort on the right
        merge(array, left, right);
    }
    private static void merge(int [] array, int[]left, int[]right){
        int leftlength=left.length;
        int rightlength=right.length;
        //we need 3 index because the array lengths will change, so we need to look at different parts of the arrays 
        int xleft=0;
        int xright=0;
        int x=0;
        while(xleft<leftlength && xright<rightlength){
            if(left[xleft]>right[xright]){
                array[x]=right[xright];
                x+=1;
                xright+=1;
            }
            else{
            array[x]=left[xleft];
            x+=1;
            xleft+=1;   
            }
        }
        //after one of the two split arrays are fully added into the big array, these while loops make sure the remaining array is fully added into it, *note* the remaining array is already sorted
        while(xleft<leftlength){
            array[x]=left[xleft];
            x+=1;
            xleft+=1;
        }
        while(xright<rightlength){
            array[x]=right[xright];
            x+=1;
            xright+=1;
        }
    }
    public static void main(String[]args){
        int[]Array={4,3,9,8,5,10,2,7};
        mergeSort(Array);
        for(int x = 0; x<Array.length; x++){
            System.out.println(Array[x]);
        }
    }
}
