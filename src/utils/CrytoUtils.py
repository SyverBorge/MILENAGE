from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def E(k, m: bytes) -> bytes:
    assert len(m) == 16
    assert len(k) == 16

    encryptor = Cipher(algorithms.AES128(k), modes.ECB()).encryptor()
    return encryptor.update(m) + encryptor.finalize()
