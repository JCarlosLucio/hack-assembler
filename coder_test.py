from coder import translate_a_instruction, translate_c_instruction
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
