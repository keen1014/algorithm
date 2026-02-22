import java.util.*;
class Solution {
    class Patient implements Comparable<Patient>{
    int index;
    int value;
    public Patient(int index, int value){
        this.index = index;
        this.value = value;
    }
    @Override
     public int compareTo(Patient o){
         return o.value- this.value;
     }
}
    
    public int[] solution(int[] emergency) {
    
        int[] answer = new int[emergency.length];
        List<Patient> list = new ArrayList<>();
        for(int i=0;i<emergency.length;i++)
            list.add(new Patient(i, emergency[i]));
        
        Collections.sort(list);
        
        int rank =1;
        for(Patient p: list){
            answer[p.index]=rank;
            rank++;
        }
        return answer;
    }
}