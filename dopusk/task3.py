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


def main(n, b, m, p, i=1, j=1, c=1, s=0):
    if j <= b:
        if i <= m:
            if c <= n:
                s = (37 * j**2 - 66 * i**3) ** 6 + 50 * (
                    34 * p + 86 * k**2 + 41
                ) ** 3
                s = main(n, m, b, i, j, c + 1, s)
            s = main(n, m, b, i + 1, j, 1, s)
        s = main(n, m, b, 1, j + 1, 1, s)
    return s


def main(n, b, m, p):
    res = (
        (37 * j**2 - 66 * i**3) ** 6 + 50 * (34 * p + 86 * k**2 + 41) ** 3
        for k in range(1, m + 1)
        for i in range(1, b + 1)
        for j in range(1, n + 1)
    )
    return sum(res)
