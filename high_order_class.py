import csv

with open('zomato.txt', 'r') as order_item:
    csv_orders = csv.DictReader(order_item,delimiter=',')
    print(csv_orders)
    print(order_item.read())
   