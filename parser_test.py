from parser import parse


def test_simple_parse():
    with open("./to_assemble/Add.asm") as file:
        simple_text = file.read()
    assert parse(simple_text) == ["@2", "D=A", "@3", "D=D+A", "@0", "M=D"]
