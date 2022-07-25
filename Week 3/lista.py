lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

even_numbers = list(filter(lambda x: x%2 ==0, lista))
uneven_numbers = list(filter(lambda x: x%2 != 0, lista))
divisible_by_three = list(filter(lambda x: x%3 ==0, lista))

print(even_numbers)
print(uneven_numbers)
print(divisible_by_three)