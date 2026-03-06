import java.util.*;
class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] dice = {a, b, c, d};
        Map<Integer, Integer> counts = new HashMap<>();
        for(int i: dice){
            counts.put(i,counts.getOrDefault(i,0)+1);
        }
        if(counts.size()==1){
            return a*1111;
        }
        else if(counts.size()==2){
            int p=0;
            int q=0;
            int p2=0;
            int q2=0;
            for(int key:counts.keySet()){
                if(counts.get(key) == 3){
                    p=key;
                }
                else if(counts.get(key) == 1){
                    q=key;
                }
                if(counts.get(key) == 2){
                    if (p2==0) p2=key;
                    else q2=key;
                }
            }
            if (p!=0){
                return (int)Math.pow((10*p+q), 2);
            }
            return (p2+q2)*Math.abs(p2-q2);
        }
        else if(counts.size()==3){
            int p=0;
            int q=0;
            int r=0;
            for(int i:counts.keySet()){
                if(counts.get(i)==2){
                    p=i;
                }
                else{
                    if(q==0) q=i;
                    else r=i;
                }
            }
            return q*r;
        }
        else{
            return Collections.min(counts.keySet());
        }
    }
}