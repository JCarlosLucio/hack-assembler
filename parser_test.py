from asm_parser import parse


def test_simple_parse():
    with open("./to_assemble/Add.asm") as file:
        simple_text = file.read()
    assert parse(simple_text) == ["@2", "D=A", "@3", "D=D+A", "@0", "M=D"]


def test_parse_with_inline_comments():
    with open("./to_assemble/Max.asm") as file:
        with_inline_comments = file.read()
    assert parse(with_inline_comments) == [
        "@R0",
        "D=M",
        "@R1",
        "D=D-M",
        "@OUTPUT_FIRST",
        "D;JGT",
        "@R1",
        "D=M",
        "@OUTPUT_D",
        "0;JMP",
        "(OUTPUT_FIRST)",
        "@R0",
        "D=M",
        "(OUTPUT_D)",
        "@R2",
        "M=D",
        "(INFINITE_LOOP)",
        "@INFINITE_LOOP",
        "0;JMP",
    ]
