/** Squares of a Sorted Array
*Given an integer array nums sorted in non-decreasing order, 
*return an array of the squares of each number sorted in non-decreasing order.
*/
public class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] temp = new int[nums.length];
        int tmp_ = 0;

        // Squaring all elements, storing in temp list:
        for(int x = 0; x <= nums.length -1; x++) {
            temp[x] = nums[x] * nums[x];
        }

        // Sorting:
        quickSort(temp, 0, temp.length -1);
        return temp;
    }
    
    public int[] quickSort(int[] array, int start, int end){
        
        if (start < end ){
         
            int pivot = pivot(array,start,end);
            quickSort(array,start,pivot -1);
            quickSort(array,pivot + 1, end);
            
        }
        
        return array;
    }
    
    private int pivot(int[] array, int start, int end){
        int pivot = array[end];
        
        int i = start -1; // index of smaller element.
        int j;
        
        for(j = start; j <= end -1; j++) {
            
            // if the cur element is smaller then the pivot then we can swap
            if (array[j] < pivot){
                i++;    
                int tmp_ = array[j];
                array[j] = array[i];
                array[i] = tmp_;
            } // if element is greater or equal, we ignore it.
            
        }
        /*
        now our pivot is almost in the right spot, we just have to iterate i, 
        swap with j then BOOM our pivot is not in a sorted spot
        */
        i++;
        int tmp_ = array[j];
        array[j] = array[i];
        array[i] = tmp_;
        return i;

    }
    
}