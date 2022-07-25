def validare_variable(variabila):
    while variabila.isdigit() is False:
        variabila = input("Reintrodu numarul: ")
        return int(variabila)


def validare_operator(op):
    if op in ['+', '-', '*', '/']:
        op = input('Reintrodu numarul: ')
    return op


def calculator(a, b, c):
    """
    :param a: primul nr
    :param b: al doilea nr
    :param c: operatorul (+, -, *, /)
    :return: calculeaza operatia dintre doua numere
    """

    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    else:
        while b == 0:
            b = input('eroare')
        return a / b


primul_numar = validare_variable(input("Numar:"))
al_doilea_numar = validare_variable(input("Numar:"))
operator = validare_operator(input("Operator:"))
total = calculator(primul_numar, al_doilea_numar, operator)
print(f"Rezultatul este: {total}")
