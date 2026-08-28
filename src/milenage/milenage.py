from src.milenage import constants as const
from src.utils.CrytoUtils import E
from src.utils.valuesUtils import IN1, rot, xor


def f1(k: bytes, rand: bytes, sqn: bytes, amf: bytes, opc: bytes) -> bytes:
    in1 = IN1(sqn, amf)
    v_1 = xor(in1, opc)
    temp = E(k, xor(rand, opc))

    v_1_rotated = rot(v_1, const.R1)
    xor_togheter = xor(xor(const.C1, temp), v_1_rotated)
    encrypto = E(k, xor_togheter)
    f1_full_value = xor(encrypto, opc)

    return f1_full_value[0:8]
