from src.utils.PrintoutUtils import a2b


def IN1(sqn: str, amf: str) -> bytes:
    SQN = a2b(sqn)
    AMF = a2b(amf)

    in1 = SQN + AMF + SQN + AMF
    return in1

def xor(a, b: bytes) -> bytes:
    assert len(a) == len(b),
    assert len(a) > 0,

    result = bytearray(len(a))

    for i in range(len(result)):
        result[i] = a[i] ^ b[i]

    return bytes(result)

