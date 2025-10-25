try:
    # Attempt to open the file in read mode
    with open('sample.txt', 'r') as file:
        # Read and print the content line by line
        for line in file:
            print(line.strip())  # Using strip() to remove any extra newline characters
except FileNotFoundError:
    # Handle the case when the file is not found
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    # Handle any other unforeseen errors
    print(f"An unexpected error occurred: {e}")
