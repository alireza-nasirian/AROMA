import os

# Define the directory containing the text files
directory = '/path/to/your/directory'

# Initialize counters
count_no_ok_or_ko = 0

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)

        # Open and read the file
        with open(file_path, 'r') as file:
            content = file.read()

            # Check if 'ok=' and 'ko=' are in the file
            if 'ok=' not in content and 'ko=' not in content:
                count_no_ok_or_ko += 1

# Print the result
print(f'Number of unsuccessful builds=": {count_no_ok_or_ko}')