import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] board= new int[M][N];
        boolean[][] visited = new boolean[M][N];
        visited[0][0]=true;
        for(int i=0;i<M;i++){
            char[] line = br.readLine().toCharArray();
            for(int j=0;j<N;j++){
                board[i][j]=line[j]-'0';
            }
        }
        int[] dx={1, 0, -1, 0};
        int[] dy={0, 1, 0, -1};
        Deque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{0,0,0});
        while(!dq.isEmpty()){
            int[] temp=dq.pollFirst();
            int r = temp[0];
            int c = temp[1];
            int block=temp[2];
            
            if(r==M-1 && c==N-1){
                System.out.println(block);
                break;
            }
            for(int z=0;z<4;z++){
                int y= r+dy[z];
                int x= c+dx[z];
                
                if(y>=M || y<0 || x>=N || x<0 || visited[y][x]==true){
                    continue;
                }
                
                if(board[y][x]==1){
                    dq.offer(new int[]{y,x,block+1});
                }
                else{
                    dq.offerFirst(new int[]{y,x,block});
                }
                visited[y][x]=true;
            }
        }
        
    }
}