import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        Map<Integer, Integer> peoples= new HashMap<>();
        List<Integer> list = new ArrayList<>();
        for(int i=0;i<M;i++){
            st = new StringTokenizer(br.readLine());
            int h1=Integer.parseInt(st.nextToken());
            int h2=Integer.parseInt(st.nextToken());
            list.add(h1);
            list.add(h2);
            peoples.put(h1, i+1);
            peoples.put(h2, i+1);
        }
        Collections.sort(list);
        int index = (N-1)%list.size();
        System.out.println(peoples.get(list.get(index)));
    }
}