def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, adds a line number to each line, and writes the modified
    content to a new file. Handles potential file errors.
    """
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")
        return

    modified_lines = []
    for index, line in enumerate(lines):
        modified_line = f"{index + 1}: {line.strip()}\n"
        modified_lines.append(modified_line)

    try:
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to the file '{output_filename}'.")

if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name for the output file: ")
    modify_and_write_file(input_file, output_file)
