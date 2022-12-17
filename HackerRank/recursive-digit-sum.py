# https://www.hackerrank.com/challenges/recursive-digit-sum
# https://programs.programmingoneonone.com/2021/03/hackerrank-recursive-digit-sum-solution.html


def sup_digits(x, k):
    a = digsum(x)
    return sup_digit(str(int(a) * k))


def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit(digsum(x))


def digsum(x):
    return str(sum((int(i) for i in list(x))))


n, k = input().split()
print(sup_digits(n, int(k)))
