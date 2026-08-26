from src.utils.PrintoutUtils import a2b


def IN1(sqn: str, amf: str) -> bytes:
    SQN = a2b(sqn)
    AMF = a2b(amf)

    in1 = SQN + AMF + SQN + AMF
    return in1
