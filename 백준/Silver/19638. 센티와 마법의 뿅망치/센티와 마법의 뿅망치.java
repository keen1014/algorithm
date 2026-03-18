import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int answer=0;
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            pq.add(Integer.parseInt(st.nextToken()));
        }
        while(pq.peek()>=H && T!=0){
            int temp=pq.remove();
            if(temp==1){
                pq.add(temp);
                break;
            }
            pq.add(temp/2);
            T-=1;
            answer+=1;
        }
        if(pq.peek()<H){
            System.out.println("YES"+"\n"+answer);
        }
        else{
            System.out.println("NO"+"\n"+pq.peek());
        }
        
    }
}