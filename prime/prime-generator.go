package main

import "fmt"

func IsPrime(n uint) bool {
    if n < 4 {
        return n > 1
    }
    if n % 2 == 0 || n % 3 == 0 {
        return false
    }
    for i := uint(5); i * i <= n; i += 6 {
        if n % i == 0 || n % (i + 2) == 0 {
            return false
        }
    }
    return true
}

func MakePrimeGenerator() func() uint {
    value := uint(2)
    return func() uint {
        prime := value
        if value == 2 {
            value += 1
        } else {
            for value += 2; !IsPrime(value); value += 2 {
            }
        }
        return prime
    }
}

func main(){
    primeGenerator := MakePrimeGenerator()
    for i := 0; i < 30; i++ {
        fmt.Println(primeGenerator())
    }
}
