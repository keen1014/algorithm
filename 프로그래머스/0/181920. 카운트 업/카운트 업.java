import java.util.Arrays;
class Solution {
    public int[] solution(int start_num, int end_num) {
        StringBuilder sb=new StringBuilder();
        for (;start_num<=end_num;start_num++){
            sb.append(start_num).append(" ");
        }
        int[] answer=Arrays.stream(sb.toString().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        return answer;
    }
}