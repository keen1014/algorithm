import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n= Long.parseLong(br.readLine());
        int k = 1;
        while(true){
            long powerVal = (long)Math.pow(2, k+1);
            long maxWeight = k+ (k+1) * (powerVal -1);

            if (maxWeight >= n){
                System.out.print(k);
                break;
            }
            k++;
        }
    }
}