#include <stdio.h>
#include <string.h>

int main() {

    int i;
    int x=0;

    char st[10];
    printf("enter the string: ");
    scanf("%s",st);

    int n=strlen(st);
    

    if (n<2){
        printf("invalid string");
    }

    else if(n==2){
        if (st[0]=='b' && st[1]=='b'){
            printf("valid string");
        }
        else{
            printf("invalid string");
        }
    }

    else if (n>2){
        if (st[n-1]=='b' && st[n-2]=='b'){
            for(i=0;i<n-2;i++){
                if(st[i]=='a'){
                    x++;
                    if(x==n-2){
                        printf("valid string");
                    }
                }
                else {
                    printf("invalid string");
                    break;
                }
            }
        }
        else {
            printf("invalid string");
        }

    }


return 0;
    }



