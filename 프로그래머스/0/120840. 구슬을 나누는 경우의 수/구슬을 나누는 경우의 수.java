class Solution {
    public int solution(int balls, int share) {
        int answer = combination(balls, share);
        
        return answer;
    }
    private int combination(int n, int r){
        if(r==0 || n==r){
            return 1;
        }
        return combination(n-1,r-1)+combination(n-1, r);
    }
}