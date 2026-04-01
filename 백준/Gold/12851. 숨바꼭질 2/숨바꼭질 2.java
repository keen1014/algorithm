import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int mintime=Integer.MAX_VALUE;
        int[] visited = new int[100001];
        Queue<int[]> que = new ArrayDeque<>();
        int answer=0;
        que.offer(new int[]{N,0});
        visited[N]=1;
        while(!que.isEmpty()){
            for(int i=0;i<que.size();i++){
                int[] temp=que.poll();
                int now=temp[0];
                int cnt=temp[1];
                if(cnt>mintime){
                    continue;
                }
                if(now==M){
                    if(cnt<mintime){
                        answer=1;
                        mintime=cnt;
                    }
                    else if(cnt==mintime){
                        answer++;
                    }
                    continue;
                }
                int[] nextPos={now-1, now+1, now*2};
                for(int z:nextPos){
                    if(z<0 || z>100000){
                        continue;
                    }
                    if(visited[z]==0 || visited[z]==cnt+1){
                        visited[z] = cnt + 1;
                        que.offer(new int[]{z, cnt+1});
                    }
                    
                    
                }
                
            }
        }
        System.out.println(mintime);
        System.out.print(answer);
    }
}