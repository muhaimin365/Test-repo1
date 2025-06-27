import os

old_name= "Old_file.text"
new_name = "New_file.txt"

with open(old_name,'w') as f:
    f.write("This is Olde File")

try:
    os.rename(old_name,new_name)
    print(f"Rename '{old_name}' to '{new_name}'.")
except FileNotFoundError:
    print(f"file'{old_name}'not found.")
except FileExistsError:
    print(f"File '{new_name}' already exist.")
except Exception as e:
    print(f"unexpected error ocured: {e}")