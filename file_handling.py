# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file and write initial content
        with open("my_file.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is my first file.\n")
            file.write("The number is 42.\n")
        print("File created and written successfully.")

    except PermissionError:
        print("Error: Permission denied when trying to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Create file operation completed.")

def read_file():
    try:
        # Read the contents of the file
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of 'my_file.txt':")
            print(content)

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Read file operation completed.")

def append_to_file():
    try:
        # Append additional content to the existing file
        with open("my_file.txt", "a") as file:
            file.write("Appending another line.\n")
            file.write("Here’s one more line.\n")
            file.write("And another line with the number 99.\n")
        print("Additional lines appended successfully.")

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied when trying to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Append file operation completed.")

# Main execution flow
if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read the file again to show the updated content
