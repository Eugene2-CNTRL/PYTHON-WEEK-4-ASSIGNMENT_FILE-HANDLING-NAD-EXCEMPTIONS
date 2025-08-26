def modify_content(content):
    # convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except (FileNotFoundError, IOError):
        print("The file doesn't exist or cannot be read.")
        return
    
    modified_content = modify_content(content)
    
    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as file:
            file.write(modified_content)
        print(f"Modified content written to {new_filename}")
    except IOError:
        print("Failed to write to the new file.")

if __name__ == "__main__":
    main()
