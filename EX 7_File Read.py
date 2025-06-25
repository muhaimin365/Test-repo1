import csv

csv_file_name = "product1.csv"

#defining the target filtered value
target_section = "leptop"

print(f"Attempting to read product data from'{csv_file_name}' and filter by '{target_section}'")

filtered_product=[]

try:
    with open(csv_file_name, mode='r',newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row.get('name')==target_section:
                filtered_product.append(row)
    print(f"Filtered product list: {filtered_product} ")
    print(f"\n...Employees un the '{target_section}' name....")


except FileNotFoundError as e:
    print(f"Error:  The file '{csv_file_name}'couldn't found. please type correct file name.{e}")
except Exception as e:
    print(f"Unexcpected Eroor Occured:{e}")