import os
import sys

SEPARATOR = bytes.fromhex('FF FF FF FF')

def append_file(main_file, file_to_append, output_file):
    """
    Append file_to_append to main_file with separator in between
    and save as output_file
    """
    try:
        with open(main_file, 'rb') as f1, open(file_to_append, 'rb') as f2, open(output_file, 'wb') as out:
            # Write main file content
            out.write(f1.read())
            
            # Write separator
            out.write(SEPARATOR)
            
            # Write appended file content
            out.write(f2.read())
            
        print(f"Successfully appended {file_to_append} to {main_file} with separator as {output_file}")
    except Exception as e:
        print(f"Error appending files: {e}")

def extract_appended_file(combined_file, output_file):
    """
    Extract the appended file from combined_file (after the separator)
    and save as output_file
    """
    try:
        with open(combined_file, 'rb') as f:
            content = f.read()
            
        # Find the separator position
        separator_pos = content.find(SEPARATOR)
        
        if separator_pos == -1:
            print("Error: Separator not found in the combined file")
            return
            
        # Get the appended file content (after separator)
        appended_content = content[separator_pos + len(SEPARATOR):]
        
        with open(output_file, 'wb') as out:
            out.write(appended_content)
            
        print(f"Successfully extracted appended file as {output_file}")
    except Exception as e:
        print(f"Error extracting file: {e}")

def print_usage():
    print("Usage:")
    print("  To append files: python file_combiner.py append <main_file> <file_to_append> <output_file>")
    print("  To extract file: python file_combiner.py extract <combined_file> <output_file>")
    print("\nExample:")
    print("  python file_combiner.py append original.dat newdata.dat combined.dat")
    print("  python file_combiner.py extract combined.dat extracted.dat")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
        
    command = sys.argv[1].lower()
    
    if command == "append":
        if len(sys.argv) != 5:
            print("Error: Wrong number of arguments for append")
            print_usage()
            sys.exit(1)
        append_file(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == "extract":
        if len(sys.argv) != 4:
            print("Error: Wrong number of arguments for extract")
            print_usage()
            sys.exit(1)
        extract_appended_file(sys.argv[2], sys.argv[3])
    else:
        print(f"Error: Unknown command '{command}'")
        print_usage()
        sys.exit(1)