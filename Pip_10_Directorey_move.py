import os
import shutil

#---Setup:Create a Dummy file and a target direcory-----
file_to_move = "Report.pdf"
target_dir = "archives"

with open (file_to_move, 'w')as f:
    f.write("Confidential Data.")
os.makedirs(target_dir,exist_ok=True)
print(f"Created '{file_to_move}' to {target_dir}.")

#---Move the File ----

try:
    shutil.move(file_to_move,target_dir)
    print(f"'{file_to_move}' move to '{target_dir}' Successfully.")
    print(f"newpath: {os.path.join(target_dir,file_to_move)}")
except FileNotFoundError:
    print(f"file'{file_to_move}'not found.")
except Exception as e:
    print(f"unexpected error ocured: {e}")    


#----Cleanup---
if os.path.exists(target_dir):
    shutil.rmtree(target_dir)
print("Cleanup dummy Directory")