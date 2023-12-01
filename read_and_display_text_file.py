def read_and_display_text_file(file_name):
    # Open the file in read mode
    file = open(file_name, 'r')

    # Read and print each line in the file
    print(f"Content of '{file_name}':")
    content = file.read()
    print(content)

    # Close the file
    file.close()

# Example usage:
file_name = "read_me.txt"  # Replace with the actual file name
read_and_display_text_file(file_name)
