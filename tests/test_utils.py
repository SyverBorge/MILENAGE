import pytest

from tests import IN1, a2b, b2a, xor


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
    assert b2a(IN1(sqn, amf)) == expected_in1


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param("0101", "1010", "1111", id="a1_b1"),
        pytest.param("00001111", "11110000", "11111111"),
    ],
)
def test_xor(a, b, expected):
    assert b2a(xor(a2b(a), a2b(b))) == expected
