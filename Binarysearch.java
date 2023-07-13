package Sorting;
public class Binarysearch {
    /**
     * Binary Search algorithm:
     * - Searches for a target element in a sorted array by repeatedly dividing the search space in half.
     * - Compares the target element with the middle element of the array and adjusts the search space accordingly.
     * - Continues dividing the search space until the target element is found or the search space is empty.
     * - Returns the index of the target element if found, or -1 if not found.
     */
    public static int searcher(int[] array, int target, int low, int high){
        int mid = Math.round((low+high)/2); //getting middle of array
         // Base case: target element found at index mid
        if (array[mid] == target) {
            return mid;
        }
        if(array[mid]>target){ //target element is smaller then the mid, so check the left half of the array
            return searcher(array, target, low, mid-1);
        }
        if(array[mid]<target){ //target element is bigger then the mid, so check the right half of the array
            return searcher(array, target, mid+1, high);
        }
        return target; // target found
        }
    public static void main(String[]args){
        int[] array = {1, 3, 7, 10, 14, 15, 24, 30, 65, 96};
        System.out.println(searcher(array, 15, 0, array.length-1));
        
    }
}
