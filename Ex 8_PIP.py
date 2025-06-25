import os



new_directory = "./Test-repo2"
print(os.path.basename)
if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory)
    print(f"Changed directory to:{os.getcwd()}")
else:
    print(f"Directore '{new_directory} does not exist or is not a directory")