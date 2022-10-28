from coder import translate_a_instruction
from symbol_table import symbol_table


def test_translate_an_int_a_instruction():
    assert translate_a_instruction("@9", symbol_table) == "0000000000001001"


def test_translate_a_symbol_a_instruction():
    assert translate_a_instruction("@SCREEN", symbol_table) == "0100000000000000"
