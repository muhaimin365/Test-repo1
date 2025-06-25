import json
import datetime

product_data = {

    "product":[
        {"id":"A1", "name":"leptop", "price":"100000", "stock":10},
        {"id":"A2", "name":"mouse", "price":"1500", "stock":50},
        {"id":"A3", "name":"keyboard", "price":"2000", "stock":250},
        {"id":"A4", "name":"monitor", "price":"8000", "stock":70}
    ],
    "last_updated":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%M")


}

json_file_name = "product.json"

print(f"Attempting to write product data to '{json_file_name}'...")

try:
    with open(json_file_name,mode='w',encoding='utf-8') as json_file:
        json.dump(product_data,json_file, indent = 4)
        print(f"Successfully wrote product data to {json_file_name}.")

except IOError as e:
    print(f"Error:  Couldn't write to the file'{json_file_name}'.{e}")
except Exception as e:
    print(f"Unexcpected Eroor Occured:{e}")

print(f"\nPlease check the '{json_file_name} 'file manually in a text editor to verify its content' ")

