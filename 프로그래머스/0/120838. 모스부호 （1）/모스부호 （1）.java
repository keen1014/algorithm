import java.util.Map;
import static java.util.Map.entry;
class Solution {
    public String solution(String letter) {
        Map<String, String> map = Map.ofEntries(entry(".-","a"), entry("-...","b"), entry("-.-.","c"), entry("-..","d"), entry(".","e"), entry("..-.","f"), entry("--.","g"), entry("....","h"), entry("..","i"),entry(".---","j"), entry("-.-","k"), entry(".-..","l"), entry("--","m"), entry("-.","n"), entry("---","o"), entry(".--.","p"), entry("--.-","q"), entry(".-.","r"), entry("...","s"), entry("-","t"), entry("..-","u"), entry("...-","v"), entry(".--","w"),entry("-..-","x"), entry("-.--","y"), entry("--..","z"));
        String answer = "";
        String[] arr=letter.split(" ");
        StringBuilder sb = new StringBuilder();
        for(String temp:arr){
            sb.append(map.get(temp));
        }
        answer=sb.toString();
        return answer;
    }
}