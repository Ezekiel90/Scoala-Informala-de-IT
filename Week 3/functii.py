# print("Ana are mere")
# var1 = input("Adauga un numar: ")
# print(var1)
# numar_mere = 3
# numar_pere = 2
# var1 = "Ana are {0} mere si {1} pere".format(numar_mere, numar_pere)
# var1 = "Ana are '3' mere"
# print(var1)


# def my_function(a:int, b:int = 0, c:int = 0, *args) -> (int, dict):
#    return a + b + c, {'diferenta': a - b - c}


# suma = my_function(b=10, a=5)
# suma, diferenta = my_function(4, c=3, b=2,)
# print(suma, diferenta)

# def suma(a, b, *args, **kwargs):
    """
    :param a:
    :param b:
    :param args:
    :param kwargs:
    :return:
    """
    total = 0
    variabila_temp = a + b
    for i in args:
        total = total + i # total += i
    print(type(kwargs))
    for i, v in kwargs.items():
        print(i, v)
        total = total + v
    return variabila_temp + total

# variabila = suma(1, 2, 3, 4, 5, c=4, d=7, e=9)
# print (variabila)

my_var = input('Adauga un numar: ')
try:
    my_int = my_var
except Exception as e:
    print('exceptie', e)

else:
    print('nu sunt exceptii')
