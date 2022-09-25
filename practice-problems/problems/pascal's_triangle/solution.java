class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();
        List<Integer> newRow = new ArrayList<>();
        List<Integer> previous_row;
        
        if (numRows <= 0){
            return triangle;
        }
        
        // base case: 
        newRow.add(1);
        triangle.add(newRow);
        
        for(int i = 1; i < numRows; i++){ 
            previous_row = triangle.get(i-1);
            newRow = new ArrayList<>();

            
            newRow.add(1);
            // Looping through the previous row, adding up the values at the pointers and iterating them:
            for(int j=1; j<i; j++){ // note: we can use 'i' here as the number of items in each row matures row's number. 
                newRow.add(previous_row.get(j-1) + previous_row.get(j));
                
            }
            
            newRow.add(1);            
            triangle.add(newRow);    
                
            }
            
        return triangle;
    }
        
}
