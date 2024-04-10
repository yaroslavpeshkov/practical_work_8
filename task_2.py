number = int(input())
number_next = int(input())
friends = [number]
while number_next != (-1):
    friends.append(number_next)
    number_next = int(input())
print(len(friends))
