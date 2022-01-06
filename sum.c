#include <stdio.h>

int add(int limit ){
    if(limit){
        return (limit+add(limit-1));
    }
    else{
        return 0;
    }

}
void main(){
    int result = add(5);
    printf("%d",result);
    
}