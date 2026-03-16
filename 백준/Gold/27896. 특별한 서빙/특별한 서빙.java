import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int N= Integer.parseInt(st.nextToken());
        int M= Integer.parseInt(st.nextToken());
        long complaine = 0;
        int answer=0;
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            int task=Integer.parseInt(st.nextToken());
            pq.add(task);
            complaine+=task;
            while(complaine>=M && !pq.isEmpty()){
                int temp=pq.poll();
                complaine-=(long)(temp*2);
                answer+=1;
            }
        }
        System.out.println(answer);
    }
}