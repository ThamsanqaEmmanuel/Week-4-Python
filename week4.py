def read_and_write_file():
    #CAPTURE FILE NAME
    filename = input("Enter the name of the file to read: ")

    try:
        
        with open( filename, 'r') as file:
    
            content = file.read()

        # Modify the content
        modified_content = content.upper()

        
        output_filename = input("Enter the name of the file to write the modified content to: ")

       
        with open(output_filename, 'w') as output_file:
            
            output_file.write(modified_content)
        
        print(f"File was successfully read and written to {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_file()
