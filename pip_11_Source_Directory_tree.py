import os
import shutil

#---Setup:Create a Dummy source dirctory tree
source_dir ="my_source_project"
os.makedirs(os.path.join(source_dir,"css"),exist_ok=True)
os.makedirs(os.path.join(source_dir,"js"),exist_ok=True)
with open(os.path.join(source_dir,"index.html"),'w') as f:
    f.write("<html></html>")
with open(os.path.join(source_dir,"css","style.css"),'w') as f:
    f.write("body{}")
print(f"Created dummy source directory: '{source_dir}'.")

#----Copy the Directory tree -----
destination_tree = "my_backup_project"
try:
    #if destination_directory already exist and is not empty, copy tree will raise an error.
    #To overwrite, you'd typically remove the desination first or handle more complex
    shutil.copytree(source_dir,destination_tree)
    print(f"'{source_dir}' copy to '{destination_tree}' Successfulyy copied.")
    print("Contented of destionation tree")
    for root,dirs,files in os.walk(destination_tree):
        level = root.replace(destination_tree,'').count(os.sep)
        indent =''*4*(level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' *4*(level+1)
        for f in files:
            print(f"{subindent}{f}")

except FileExistsError:
    print(f"Directory '{destination_tree}' already exist.")
except Exception as e:
    print(f"Unexpected error occured")

#----Clean UP ----
if os.path.exists(source_dir):
    shutil.rmtree(source_dir)
if os.path.exists(destination_tree):
    shutil.rmtree(destination_tree)
print("Sucessfully Cleenedup")
