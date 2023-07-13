package Sorting;
import java.util.Random;
public class Quicksort {
    /**
     * Quicksort algorithm:
     * - Selects a pivot element from the array.
     * - Partitions the array into two subarrays: elements smaller than the pivot and elements greater than the pivot.
     * - Recursively applies the Quicksort algorithm to the subarrays.
     * - Combines the sorted subarrays to obtain the final sorted array.
     */
    public static void quickSort(int[] array, int low, int high ){
        if(low<high){
            int pivot=partition(array, low, high);
            quickSort(array, low, pivot-1); //sorts the left side of the pivot of the array
            quickSort(array, pivot+1, high); //sorts the right side of the pivot of the array
        }
    }
    public static int partition(int [] array, int low, int high){
        int pivot = array[high]; //taking the pivot element, can be subsituted for a random number
        int i = low-1;  //index of smaller elements
        int z = low;    //index that goes through the smaller array
        while(z<high){
            //swaps the smaller element w an element left of the pivot
            if(array[z]<pivot){
            int temp=array[i+1];
            array[i+1]=array[z];
            array[z]=temp;
            i++;
            }   
            z++;
        }
        //swaps pivot with last element sorted to make sure it is in correct place
        int temp = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp;
        return i; //returns index of pivot
        
    }
    public static void main(String[]args){
        int[]tester={6,3,1,4,9,10,7,8,5,2};
        quickSort(tester, 0, tester.length-1);
        for(int i = 0; i<tester.length; i++){
            System.out.println(tester[i]);
        }
    }
}
