// gcc prime-generator.c -Wall -pedantic -o prime-generator
#include <stdio.h>
#include <stdlib.h>
#define true 1u
#define false 0u

unsigned is_prime(unsigned n){
    unsigned i;
    if(n < 4)
        return n > 1;
    if(n % 2 == 0 || n % 3 == 0)
        return false;
    for(i = 5; i * i <= n; i += 6)
        if(n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int _next_prime(unsigned n){
    if(n <= 2)
        return 2;
    if(n % 2 == 0)
        n += 1;
    while(!is_prime(n))
        n += 2;
    return n;
}

unsigned next_prime(){
    static unsigned value = 1;
    unsigned prime = _next_prime(value);
    value = prime + 1;
    return prime;
}

int main(void){
    unsigned i = 0;
    for(;i < 30; i++){
        printf("%u\n", next_prime());
    }
    return EXIT_SUCCESS;
}
