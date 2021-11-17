import csv
items = []
with open('product_data.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        items.append(row)
        break

print(items)
