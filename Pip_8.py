import os

file_to_delete = "my_temp_file.txt"

with open(file_to_delete, 'w') as f:
    f.write("This is temporry file.")
    print(f"File '{file_to_delete}' write successfully.")

try:
    os.remove(file_to_delete)
    print(f"File '{file_to_delete}'Removed Successfully.")
except FileNotFoundError:
    print(f"file'{file_to_delete}'not found.")
except Exception as e:
    print(f"Unexpected error occured:{e}")