import subprocess
import os
import re

# Define the paths
paths_file = 'paths.txt'
script = './rebuild.sh'
output_directory = 'output_logs'

# Function to sanitize the path to create a valid filename
def sanitize_filename(path):
    # Replace any non-alphanumeric characters with an underscore
    sanitized = re.sub(r'[^a-zA-Z0-9]', '_', path)
    return sanitized

# Read paths from the file
with open(paths_file, 'r') as file:
    paths = [line.strip() for line in file.readlines()]

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Run the script for each path and save the output
for path in paths:
    sanitized_path = sanitize_filename(path)
    output_file_path = os.path.join(output_directory, f'output_{sanitized_path}.txt')
    try:
        # Run the script and capture the output
        result = subprocess.run([script, path], capture_output=True, text=True, check=True)
        # Write the output to the file
        with open(output_file_path, 'w') as output_file:
            output_file.write(result.stdout)
    except subprocess.CalledProcessError as e:
        # If there's an error, write the error message to the file
        with open(output_file_path, 'w') as output_file:
            output_file.write(f'Error occurred while running the script for path {path}\n')
            output_file.write(e.stderr)

    print(f'Output for path {path} written to {output_file_path}')

