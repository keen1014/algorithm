import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        List<Integer> li = new ArrayList<>();
        int i=0;
        while(true){
            if(i>=arr.length){
                break;
            }
            if(li.size()==0){
                li.add(arr[i]);
                i++;
            }
            else if(li.get(li.size()-1)<arr[i]){
                li.add(arr[i]);
                i++;
            }
            else{
                li.remove(li.size()-1);
            }
        }
        
        return li.stream().mapToInt(Integer::intValue).toArray();
    }
}