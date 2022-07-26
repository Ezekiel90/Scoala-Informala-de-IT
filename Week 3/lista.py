list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

def split_list(list):
    odd_numbers = [number for number in list if number % 2 == 1]
    even_numbers = [number for number in list if number % 2 == 0]
    divisible_by_three = [number for number in list if number % 3 == 0]
    return odd_numbers, even_numbers, divisible_by_three
print("The odd numbers are {}".format(split_list(list)[0]))
print("The even numbers are {}".format(split_list(list)[1]))
print("The numbers divisible by three are {}".format(split_list(list)[2]))

# even_numbers = list(filter(lambda x: x%2 ==0, lista))
# uneven_numbers = list(filter(lambda x: x%2 != 0, lista))
# divisible_by_three = list(filter(lambda x: x%3 ==0, lista))
#
# print(even_numbers)
# print(uneven_numbers)
# print(divisible_by_three)

# for num in list
#     if num % 2 == 0:
#         print (num, end=" ")
#
#
# for num in list:
#     if num % 2 != 0:
#         print (num, end=" ")


# def get_even_numbers(list):
#     even_numbers = []
#
#     for number in list:
#         if number % 2 == 0:
#             even_numbers.append(number)
#
#     return even_numbers
#     list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
#     print(get_even_numbers(list))
