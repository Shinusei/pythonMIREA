""" import struct


class Parser:
    d = {
            'float': '<f',
            'double': '<d',
            'char': '<c',
            'int8': '<b',
            'uint8': '<B',
            'int16': '<h',
            'uint16': '<H',
            'int32': '<i',
            'uint32': '<I',
            'int64': '<q',
            'uint64': '<Q'
        }

    def __init__(self, buf, offset):
        self.buf = buf
        self.offset = offset

    def join(self, offset):
        return Parser(self.buf, offset)

    def get(self, type_d):
        buf = struct.unpack_from(self.d[type_d], self.buf, self.offset)
        self.offset += struct.calcsize(self.d[type_d])
        return buf[0]


def parser_a(parser):
    a1 = parser.get("int32")
    a2 = parser_b(parser.join(parser.get("uint32")))
    a3 = parser.get("uint16")
    a4 = parser.get("double")
    a5 = parser.get("float")
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}


def parser_b(parser):
    b1 = parser.get("uint8")
    b2 = [parser_c(parser) for _ in range(2)]
    b3 = parser.get("int32")
    b4 = parser.get("int8")
    b5 = parser.get("int8")
    b6 = parser_d(parser)
    b7 = parser.get("int8")
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7}


def parser_c(parser):
    c1 = [parser.get("int16") for _ in range(4)]
    c2_size = parser.get("uint32")
    c2_offset = parser.get("uint32")
    c2_parser = parser.join(c2_offset)
    c2 = [c2_parser.get("int8") for _ in range(c2_size)]
    c3 = [parser.get("int64") for _ in range(2)]
    c4 = parser.get("int32")
    c5 = parser.get("uint32")
    c6 = parser.get("int64")
    c7 = parser.get("uint16")
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6, 'C7': c7}


def parser_d(parser):
    d1 = parser.get("uint8")
    d2_size = parser.get("uint16")
    d2_offset = parser.get("uint32")
    d2_parser = parser.join(d2_offset)
    d2 = [d2_parser.get("int16") for _ in range(d2_size)]
    d3 = parser.get("int8")
    return {'D1': d1, 'D2': d2, 'D3': d3}


def main(data):
    return parser_a(Parser(data, 4))
 """
 
import struct


class Parser:
    d = {
            'float': '<f',
            'double': '<d',
            'char': '<c',
            'int8': '<b',
            'uint8': '<B',
            'int16': '<h',
            'uint16': '<H',
            'int32': '<i',
            'uint32': '<I',
            'int64': '<q',
            'uint64': '<Q'
        }

    def __init__(self, buf, offset):
        self.buf = buf
        self.offset = offset

    def join(self, offset):
        return Parser(self.buf, offset)

    def get(self, type_d):
        buf = struct.unpack_from(self.d[type_d], self.buf, self.offset)
        self.offset += struct.calcsize(self.d[type_d])
        return buf[0]


def parser_a(parser):
    a1 = parser.get("int16")
    a2_size = parser.get("uint16")
    a2_offset = parser.get("uint32")
    a2_parser = parser.join(a2_offset)
    a2 = [a2_parser.get(parser_b(parser)) for _ in range(a2_size)]
    a3 = parser_c(parser)
    a4 = a4_size = parser.get("uint16")
    a4_offset = parser.get("uint32")
    a4_parser = parser.join(a4_offset)
    a4 = [a4_parser.get("int8") for _ in range(a4_size)]
    a5 = parser.get("int64")
    a6 = parser.get("uint64")
    a7 = parser.get("float")
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5, 'A6': a6, 'A7': a7}


def parser_b(parser):
    b1 = parser.get("int64")
    b2 = parser.get("uint32")
    b3 = b3_size = parser.get("uint32")
    b3_offset = parser.get("uint32")
    b3_parser = parser.join(b3_offset)
    b3 = [b3_parser.get("char") for _ in range(b3_size)]
    return {'B1': b1, 'B2': b2, 'B3': b3}


def parser_c(parser):
    c1 = parser.get("uint8")
    c2 = parser_d(parser)
    c3 = parser.get("int16")
    c4 = parser.get("uint32")
    c5 = parser.get("double")
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5}


def parser_d(parser):
    d1 = parser.get("int16")
    d2 = parser.get("uint8")
    d3 = parser.get("uint16")
    d4 = [parser.get("int16") for _ in range(4)]
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}


def main(data):
    return parser_a(Parser(data, 5))


import pprint

pprint.pprint(main(b'GYVPh>\x04\x00Z\x00\x00\x00\x94\xbc\xbf\x86I\xc9\xae\xa9\xd0\xd6\xd5\xf8'
 b'\xd5\xee@\x1c`|\x89\xdf\x18\x83\x92td\xfa\xc1\xbf\x04\x00\xaa\x00'
 b'\x00\x00A\xe5h2\x04\x82\xbec\xcaD\xf6v\xec\x01$\xc4\x7f\x13\t?hb$>G,v?5\xe8'
 b'{>\xdaZa?kplkchca\xe9\r\xa1\x03 \x10\xd9\xbe[5\xe1\x97\x02\x00\x00\x00R\x00'
 b'\x00\x00\x11s\xa6\xc6\xd4{-\xd4L\xac\xe0c\x02\x00\x00\x00T\x00'
 b'\x00\x00\xc3\xaf\xef\x97\xf9\x91O\xaf\xb9\xd4"\x02\x02\x00\x00\x00V\x00'
 b'\x00\x00\xd9[\xe9\x8e\xf7\x15\xc7\xc1\xa4\xf1\x88\xb0\x02\x00\x00\x00X\x00'
 b'\x00\x00a\xdfd\xbc'))