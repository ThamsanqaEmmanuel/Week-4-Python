#reading the file and printing it's contents
try:
    #Reading existing file
    filename = input("Enter the name of the file you want to read:")
    with open(filename, "r") as file:
        data = file.read()
        print(data) 
#Creating and writing a new file
    filename2 = input("Enter the name of the new file you want to create:")
    new_content = input("Enter the new content you want to add:")
    with open(filename2, 'w') as file:
        new_file = data + '\n' + new_content
        file.write(new_file)
    print(f"created successfully {new_file}")
except FileNotFoundError: 
    print("File was not found")
