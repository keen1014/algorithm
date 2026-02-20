import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        for(int i=0;i<4;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1=Integer.parseInt(st.nextToken());
            int y1=Integer.parseInt(st.nextToken());
            int x2=Integer.parseInt(st.nextToken());
            int y2=Integer.parseInt(st.nextToken());
            int p1=Integer.parseInt(st.nextToken());
            int q1=Integer.parseInt(st.nextToken());
            int p2=Integer.parseInt(st.nextToken());
            int q2=Integer.parseInt(st.nextToken());

            int sx=0;
            int sy=0;
            for(int j=x1;j<=x2;j++){
                if(p1<=j && j<=p2){
                    sx+=1;
                }
            }
            for(int z=y1;z<=y2;z++){
                if(q1<=z && z<=q2){
                    sy+=1;
                }
            }
            if(sx==0||sy==0){
                bw.write("d\n");
            }
            else if((sx==1 || sy==1)&& (1<sx || 1<sy)){
                bw.write("b\n");
            }
            else if(sx==1 && sy==1){
                bw.write("c\n");
            }
            else if(0<sx && 0<sy){
                bw.write("a\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}