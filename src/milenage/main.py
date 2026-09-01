import re
from pathlib import Path

from src.milenage.milenage import *
from src.utils.PrintoutUtils import *
from src.utils.valuesUtils import *

PROJECT_ROOT = Path(__file__).resolve().parents[2]


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
    path = PROJECT_ROOT / "TS35208_CONFORMANCE_TEST_DATA_pure.TEXT"
    path2 = PROJECT_ROOT / "EXTRA_TESTS-1.text"
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
        assert f4_value == dataset["f4"]

        f5_value = f5(dataset["K"], dataset["RAND"], opc)
        assert f5_value == dataset["f5"]

        f5_star_value = f5_star(dataset["K"], dataset["RAND"], opc)
        assert f5_star_value == dataset["f5*"]

    print(f"OPc, f1, f1*, f2, f3, f4, f5 and f5* verified for test sets")

    test_data_extra = parse_test_vectors(path2)

    for dataset in test_data_extra:
        opc = OPC(dataset["OP"], dataset["K"])

        f1_flat, f1_star = f1(
            dataset["K"], dataset["RAND"], dataset["SQN"], dataset["AMF"], opc
        )

        f2_value = f2(dataset["K"], dataset["RAND"], opc)

        f3_value = f3(dataset["K"], dataset["RAND"], opc)

        f4_value = f4(dataset["K"], dataset["RAND"], opc)

        f5_value = f5(dataset["K"], dataset["RAND"], opc)

        f5_star_value = f5_star(dataset["K"], dataset["RAND"], opc)

        print("Dataset: ", dataset["name"])
        print("OPC: ", b2a(opc))
        print("f1: ", b2a(f1_flat))
        print("f2: ", b2a(f2_value))
        print("f3: ", b2a(f3_value))
        print("f4: ", b2a(f4_value))
        print("f5: ", b2a(f5_value))

    print("\n\nSuccess!!! all test run as intended!!!")


if __name__ == "__main__":
    main()
