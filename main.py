import math
from typing import Tuple, List

# Note that the function only works for integers that satisfy 2^k, where k is any natural number.
# See README for more info on this.

def eliminationPermute(parts: int) -> List[Tuple]:
    orig_k = int(math.log2(parts))
    matches = []

    def rec(i: int, p: int) -> None:
        a = 2 ** i + 1 - p
        if i == orig_k:
            # print("%s\t\t-\t\t%s" % (int(p), int(parts + 1 - p)))
            matches.append((p, parts + 1 - p))
        else:
            rec(i + 1, p)
            rec(i + 1, a)

    rec(1, 1)
    return matches
