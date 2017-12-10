#include <stdio.h>

int main(){
        unsigned int random;
        random = rand();
        printf("%d",random ^0xdeadbeef);
}
