# Function to read a file, convert its content to uppercase, and write it back to the same file
def read_and_write_file(filename):
    try:
        # Open the file in 'r' (read) mode
        with open(filename, 'r') as file:
            # Read the content of the file into the 'content' variable
            content = file.read()
        
        # Close the file after reading

        # Open the same file in 'w' (write) mode, which will overwrite its contents
        with open(filename, 'w') as file:
            # Write the uppercase content back to the file
            file.write(content.upper())
        
        # Print a success message
        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        # If an error occurs during file operations, print an error message
        print(f"An error occurred: {str(e)}")

# Main function
def main():
    # Define the filename of the file to be processed
    filename = "sample.txt"
    # Call the read_and_write_file function with the specified filename
    read_and_write_file(filename)

# Check if this script is being run as the main program
if _name_ == "_main_":
    # If so, execute the main function
    main()
