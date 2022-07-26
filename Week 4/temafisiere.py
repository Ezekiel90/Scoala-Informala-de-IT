import csv
import datetime


def introducere_categorii():
    while True:
        with open('categorii.txt', 'a') as file:
            file.write(f'{input("Adauga categoria: ")} \n')
        decizie = input('Doriti sa introduceti o alta categorie? (Y/N)')
        print(decizie)
        if decizie.lower() == 'n':
            break
    return True


# introducere_categorii()


def introducere_taskurilor():
    while True:
        with open('taskuri.csv', 'a') as file:
            csv_writer = csv.writer(file, delimiter=',')
            task = input('Adauga un task: ')
            data_limita = input('Adauga o data limita: ')
            responsabil = input('Adauga persoana responsabila: ')
            categoria = input('Adauga o categorie: ')
            with open('categorii.txt', 'r') as file:
                line = file.readlines()
            verificare = categoria.strip()
            new_list = [item.strip() for item in line]
            if verificare not in new_list:
                introducere_categ = input('Reintrodu categoria: ')
                if introducere_categ in line:
                    break
                print('Categorie inexistenta ')
            csv_writer.writerow([task, data_limita, responsabil, categoria])
        decizie = input('Doriti sa introduceti un alt task (Y/N)')
        print(decizie)
        if decizie.lower() == 'n':
            break
    return True


introducere_taskurilor()
