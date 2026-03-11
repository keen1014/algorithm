import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double score = 0d;
        double total = 0d;
        for(int i=0;i<20;i++){
            String input = br.readLine();
            StringTokenizer st = new StringTokenizer(input);
            st.nextToken();
            double sc = Double.parseDouble(st.nextToken());
            String  tempgrade = st.nextToken();
            if(tempgrade.equals("P")) continue;
            double grade = Getgradepoint(tempgrade);
            score+=sc;
            total+=(sc*grade);
        }
        System.out.println(total/score);
    }
    public static double Getgradepoint(String grade){
        if(grade.equals("A+")) return 4.5;
        if(grade.equals("A0")) return 4.0;
        if(grade.equals("B+")) return 3.5;
        if(grade.equals("B0")) return 3.0;
        if(grade.equals("C+")) return 2.5;
        if(grade.equals("C0")) return 2.0;
        if(grade.equals("D+")) return 1.5;
        if(grade.equals("D0")) return 1.0;
        return 0.0;
    }
}