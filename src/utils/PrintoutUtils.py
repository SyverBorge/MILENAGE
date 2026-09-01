def a2b(s: str) -> bytes:
    s = s.replace(" ", "")
    assert len(s) % 2 == 0
    bytelist = list()
    for i in range(0, len(s), 2):
        bytelist.append(int("0x" + s[i] + s[i + 1], 16))
    return bytes(bytelist)


hexdig = "0123456789abcdef"


def b2a(b: bytes) -> str:
    assert len(b) > 0
    hexstr = ""
    for byte in b:
        lo = hexdig[byte & 0x0F]
        hi = hexdig[byte >> 4]
        hexstr += hi + lo

    if len(hexstr) == 32:
        hexstr = (
            hexstr[0:8] + " " + hexstr[8:16] + " " + hexstr[16:24] + " " + hexstr[24:]
        )

    if len(hexstr) == 16:
        hexstr = hexstr[0:8] + " " + hexstr[8:16]

    else:
        hs = ""
        while len(hexstr) >= 8:
            hs = hs + hexstr[0:8]
            hexstr = hexstr[8:]
        hexstr = hs + hexstr

    return hexstr
