import math


# Note that the function only works for integers that satisfy 2^k, where k is any natural number.
# See README for more info on this.

def func(parts):
    orig_k = math.log2(parts)

    def rec(i, p):
        a = p
        b = parts / (2 ** (orig_k - i)) + 1 - p
        if i == orig_k:
            print("%s\t\t-\t\t%s" % (int(a), int(parts + 1 - a)))
            return
        else:
            rec(i + 1, a)
            rec(i + 1, b)

    rec(1, 1)
