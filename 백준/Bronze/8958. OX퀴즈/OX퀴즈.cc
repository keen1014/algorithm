#include <stdio.h>
#include <string.h>
int main() {
    int k;
    char S[80];
    int score = 1;
    int sum;
    scanf("%d", &k);
    for(int i=0;i<k;i++){
        scanf("%s", S);
        sum = 0;
        score=1;
            for(int j = 0;j<strlen(S);j++){
                if(S[j]=='X'){
                    score = 1;
                    continue;
                }else{
                    sum += score;
                    score += 1;
                }
            }
        printf("%d\n", sum);
    }
    return 0;
}