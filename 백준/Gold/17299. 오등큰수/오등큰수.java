import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Map<Integer, Integer> map = new HashMap<>();
        
        int N=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for(int i=0;i<N;i++){
            int temp=Integer.parseInt(st.nextToken());
            arr[i]=temp;
            map.put(temp, map.getOrDefault(temp,0) +1);
        }
        
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[N];

        for(int i=N-1;i>=0;i--){
            int nowNum = arr[i];
            int freq = map.get(arr[i]);

            while(!stack.isEmpty()&&map.get(stack.peek())<=freq){
                stack.pop();
            }
            if(stack.isEmpty()){
                ans[i]=-1;
            }
            else{
                ans[i]=stack.peek();
            }
            stack.push(nowNum);
        }

        StringBuilder sb = new StringBuilder();
        for(int i:ans){
            sb.append(i).append(" ");
        }
        System.out.print(sb);
    }
}