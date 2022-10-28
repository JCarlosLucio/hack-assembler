def translate_a_instruction(line: str, symbol_table: dict[str, int]):
    """Translates a instructions to their binary form
        ex. "@R9" -> "0000000000001001"

    Args:
        line (str): the line to be transformed
        symbol_table (dict[str, int]): the symbols used for transformation

    Returns:
        str: the binary form in a string padded with 0s
    """
    a_instruction = line[1:]
    symbol = int(symbol_table.get(a_instruction, a_instruction))
    binary = f"0{symbol:015b}"

    return binary
