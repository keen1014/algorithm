#include <stdio.h>
#include <string.h>
int main() {
    char S[5][15]={};
    for(int a=0;a<5;a++){
        scanf("%s", S[a]);
    }
    for(int i=0;i<15;i++){
        for(int j=0;j<5;j++){
            if(S[j][i]=='\0'){
                continue;
            }
            printf("%c", S[j][i]);
        }
    }
    return 0;
}