from src.utils.CrytoUtils import E
from src.utils.PrintoutUtils import a2b


def IN1(sqn: bytes, amf: bytes) -> bytes:
    in1 = sqn + amf + sqn + amf
    return in1


def xor(a, b: bytes) -> bytes:
    assert len(a) == len(b)
    assert len(a) > 0

    result = bytearray(len(a))

    for i in range(len(result)):
        result[i] = a[i] ^ b[i]

    return bytes(result)


def rot(a: bytes, r) -> bytes:
    r_num = r // 8
    top = a[0:r_num]
    end = a[r_num:]

    rotated = end + top
    return rotated


def set_bits(b: bytearray, bits) -> bytearray:
    c = b
    c[-1] = bits
    return c


def OPC(op, k):
    op_E = E(k, op)
    opc = xor(op_E, op)

    return opc
