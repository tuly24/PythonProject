products = ["Apples", "Bananas", "Oranges", "Milk", "Eggs"]

quantities = [10, 2, 0, 15, 4]

low_stock = []
out_of_stock = []
total_items = 0

for product, quantity in zip(products, quantities):
    total_items += quantity
    if quantity < 5:
        low_stock.append(product)
    if quantity == 0:
        out_of_stock.append(product)

print("Products that need restocking:", low_stock)
print("Products out of stock:", out_of_stock)
print("Total number of items in the store:", total_items)

