import csv

inventory=[
    {"id":"p001", "name":"leptop", "price":"100000", "stock":10},
    {"id":"p002", "name":"mouse", "price":"1500", "stock":50},
    {"id":"p003", "name":"keyboard", "price":"2000", "stock":250},
    {"id":"p004", "name":"monitor", "price":"8000", "stock":70}
]

print ("initial inventory")

for product in inventory:
    print(f"ID:{product['id']}, Name:{product['name']}, Price:{product['price']}, Stock:{product['stock']}")


def update_stock(product_id,quantity):

    found = False
    for product in inventory:
        if product['id']==product_id:
            if product['stock']>=0:
                product=product['stock']+quantity
                print(f"updated Stock for: {product['name']}(ID:{product_id}).New stock{product['stock']}")
            else:
                print(f"Nostock for :{product['name']}")
            found = True
            break
    if not found:
        print(f"Error product with ID: {product['name']}(ID{product['id']})")


def get_low_stock_product(threshold):
    """ Returns:
    list : Alist of names of product with low stock."""

    low_stock_product =[]
    for product in inventory:
        if product['stock']<threshold:
            low_stock_product.append(product['name'])
    return low_stock_product

csv_file_name = "product1.csv"
fieldnames = ["id","name","price","stock"]

if __name__ == "__main__":

    try:
        Low_Stock = get_low_stock_product(100)
        print(f"You entered a low stock product: {Low_Stock}")
        with open(csv_file_name, mode='w',newline='') as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
            #write the header Row
            writer.writeheader()
            print("CSV Header written.")
            #write all product data rows
            writer.writerows(inventory)
            print(f"Successfully wrote{len(inventory)} product records to '{csv_file_name}' ")

    except IOError as e:
        print(f"Error:  Couldn't write to the file'{csv_file_name}'.{e}")

    except Exception as e:
        print(f"Unexcpected Eroor Occured:{e}")

