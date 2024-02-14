def main(n, b, m, p):
    res = 0
    for k in range(1, m + 1):
        for i in range(1, b + 1):
            for j in range(1, n + 1):
                res += (37 * j**2 - 66 * i**3) ** 6 + 50 * (
                    34 * p + 86 * k**2 + 41
                ) ** 3
    return res


def main(n, b, m, p):
    res = [
        (37 * j**2 - 66 * i**3) ** 6 + 50 * (34 * p + 86 * k**2 + 41) ** 3
        for k in range(1, m + 1)
        for i in range(1, b + 1)
        for j in range(1, n + 1)
    ]
    return sum(res)


def main(n, b, m, p):
    k = 1
    res = 0
    while k <= m:
        i = 1
        while i <= b:
            j = 1
            while j <= n:
                res += (37 * j**2 - 66 * i**3) ** 6 + 50 * (
                    34 * p + 86 * k**2 + 41
                ) ** 3
                j += 1
            i += 1
        k += 1
    return res


def main(n, b, m, p, i=1, j=1, k=1):
    if j > n:
        j = 1
        i += 1
    if i > b:
        i = 1
        k += 1
    if k > m:
        return 0
    return (
        (37 * j**2 - 66 * i**3) ** 6
        + 50 * (34 * p + 86 * k**2 + 41) ** 3
        + main(n, b, m, p, i, j+1, k)
    )
 


def main(n, b, m, p):
    res = (
        (37 * j**2 - 66 * i**3) ** 6 + 50 * (34 * p + 86 * k**2 + 41) ** 3
        for k in range(1, m + 1)
        for i in range(1, b + 1)
        for j in range(1, n + 1)
    )
    return sum(res)
