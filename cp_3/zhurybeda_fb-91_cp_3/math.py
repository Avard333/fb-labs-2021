def gcd(a, b):
    if not b:
        return 1, 0, a
    y, x, d = gcd(b, a % b)
    return x, y - (a // b) * x, d


# print(gcd(154, 803))


def linear_comp(a, b, n):
    a_re, _, d = gcd(a, n)
    if d == 1:
        x = (a_re * b) % n
        return x
    else:
        solutions = []
        if b % d == 0:
            a1 = a / d
            b1 = b / d
            n1 = n / d
            x = linear_comp(a1, b1, n1)
            solutions.append(x)
            for i in range(1, d):
                solutions.append(x + int(n / d) * i)
            return solutions
        else:
            return None


# print(linear_comp(154, 22, 803))