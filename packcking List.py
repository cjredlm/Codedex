
import csv  

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]


try:
    with open('packing_list.csv','r', newline='') as file:
     csv_read = csv.reader(file)
    for row in csv_read:
            print(row)
except FileNotFoundError:
      print('El archivo fallo')
except Exception as e:
      print(f"Ocurrió un error: {e}")



     


