from parser import parse


# SymbolTable - manages the symbol table

# Main - initializes the I/O files and drives the process
file_name = input("Enter the name of the file to assamble: \n")

with open(f"./to_assemble/{file_name}.asm") as file:
    contents = file.read()

# Parser - unpacks each instruction into its underlying field
parsed = parse(contents)


# create/write to new file
with open(f"./assembled/{file_name}.hack", mode="w") as data:
    data.write(f"{parsed}")
