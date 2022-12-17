def parse(text: str):
    """Removes whitespace and comments(that start with '//') from text

    Args:
        text (str): the text to parse

    Returns:
        list[str]: a list of strings without whitespace and comments
    """

    lines = text.splitlines()
    cleaned: list[str] = []

    for line in lines:
        stripped = line.lstrip()

        if stripped and not stripped.startswith("//"):
            clean = stripped.split(" ")[0]
            cleaned.append(clean)

    return cleaned
