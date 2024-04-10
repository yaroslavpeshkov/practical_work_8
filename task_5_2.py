number_n = int(input())
count = 0
for i in range(2, number_n):
    summary = 0
    for j in range(1, i):
        if i % j == 0:
            summary += j
    if i == summary:
        count += 1
print(count)
