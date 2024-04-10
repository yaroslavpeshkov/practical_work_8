import ru_local as ru

number = int(input())
summary = 0
for i in range(1, number):
    if number % i == 0:
        summary += i
if number == summary:
    print(ru.PERFECT)
else:
    print(ru.NOT_PERFECT)
