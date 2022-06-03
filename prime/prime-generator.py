import itertools

def is_prime(n):
    if 1 < n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_generator():
    yield 2
    oddGenerator = itertools.count(3, 2)
    while True:
        odd = next(oddGenerator)
        if is_prime(odd):
            yield odd

if __name__ == '__main__':
    prime_generator = get_prime_generator()
    for _ in range(30):
        print(next(prime_generator))
