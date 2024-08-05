import os
import re

# Define the directory containing the text files
directory = '/path/to/your/directory'

# Initialize counters
total_ok_count = 0
total_ko_count = 0

# Define regex patterns for finding numbers after 'ok=' and 'ko='
ok_pattern = re.compile(r'ok=(\d+)')
ko_pattern = re.compile(r'ko=(\d+)')

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a text file
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)

        # Open and read the file
        with open(file_path, 'r') as file:
            content = file.read()

            # Find all numbers after 'ok='
            ok_matches = ok_pattern.findall(content)
            for match in ok_matches:
                total_ok_count += int(match)

            # Find all numbers after 'ko='
            ko_matches = ko_pattern.findall(content)
            for match in ko_matches:
                total_ko_count += int(match)

# Print the results
print(f'Total sum of numbers following "ok=": {total_ok_count}')
print(f'Total sum of numbers following "ko=": {total_ko_count}')