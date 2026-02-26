import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static int answer=Integer.MAX_VALUE;
    static int[] dx={0, 1, 0, -1};
    static int[] dy={-1, 0, 1, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input=br.readLine();
        int N= Integer.parseInt(input);
        int[][] board=new int[N][N];
        boolean[][] vis=new boolean[N][N];
        
        List<List<Integer>> list= new ArrayList<>();
        
        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=1;i<N-1;i++){
            for(int j=1;j<N-1;j++){
                int temp=board[i][j];
                for(int z =0;z<4;z++){
                    int x=j+dx[z];
                    int y=i+dy[z];
                    temp+=board[y][x];
                }
                list.add(new ArrayList<>(Arrays.asList(temp, i, j)));
            }
        }
        list.sort((a,b) -> a.get(0)-b.get(0));
        backtracking(0, 0, 0, N, vis, list);
        System.out.print(answer);
    }


    
    static void backtracking(int idx, int count, int sum, int N, boolean[][] vis, List<List<Integer>> list){
        if(count==3){
            answer = Math.min(answer, sum);
            return;
        }

        for(int i = idx; i<list.size();i++){
            List<Integer> flower = list.get(i);
            int cost = flower.get(0);
            int r = flower.get(1);
            int c = flower.get(2);

            if(check(r, c, vis, N)){
                toggle(r, c, vis, true);

                backtracking(i + 1, count + 1, sum + cost, N, vis, list);

                toggle(r, c, vis, false);
            }
        }
    }
    public static boolean check(int r, int c, boolean[][] vis, int N){
        if(vis[r][c]) return false;

        for(int i =0;i<4;i++){
            int ny= r+dy[i];
            int nx = c + dx[i];

            if(ny<0||nx <0|| ny >=N || nx>= N ||  vis[ny][nx]){
                return false;
            }
        }
        return true;
    }



    public static void toggle(int r, int c, boolean[][] vis, boolean value){
        vis[r][c] = value;

        for(int i=0;i<4;i++){
            int ny = r + dy[i];
            int nx = c + dx[i];
            vis[ny][nx] = value;
        }
    }
}