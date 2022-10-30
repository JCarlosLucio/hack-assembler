def find_between(s: str, start: str, end: str):
    """Find the a string between two strings (start and end)

    Args:
        s (str): the complete string
        start (str): the start string of the enclosing wanted value
        end (str): the end string of the enclosing wanted value

    Returns:
        str: the string found between the start and the end string
    """
    return s[s.index(start) + 1 : s.index(end)]


def handle_labels(
    lines: list[str], symbol_table: dict[str, int]
) -> dict[str, list[str] | dict[str, int]]:
    """Handles labels ( surrounded by parentheses ex. (LOOP)) for translation
    Removes labels from lines and adds their values to the symbol table

    Args:
        lines (list[str]): The lines with labels
        symbol_table (dict[str, int]): the symbol table to adding label values

    Returns:
        dict[str, list[str] | dict[str, int]]: _description_
    """
    labels_count = 0
    lines_without_labels: list[str] = []

    # filter lines without labels and add their value to symbol_table
    for i, line in enumerate(lines):
        if line.startswith("(") and line.endswith(")"):
            label = find_between(line, "(", ")")
            symbol_table[label] = i - labels_count
            labels_count += 1
        else:
            lines_without_labels.append(line)

    return {"lines": lines_without_labels, "symbol_table": symbol_table}


def handle_variables(lines: list[str], symbol_table: dict[str, int]) -> dict[str, int]:
    """Add variables (a instructions that aren't default symbols or labels) to symbol_table

    Args:
        lines (list[str]): clean lines without labels and with variables to be handled
        symbol_table (dict[str, int]): the symbol table where variables will be added

    Returns:
        dict[str, int]: the symbol table with variables added
    """
    # 16 is the start of memory space for variables from language specs
    variable_mem_pos = 16

    for line in lines:
        if line.startswith("@"):
            a_instruction = line[1:]

            if not a_instruction.isdigit() and not (a_instruction in symbol_table):
                symbol_table[a_instruction] = variable_mem_pos
                variable_mem_pos += 1

    return symbol_table


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


def translate_c_instruction(
    line: str,
    dest_table: dict[str, str],
    comp_table: dict[str, str],
    jump_table: dict[str, str],
):
    """Translates c instructions (dest=comp;jump) to their binary form
        ex. "MD=A-1" -> "1110110010011000"

    Args:
        line (str): the line to be transformed
        dest_table (dict[str, str]): the symbols for transforming dest instruction
        comp_table (dict[str, str]): the symbols for transforming comp instruction
        jump_table (dict[str, str]): the symbols for transforming jump instruction

    Returns:
        str: the binary form in a string
    """
    dest = "null"
    comp = line
    jump = "null"

    if ";" in line:
        semicolon_index = line.index(";")
        comp = line[:semicolon_index]
        jump = line[semicolon_index + 1 :]

    if "=" in line:
        equals_index = line.index("=")
        dest = line[:equals_index]
        comp = line[equals_index + 1 :]
        if ";" in line:
            comp = find_between(line, "=", ";")

    dest = dest_table[dest]
    comp = comp_table[comp]
    jump = jump_table[jump]

    binary = "111" + comp + dest + jump

    return binary


def translate(
    lines: list[str],
    symbol_table: dict[str, int],
    dest_table: dict[str, str],
    comp_table: dict[str, str],
    jump_table: dict[str, str],
):
    """The translation of the entire of the parsed lines of a asm program

    Args:
        lines (list[str]): the parsed lines of the asm program
        symbol_table (dict[str, int]): the symbols used for transforming a instructions
        dest_table (dict[str, str]): the symbols for transforming dest instruction in c instructions
        comp_table (dict[str, str]): the symbols for transforming comp instruction in c instructions
        jump_table (dict[str, str]): the symbols for transforming jump instruction in c instructions

    Returns:
        str: a string of the translated lines
    """
    translated: list[str] = []

    for line in lines:
        if line.startswith("@"):
            binary = translate_a_instruction(line, symbol_table)
            translated.append(binary)
        else:
            binary = translate_c_instruction(
                line,
                dest_table,
                comp_table,
                jump_table,
            )
            translated.append(binary)

    return "\n".join(translated)
