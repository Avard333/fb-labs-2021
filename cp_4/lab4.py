import random


def fast_pow(x, pow_num, mod):
    e = bin(pow_num)[2:]
    y = 1
    for i in e:
        y = (pow(y, 2)) % mod
        if int(i) == 1:
            y = (x * y) % mod
    return y


def miller_rabin(n, k=40):
    for i in range(k):
        a = random.randrange(2, n - 1)
        exp = n - 1
        while not exp & 1:
            exp >>= 1

        if fast_pow(a, exp, n) == 1:
            return True

        while exp < n - 1:
            if fast_pow(a, exp, n) == n - 1:
                return True

            exp <<= 1

        return False

    return True


def gen_prime(bits):
    while True:
        a = (random.randrange(2**(bits-1), 2**bits))
        if miller_rabin(a):
            return a


def generate_primes():
    p = gen_prime(256)
    q = gen_prime(256)
    p1 = gen_prime(256)
    q1 = gen_prime(256)
    while not p * q <= p1 * q1:
        generate_primes()
        return p, q, p1, q1


def gen_keys(p, q):
    n = p * q
    pass

print(gen_prime(256))
