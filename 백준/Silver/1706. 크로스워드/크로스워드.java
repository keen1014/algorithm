import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R= Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        char[][] board = new char[R][C];
        for(int i=0;i<R;i++){
            board[i]=br.readLine().toCharArray();
        }
        List<String> list = new ArrayList<String>();
        for(int i=0;i<R;i++){
            String temp=String.valueOf(board[i]);
            String[] strs=temp.split("#");
            for(String s:strs){
                if(2>s.length()){
                    continue;
                }
                else{
                    list.add(s);
                }
            }
        }

        
        for(int i=0;i<C;i++){
            StringBuilder sb = new StringBuilder();
            for(int j=0;j<R;j++){
                sb.append(board[j][i]);
            }
            String temp=String.valueOf(sb);
            String[] strs=temp.split("#");
            for(String s:strs){
                if(2>s.length()){
                    continue;
                }
                else{
                    list.add(s);
                }
            }
        }
        Collections.sort(list);
        System.out.print(list.get(0));
    }
}