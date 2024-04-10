import ru_local as ru

number = input(ru.INPUT)
while not number.isdigit():
    number = input(ru.MISTAKE)
print(f'{ru.RIGHT}{number}')
