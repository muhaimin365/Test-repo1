import csv


product_data = [ 
    {"id":"A1", "name":"leptop", "price":"100000", "stock":10},
    {"id":"A2", "name":"mouse", "price":"1500", "stock":50},
    {"id":"A3", "name":"keyboard", "price":"2000", "stock":250},
    {"id":"A4", "name":"monitor", "price":"8000", "stock":70}
]

csv_file_name = "product1.csv"

fieldnames = ["id","name","price","stock"]

try:
    with open(csv_file_name, mode='w',newline='') as csv_file:
       writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        #write the header Row
       writer.writeheader
       print("CSV Header written.")
       #write all product data rows
       writer.writerows(product_data)
       print(f"Successfully wrote{len(product_data)} product records to '{csv_file_name}' ")

except IOError as e:
    print(f"Error:  Couldn't write to the file'{csv_file_name}'.{e}")
except Exception as e:
    print(f"Unexcpected Eroor Occured:{e}")


 
       

