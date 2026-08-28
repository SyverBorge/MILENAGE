import pytest

from tests import a2b, b2a, f1


@pytest.mark.parametrize(
    "k, rand, sqn, amf, opc, expected",
    [
        pytest.param(
            a2b("465b5ce8 b199b49f aa5f0a2e e238a6bc"),
            a2b("23553cbe 9637a89d 218ae64d ae47bf35"),
            a2b("ff9bb4d0 b607"),
            a2b("b9b9"),
            a2b("cd63cb71 954a9f4e 48a5994e 37a02baf"),
            "4a9ffac3 54dfafb3",
            id="f1_test_1",
        ),
        pytest.param(
            a2b("0396eb31 7b6d1c36 f19c1c84 cd6ffd16"),
            a2b("c00d6031 03dcee52 c4478119 494202e8"),
            a2b("fd8eef40 df7d"),
            a2b("af17"),
            a2b("53c15671 c60a4b73 1c55b4a4 41c0bde2"),
            "5df5b318 07e258b0",
            id="f1_test_2",
        ),
    ],
)
def test_f1(k, rand, sqn, amf, opc, expected):
    value = f1(k, rand, sqn, amf, opc)
    assert b2a(value[0]) == expected
