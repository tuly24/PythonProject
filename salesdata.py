sales = [250, 400, 150, 700, 300, 500, 600]

sales.append(450)
print("After adding $450:", sales)

total_sales = sum(sales)
print("Total sales: $", total_sales)

highest_sales = max(sales)
lowest_sales = min(sales)
print("Highest sales: $", highest_sales)
print("Lowest sales: $", lowest_sales)

average_sales = total_sales / len(sales)
print("Average daily sales: $", round(average_sales, 2))

sales.remove(150)
print("After removing $150:", sales)

sales.sort()
print("Sorted sales data:", sales)

high_sales_days = sum(1 for sale in sales if sale > 500)
print("Days with sales > $500:", high_sales_days)

sales.reverse()
print("Sales in descending order:", sales)
