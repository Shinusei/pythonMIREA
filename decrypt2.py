def encode_val(n, k, val):
    encoded = 0
    for i in range(k):
        encoded = (encoded << 3) | ((val >> i) & 1) * 7
    return encoded

def decode_val(n, k, val):
    decoded = 0
    for i in range(k):
        decoded = (decoded << 1) | ((val >> (3 * i)) & 1)
    return decoded

def ham_dist(a, b):
    return bin(a ^ b).count('1')

def correct_errors(message):
    corrected = []
    for val in message:
        binary = bin(val)[2:].zfill(24)
        groups = [binary[i:i+3] for i in range(0, 24, 3)]
        corrected_binary = ''
        for group in groups:
            if group.count('1') > 1:
                corrected_binary += '1'
            else:
                corrected_binary += '0'
        corrected_val = int(corrected_binary, 2)
        corrected.append(corrected_val)
    return corrected

message = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407, 6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903, 2067967, 2068456]
corrected_message = correct_errors(message)
#print(corrected_message)
for i in corrected_message:
    print(chr(i), end="")
print()