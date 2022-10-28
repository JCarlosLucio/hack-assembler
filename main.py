from parser import parse
from coder import translate
from symbol_table import symbol_table, dest_table, comp_table, jump_table

# SymbolTable - manages the symbol table

# Main - initializes the I/O files and drives the process
file_name = input("Enter the name of the file to assamble: \n")

with open(f"./to_assemble/{file_name}.asm") as file:
    contents = file.read()

# Parser - unpacks each instruction into its underlying field
parsed = parse(contents)

# Code - translates each field into its corresponding binary value
translated = translate(parsed, symbol_table, dest_table, comp_table, jump_table)

# create/write to new file
with open(f"./assembled/{file_name}.hack", mode="w") as data:
    data.write(f"{translated}")
