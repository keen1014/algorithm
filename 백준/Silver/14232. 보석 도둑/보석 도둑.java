import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long k= Long.parseLong(st.nextToken());
        ArrayList<Long> list = new ArrayList<>();
        
        for(long i=2;i*i<=k;i++){
            while(k%i==0){
                list.add((long)i);
                k/=i;
            }
        }
        if(k>1){
            list.add(k);
        }
        System.out.println(list.size());
        StringBuilder sb = new StringBuilder();
        for(long f:list){
            sb.append(f).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}