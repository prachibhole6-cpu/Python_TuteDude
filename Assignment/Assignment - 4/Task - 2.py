# Function to write and append data to the file
def write_and_append_to_file():
    # Step 1: Take user input
    user_input = input("Enter some text to write to the file: ")

    # Step 2: Open the file in write mode and write the user input
    with open("output.txt", "w") as file:
        file.write(user_input + "\n")

    # Step 3: Append additional data to the file
    additional_input = input("Enter additional text to append to the file: ")
    with open("output.txt", "a") as file:
        file.write(additional_input + "\n")

    # Step 4: Read and display the final content of the file
    with open("output.txt", "r") as file:
        content = file.read()
