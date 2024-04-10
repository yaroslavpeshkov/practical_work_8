number_n = int(input())
count = 0
while number_n > 0:
    x = number_n - 1
    count += 1
    print(' '*x + '*'*count)
    number_n -= 1
