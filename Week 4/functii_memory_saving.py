element = lambda x: x * 10

element_2 = lambda x, y: x + y

""" FILTER """

list_1 = (1, 5, 4, 6, 8, 11, 3, 12)
list_2 = filter(lambda x: (x % 2 == 0), list_1)
print(list_2)