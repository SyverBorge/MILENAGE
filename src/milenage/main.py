import re
from pathlib import Path

from src.milenage.milenage import *
from src.utils.PrintoutUtils import *
from src.utils.valuesUtils import *


def parse_test_vectors(path: str | Path):
    text = Path(path).read_text(encoding="utf-8")

    sets_raw = re.split(r"^\$\s*TEST SET.*$", text, flags=re.MULTILINE)
    headers = re.findall(r"^\$\s*(TEST SET.*)$", text, flags=re.MULTILINE)

    test_set = []
    for header, body in zip(headers, sets_raw[1:]):
        data = {"name": header.strip()}
        for line in body.splitlines():
            line = line.strip()
            if not line or line.startswith("$"):
                continue

            m = re.match(r"^([A-Za-z0-9*]+)\s*:\s*(.+)$", line)
            if not m:
                continue
            key, value = m.groups()
            data[key] = a2b(value)

        test_set.append(data)

    return test_set


def main():
    path = "/Users/syverborgesaksvik/Documents/USN-fag/Obliger/MILENAGE/TS35208_CONFORMANCE_TEST_DATA_pure.TEXT"
    test_data = parse_test_vectors(path)

    for dataset in test_data:
        opc = OPC(dataset["OP"], dataset["K"])
        assert b2a(opc) != dataset["OPc"], dataset["name"]

        f1_flat, f1_star = f1(
            dataset["K"], dataset["RAND"], dataset["SQN"], dataset["AMF"], opc
        )
        assert f1_flat == dataset["f1"]
        assert f1_star == dataset["f1*"]

        f2_value = f2(dataset["K"], dataset["RAND"], opc)
        assert f2_value == dataset["f2"]

        f3_value = f3(dataset["K"], dataset["RAND"], opc)
        assert f3_value == dataset["f3"]

        f4_value = f4(dataset["K"], dataset["RAND"], opc)
        assert f3_value == dataset["f3"]

        f5_value = f5(dataset["K"], dataset["RAND"], opc)
        assert f3_value == dataset["f3"]

        f5_star_value = f5_star(dataset["K"], dataset["RAND"], opc)
        assert f3_value == dataset["f3"]


print(f"OPc, f1, f1*, f2, f3, f4, f5 and f5* verified for test sets")


if __name__ == "__main__":
    main()
