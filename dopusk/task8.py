def main(data):
    d1 = ((((data[3] << 3 | data[2]) << 4)) << 3) 
    d2 = (d1 | data[1]) << 5 | data[0]
    return hex(d2)


print(main((5, 4, 2, 13)))