from src.milenage import constants as const
from src.utils.CrytoUtils import E
from src.utils.valuesUtils import IN1, rot, xor


def opc_and_rand(rand, opc, k):
    temp = E(k, xor(rand, opc))
    return temp


def f1(k: bytes, rand: bytes, sqn: bytes, amf: bytes, opc: bytes) -> tuple:
    in1 = IN1(sqn, amf)
    v_1 = xor(in1, opc)
    temp = opc_and_rand(rand, opc, k)

    v_1_rotated = rot(v_1, const.R1)
    xor_togheter = xor(xor(const.C1, temp), v_1_rotated)
    encrypto = E(k, xor_togheter)
    f1_full_value = xor(encrypto, opc)
    f1_flat = f1_full_value[0:8]
    f1_star = f1_full_value[8:16]

    return f1_flat, f1_star


def f2_and_f5(k: bytes, rand: bytes, opc: bytes):
    temp = opc_and_rand(rand, opc, k)
    temp2 = xor(temp, opc)
    temp3 = rot(temp2, const.R2)
    temp4 = xor(const.C2, temp3)
    encrypto = E(k, temp4)
    xor_encrypto = xor(encrypto, opc)
    return xor_encrypto


def f2(k: bytes, rand: bytes, opc: bytes) -> bytes:
    f2_value = f2_and_f5(k, rand, opc)
    return f2_value[8:16]


def f3(k: bytes, rand: bytes, opc: bytes) -> bytes:
    opcRand = opc_and_rand(rand, opc, k)
    xor_onto_opcrand = xor(opc, opcRand)
    roated = rot(xor_onto_opcrand, const.R3)
    xor_after_roatation = xor(const.C3, roated)
    encryped = E(k, xor_after_roatation)
    f3_value = xor(opc, encryped)
    return f3_value


def f4(k: bytes, rand: bytes, opc: bytes) -> bytes:
    opcRand = opc_and_rand(rand, opc, k)
    xor_onto_opcrand = xor(opc, opcRand)
    rotated = rot(xor_onto_opcrand, const.R4)
    xor_after_roatation = xor(const.C4, rotated)
    encryped = E(k, xor_after_roatation)
    f4_value = xor(opc, encryped)
    return f4_value


def f5(k: bytes, rand: bytes, opc: bytes) -> bytes:
    f5_value = f2_and_f5(k, rand, opc)
    return f5_value[0:6]


def f5_star(k: bytes, rand: bytes, opc: bytes) -> bytes:
    opcRand = opc_and_rand(rand, opc, k)
    xor_onto_opcrand = xor(opc, opcRand)
    rotated = rot(xor_onto_opcrand, const.R5)
    xor_after_roatation = xor(const.C5, rotated)
    encrypted = E(k, xor_after_roatation)
    f5_star_value = xor(opc, encrypted)
    return f5_star_value[0:6]
