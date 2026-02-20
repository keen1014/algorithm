import java.util.*;
import java.lang.*;
import java.io.*;
class Point implements Comparable<Point>{
    int value;
    int index;

    public Point(int value, int index){
        this.value=value;
        this.index=index;
    }
    @Override
    public int compareTo(Point o){
        return this.value - o.value;
    }
}
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
        int N=Integer.parseInt(br.readLine());
        Point[] A = new Point[N];
        for(int i=0;i<N;i++){
            A[i]=new Point(Integer.parseInt(br.readLine()), i);
        }
        Arrays.sort(A);
        int max=0;
        for (int i=0;i<N;i++){
            if (max<A[i].index-i){
                max=A[i].index-i;
            }
        }
        bw.write(max+1+"");
        bw.flush();
        bw.close();
    }
}