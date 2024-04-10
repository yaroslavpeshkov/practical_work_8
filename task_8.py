numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = ''
for i in numbers:
    x += str(i)
    print(f'{x} * 8 + {i} = {int(x) * 8 + i}')
x = ''
for i in numbers:
    x += str(i)
    print(f'{x} * 9 + {i+1} = {int(x) * 9 + (i+1)}')
for i in numbers:
    x = '1'
    x *= i
    print(f'{x} * {x} = {int(x)*int(x)}')
