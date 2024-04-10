number = int(input())
number_next = int(input())
while number_next != (-1):
    if number_next > number:
        number = number_next
    number_next = int(input())
print(number)
