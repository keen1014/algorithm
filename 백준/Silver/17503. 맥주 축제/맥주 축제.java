import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf= new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
        String s= bf.readLine();
        StringTokenizer st = new StringTokenizer(s);
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        
        Beer[] beers = new Beer[K];
        for (int i=0;i<K;i++){
            String line = bf.readLine();
            if (line == null || line.trim().isEmpty()){
                i--;
                continue;
            }
            StringTokenizer stbeer = new StringTokenizer(line);
            if(stbeer.countTokens() <2){
                i--;
                continue;
            }
            int v= Integer.parseInt(stbeer.nextToken());
            int c= Integer.parseInt(stbeer.nextToken());
            beers[i]=new Beer(v, c);
        }
        Arrays.sort(beers);
        PriorityQueue<Integer> pq=new PriorityQueue<>();
        
        long totalPreference = 0;
        
        for(Beer beer: beers){
            pq.add(beer.preference);
            totalPreference += beer.preference;
            
            if(pq.size() > N){
                int minPref = pq.poll();
                totalPreference -= minPref;
            }
            
            if(pq.size() == N && totalPreference >=M){
                System.out.println(beer.alcohol);
                return;
            }
        }
        System.out.print("-1");
    }
}
class Beer implements Comparable<Beer>{
    int preference;
    int alcohol;
    
    public Beer(int preference, int alcohol){
        this.preference = preference;
        this.alcohol = alcohol;
    }
    
    @Override
    public int compareTo(Beer o){
        if(this.alcohol == o.alcohol){
            return o.preference - this.preference;
        }
        return this.alcohol - o.alcohol;
    }
}