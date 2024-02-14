""" def main(n, b, m, p):
    res = 0
    for k in range(1, m + 1):
        for i in range(1, b + 1):
            for j in range(1, n + 1):
                res += (37 * j**2 - 66 * i**3) ** 6 + 50 * (
                    34 * p + 86 * k**2 + 41
                ) ** 3
    return res
 """

def main(n, b, m, p):
    res = [(37 * j**2 - 66 * i**3) ** 6 + 50 * (
                    34 * p + 86 * k**2 + 41
                ) ** 3 for k in range(1, m + 1) \
                    for i in range(1, b + 1) for j in range(1, n + 1)]
    print (type(res))
    return res

print(main(3, 8, 6, -0.11))
