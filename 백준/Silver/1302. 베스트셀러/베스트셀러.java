import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Map<String, Integer> map = new HashMap<>();
        String s=br.readLine();
        int N = Integer.parseInt(s.trim());
        for(int i=0;i<N;i++){
            s=br.readLine();
            map.put(s,map.getOrDefault(s,0)+1);
        }
        
        List<String> keyList = new ArrayList<>(map.keySet());
        
        keyList.sort((o1, o2) -> {
            int v1=map.get(o1);
            int v2=map.get(o2);
            if(v1==v2){
                return o1.compareTo(o2);
            }
            return v2-v1;
        });
        
        if(!keyList.isEmpty()){
            bw.write(keyList.get(0));
        }
        bw.flush();
        bw.close();
    }
}