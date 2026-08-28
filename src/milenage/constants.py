from src.utils.valuesUtils import set_bits

# Rotating constants
R1 = 64
R2 = 0
R3 = 32
R4 = 64
R5 = 96

# Constants
C1 = bytes(16)
C2 = set_bits(bytearray(16), 0b00000001)
C3 = set_bits(bytearray(16), 0b00000010)
C4 = set_bits(bytearray(16), 0b00000100)
C5 = set_bits(bytearray(16), 0b00001000)
