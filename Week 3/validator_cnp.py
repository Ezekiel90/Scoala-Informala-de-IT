import datetime


def validare(variabila):
    """
    :param variabila: cnp-ul introdus de utilizator de la tastatura
    :return: cnp-ul valid
    """
    while len(variabila) != 13 or variabila.isdigit() is False:
        variabila = input("Reintrodu cnp-ul: ")
    return variabila


def validare_sex(a):
    if int(a[0]) in range(1, 10):
        return True
    return False


def validare_data_nastere(cnp):
    data_nastere = cnp[1:7]
    try:
        datetime.datetime.strptime(data_nastere, '%y%m%d')
        return True
    except Exception:
        return False


def validare_judet(cnp):
    judet = int(cnp[7:9])
    if judet < 47 or judet in [51, 52]:
        return True
    return False


def validare_nnn(cnp):
    nnn = int(cnp[9:12])
    if nnn in range(1, 1000):
        return True
    return False


control = '279146358279'


def validare_cifra_de_control(cnp):
    multiply = sum([a * b for a, b in zip([int(i) for i in cnp], [int(i) for i in control])])
    if multiply % 11 == int(cnp[12]):
        return True
    elif multiply % 11 == 10 and int(cnp[12]) == 1:
        return True
    return False


def validator_cnp(cnp):
    """

    :param cnp: cnp-ul introdus de utilizator de la tastatura
    :return: mesaj "valid" in cazul in care cnp-ul este valid, "invalid" in cazul in care cnp-ul nu este valid
    """
    if cnp and validare_sex(cnp) and validare_data_nastere(cnp):
        return "Valid"
    return "Invalid"


variabila_cnp = validare(input("Introdu_CNP-ul "))
validator = validator_cnp(variabila_cnp)
print(validator)
