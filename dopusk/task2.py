from math import log2


def main(y):
    if y < 81:
        return 46 - y**6/39 - 71*(y**2 + y**3/91 + 8*y)**4
    if y < 141:
        return y**3
    if y < 211:
        return 30*log2(y**2 - 1 - y)**5
    if y < 279:
        return y**3 + 1 + y**12
    else:
        return 1 - 69*y**2 - y**3/91

import math


def main(y):
    a = 46 - y**6/39 - 71(y**2 + y**3/91 + 8*y)**4 if y < 81 \
           else y**3 if y < 141 \
           else 30*math.log2(y**2 - 1 - y)**5 if y < 211 else y**3 + 1 + y**12
    a = 1 - 69*y**2 - y**3/91 if y > 279 else a
    return a


from math import log2


def main(y):
    a = [46 - y**6 / 39 - 71 * (y**2 + y**3 / 91 + 8 * y) ** 4, y**3][y > 81]
    a = [a, 30 * log2(y**2 - 1 - y) ** 5][y > 141]
    a = [a, y**3 + 1 + y**12][y > 211]
    a = [a, 1 - 69 * y**2 - y**3 / 91][y > 279]
    return a
   
