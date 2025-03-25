import os

# List of files to check
files_to_check = [
    'alx_travel_app/requirement.txt',
    'alx_travel_app/settings.py',
    'alx_travel_app/urls.py'
]

# Function to check if a file exists and is not empty
def check_file(file_path):
    if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
        print(f"The file '{file_path}' exists and is not empty.")
    else:
        print(f"The file '{file_path}' either does not exist or is empty.")

# Check each file
for file in files_to_check:
    check_file(file)
