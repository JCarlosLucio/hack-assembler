from coder import (
    find_between,
    translate,
    translate_a_instruction,
    translate_c_instruction,
)
from symbol_table import symbol_table, dest_table, comp_table, jump_table


def test_translate_an_int_a_instruction():
    assert translate_a_instruction("@9", symbol_table) == "0000000000001001"


def test_translate_a_symbol_a_instruction():
    assert translate_a_instruction("@SCREEN", symbol_table) == "0100000000000000"


def test_translate_c_instruction_without_semicolon():
    assert (
        translate_c_instruction("MD=A-1", dest_table, comp_table, jump_table)
        == "1110110010011000"
    )


def test_find_between_parentheses():
    assert find_between("(LOOP)", "(", ")") == "LOOP"


def test_find_between_equals_semicolon():
    assert find_between("D=D+A;JMP", "=", ";") == "D+A"


def test_translate_c_instruction_without_equals():
    assert (
        translate_c_instruction("0;JMP", dest_table, comp_table, jump_table)
        == "1110101010000111"
    )


def test_translate_complete_c_instruction():
    assert (
        translate_c_instruction("MD=A-1;JGE", dest_table, comp_table, jump_table)
        == "1110110010011011"
    )


def test_simple_a_instruction():
    assert (
        translate(["@9"], symbol_table, dest_table, comp_table, jump_table)
        == "0000000000001001"
    )


def test_a_instruction_with_symbol():
    assert (
        translate(["@R9"], symbol_table, dest_table, comp_table, jump_table)
        == "0000000000001001"
    )


def test_c_instruction_without_semicolon():
    assert (
        translate(["MD=A-1"], symbol_table, dest_table, comp_table, jump_table)
        == "1110110010011000"
    )


def test_c_instruction_without_equals():
    assert (
        translate(["0;JMP"], symbol_table, dest_table, comp_table, jump_table)
        == "1110101010000111"
    )


def test_complete_c_instruction():
    assert (
        translate(["MD=A-1;JGE"], symbol_table, dest_table, comp_table, jump_table)
        == "1110110010011011"
    )


def test_add():
    assert (
        translate(
            ["@2", "D=A", "@3", "D=D+A", "@0", "M=D"],
            symbol_table,
            dest_table,
            comp_table,
            jump_table,
        )
        == """0000000000000010
1110110000010000
0000000000000011
1110000010010000
0000000000000000
1110001100001000"""
    )


def test_max_l():
    assert (
        translate(
            [
                "@0",
                "D=M",
                "@1",
                "D=D-M",
                "@10",
                "D;JGT",
                "@1",
                "D=M",
                "@12",
                "0;JMP",
                "@0",
                "D=M",
                "@2",
                "M=D",
                "@14",
                "0;JMP",
            ],
            symbol_table,
            dest_table,
            comp_table,
            jump_table,
        )
        == """0000000000000000
1111110000010000
0000000000000001
1111010011010000
0000000000001010
1110001100000001
0000000000000001
1111110000010000
0000000000001100
1110101010000111
0000000000000000
1111110000010000
0000000000000010
1110001100001000
0000000000001110
1110101010000111"""
    )


def test_rect_l():
    assert (
        translate(
            [
                "@0",
                "D=M",
                "@23",
                "D;JLE",
                "@16",
                "M=D",
                "@16384",
                "D=A",
                "@17",
                "M=D",
                "@17",
                "A=M",
                "M=-1",
                "@17",
                "D=M",
                "@32",
                "D=D+A",
                "@17",
                "M=D",
                "@16",
                "MD=M-1",
                "@10",
                "D;JGT",
                "@23",
                "0;JMP",
            ],
            symbol_table,
            dest_table,
            comp_table,
            jump_table,
        )
        == """0000000000000000
1111110000010000
0000000000010111
1110001100000110
0000000000010000
1110001100001000
0100000000000000
1110110000010000
0000000000010001
1110001100001000
0000000000010001
1111110000100000
1110111010001000
0000000000010001
1111110000010000
0000000000100000
1110000010010000
0000000000010001
1110001100001000
0000000000010000
1111110010011000
0000000000001010
1110001100000001
0000000000010111
1110101010000111"""
    )
