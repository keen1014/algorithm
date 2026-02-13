import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int L = Integer.parseInt(st.nextToken());
        int[] li = new int[L];
        String s=br.readLine();
        int n =Integer.parseInt(br.readLine());
        int answer = 0;
        li=Arrays.stream(s.split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(li);
        int left =0;
        int right =0;
        if(n<li[0]){
            left=0;
            right=li[0];
        }
        else{
            for(int i=0;i<li.length-1;i++){
                if (li[i]<n&&n<li[i+1]){
                    left=li[i];
                    right=li[i+1];
                    break;
                }
            }
        }
        if (right!=0){
            int r=n-left;
            int c=right-n;
            answer=r*c-1;
        }
        
        
        bw.write(answer+"");
        bw.flush();
        bw.close();
        br.close();
    }
}