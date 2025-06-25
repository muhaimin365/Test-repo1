import os


path_c1="C://Muhaimin"
path_c2="Test-repo2"
file_name="Monthly_Report.pdf"

full_path = os.path.join(path_c1,path_c2,file_name)
print(f"joind path:{full_path}")