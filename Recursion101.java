package Sorting;
public class Recursion101{
    public static int Factorial(int x){
        if(x==0){
            return 1; //we return 1 to end the recursion so it doesn't go on forever
        } 
        else{
           return x * Factorial(x-1); 
        }
    }
    public static void main (String []args){
        int result = Factorial(5);
        System.out.println(result);
    }
}