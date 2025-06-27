import os

new_folder_name = "my_new_folder"

try:
    os.mkdir(new_folder_name)
    print(f"Directory '{new_folder_name}' Created Successfully.")
except FileExistsError:
    print(f"Directory '{new_folder_name}' already exist.")
except Exception as e:
    print(f"Unexpected error occured")