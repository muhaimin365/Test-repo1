import os

full_path="/Muhaimin/Test-repo1/test1.txt"

directory_name =os.path.dirname(full_path)
basename= os.path.basename(full_path)
print(f"Directory name: {directory_name}")
print(f"Basename: {basename}")
