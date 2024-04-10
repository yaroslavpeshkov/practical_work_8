revenue = int(input())
revenue_next = int(input())
count = 1
while revenue_next != 0:
    revenue += revenue_next
    count += 1
    revenue_next = int(input())
average_revenue = revenue / count
print(average_revenue)
