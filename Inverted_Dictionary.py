# Function to read the dictionary from a file
def read_dictionary(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Convert file content into a dictionary
            original_dict = eval(content)
            return original_dict
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except SyntaxError:
        print(f"Error: The file '{file_path}' is not correctly formatted.")
        return None

# Function to invert the dictionary
def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        # Handle single or multiple values for each key
        values = value.split(", ") if isinstance(value, str) else [value]
        for val in values:
            inverted_dict.setdefault(val, []).append(key)
    return inverted_dict

# Function to write the inverted dictionary to a file
def write_dictionary(file_path, dictionary):
    try:
        with open(file_path, 'w') as file:
            file.write(str(dictionary))
        print(f"Inverted dictionary successfully written to '{file_path}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Main program
input_file = "input_dict.txt"
output_file = "output_dict.txt"

# Read the dictionary from the input file
original_dict = read_dictionary(input_file)

if original_dict:
    # Invert the dictionary
    inverted_dict = invert_dictionary(original_dict)
    
    # Write the inverted dictionary to the output file
    write_dictionary(output_file, inverted_dict)
