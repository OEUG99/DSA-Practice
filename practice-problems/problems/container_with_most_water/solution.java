class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int start = 0;
        int end = height.length -1;
        
        int b, h, currentArea;
        
        while (start < end){
            
            b = end - start;
            // determing lowest height w/ ternary operator;     
            h = (height[start] > height[end] ? height[end] : height[start]);

            
            currentArea = calculateArea(b,h);
            
            if (currentArea > maxArea){
                maxArea = currentArea;
            }
            
            if(height[start] > height[end]){
                end--;
            } else {
                start++;
            }
        }
        return maxArea; 
    }
    
    public int calculateArea(int b, int h){
        return b*h;
    }
    
}