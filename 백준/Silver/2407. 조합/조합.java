import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.BigInteger;
class Main {
    static int n, m;
    static int answer=0;
    static BigInteger[][] memo;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter (new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        memo = new BigInteger[n+1][m+1];
        // combination(0,0);
        dp(n,m);
        bw.write(memo[n][m]+"");
        bw.flush();
        bw.close();
    }
    static void combination(int start, int depth){
        if (depth==m){
            answer+=1;
            return;
        }
        for(int i=start;i<n;i++){
            combination(i+1,depth+1);
        }
    }
    static BigInteger dp(int i, int depth){
        if (depth>i) return BigInteger.ZERO;
        if (depth==0||i==depth) return BigInteger.ONE;
        if (memo[i][depth]!=null) return memo[i][depth];
        return memo[i][depth] = dp(i-1, depth-1).add(dp(i-1, depth));
    }
}