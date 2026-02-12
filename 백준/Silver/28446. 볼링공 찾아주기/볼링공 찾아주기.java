import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        String s = br.readLine();
        int N = Integer.parseInt(s.trim());
        Map<String, String> map = new HashMap<>();
        for(int i=0;i<N;i++){
            s=br.readLine();
            StringTokenizer st = new StringTokenizer(s);
            int a=Integer.parseInt(st.nextToken());
            if(a==1){
                String locker = st.nextToken();
                String wight = st.nextToken();
                map.put(wight,locker);
            }
            else{
                String wight = st.nextToken();
                bw.write(map.get(wight));
                bw.write('\n');
            }
        }
        bw.flush();
        bw.close();
    }
}