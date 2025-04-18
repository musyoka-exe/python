def modify_and_save_file(input_filename, output_filename):
    """
    Reads the input file, modifies its content (converts to uppercase),
    and writes the modified content to the output file.
    """
    try:
        # Open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"✅ File successfully processed. Modified content saved to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read or write the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def main():
    """
    Main function to handle user input and execute the file processing.
    """
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ").strip()
    
    # Define the output filename
    output_filename = "modified_output.txt"
    
    # Process the file
    modify_and_save_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
