

import csv

max_sales = 0
best_seller_book =  []

with open('Bestseller - Sheet1.csv' ,  'r', newline='') as file:
    csv_read = csv.reader =(file)
    next(csv_read,None)
    for row in csv_read:
        try:
            current_sales = int(row[4])
            if current_sales > max_sales:
                max_sales = current_sales
        except FileExistsError:
            print('A ocurrido un error')
        except Exception:
            print('osurrio un error')



