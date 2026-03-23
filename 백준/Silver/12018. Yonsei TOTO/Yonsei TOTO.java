import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        ArrayList<Integer> list =new ArrayList<>();
        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            int person= Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
            for(int j=0;j<person;j++){
                pq.add(Integer.parseInt(st.nextToken()));
            }
            if(pq.size()<L){
                list.add(1);
            }
            else{
                for(int z=0;z<L-1;z++){
                    pq.remove();
                }
                list.add(pq.poll());
            }
        }
        Collections.sort(list);
        int answer=0;
        int total=0;
        for(int tmp:list){
            if(m>=total+tmp){
                total+=tmp;
                answer+=1;
            }
        }
        System.out.print(answer);

        
    }
}