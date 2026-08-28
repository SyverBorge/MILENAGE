import pytest

from tests import IN1, OPC, E, a2b, b2a, const, rot, set_bits, xor


@pytest.mark.parametrize(
    "hex_str, expected_bytes",
    [
        (
            "465b5ce8 b199b49f aa5f0a2e e238a6bc",
            bytes.fromhex("465b5ce8b199b49faa5f0a2ee238a6bc"),
        ),
        ("0011223344556677", bytes.fromhex("0011223344556677")),
        ("ab", bytes.fromhex("ab")),
    ],
)
def test_a2b_valid(hex_str, expected_bytes):
    assert a2b(hex_str) == expected_bytes


def test_a2b_odd_length_raises():
    with pytest.raises(AssertionError):
        a2b("abc")


@pytest.mark.parametrize(
    "data, expected_hex",
    [
        (
            bytes.fromhex("00112233445566778899aabbccddeeff"),
            "00112233 44556677 8899aabb ccddeeff",
        ),
        (bytes.fromhex("0011223344556677"), "0011223344556677"),
        (bytes([0xAB]), "ab"),
    ],
)
def test_b2a_valid(data, expected_hex):
    assert b2a(data) == expected_hex


def test_b2a_empty_raises():
    with pytest.raises(AssertionError):
        b2a(b"")


@pytest.mark.parametrize(
    "sqn, amf, expected_in1",
    [
        pytest.param(
            "ff9bb4d0 b607",
            "b9b9",
            "ff9bb4d0 b607b9b9 ff9bb4d0 b607b9b9",
            id="sqn1_amf1",
        ),
        pytest.param(
            "00000000 0001",
            "0001",
            "00000000 00010001 00000000 00010001",
            id="sqn2_amf2",
        ),
    ],
)
def test_IN1_concatination(sqn, amf, expected_in1):
    assert b2a(IN1(a2b(sqn), a2b(amf))) == expected_in1


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param("0101", "1010", "1111", id="a1_b1"),
        pytest.param("00001111", "11110000", "11111111"),
    ],
)
def test_xor(a, b, expected):
    assert b2a(xor(a2b(a), a2b(b))) == expected


@pytest.mark.parametrize(
    "a, r, expected",
    [
        pytest.param(
            bytes([i for i in range(16)]),
            const.R1,
            "08090a0b 0c0d0e0f 00010203 04050607",
        ),
        pytest.param(
            bytes([i for i in range(16)]),
            const.R3,
            "04050607 08090a0b 0c0d0e0f 00010203",
        ),
    ],
)
def test_rot(a, r, expected):
    assert b2a(rot(a, r)) == expected


@pytest.mark.parametrize(
    "byte, bits, expected",
    [
        pytest.param(
            bytearray(16),
            0b00000001,
            "00000000 00000000 00000000 00000001",
            id="bytes0_bits1",
        )
    ],
)
def test_setbits(byte, bits, expected):
    assert b2a(bytes(set_bits(byte, bits))) == expected


@pytest.mark.parametrize(
    "k, m, xc",
    [
        pytest.param(
            "465b5ce8 b199b49f aa5f0a2e e238a6bc",
            "ee36f7cf 037d37d3 692f7f03 99e7949a",
            "9e2980c5 9739da67 b136355e 3cede6a2",
            id="K1M1",
        )
    ],
)
def test_E(k, m, xc):
    assert E(a2b(k), a2b(m)) == a2b(xc)


@pytest.mark.parametrize(
    "op, k, opc",
    [
        pytest.param(
            "cdc202d5 123e20f6 2b6d676a c72cb318",
            "465b5ce8 b199b49f aa5f0a2e e238a6bc",
            "cd63cb71 954a9f4e 48a5994e 37a02baf",
            id="op1k1opc1",
        )
    ],
)
def test_OPC(op, k, opc):
    assert b2a(OPC(a2b(op), a2b(k))) == opc
