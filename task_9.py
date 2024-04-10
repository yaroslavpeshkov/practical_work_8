number_n = int(input())
for i in range(2, number_n):
    divider = 2
    while i % divider != 0:
        divider += 1
    if divider == i:
        print(i)
