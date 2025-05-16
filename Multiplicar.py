import os

'''
Autor: Andy D
Fecha: 16/05/2025
Version: 1.0
Descripcion: escriba un programa que calcule la tabla de multiplicar del
numero n, desde 1 hasta m.
'''

def multiplicar():
    print("*********** TABLA DE MULTIPLICAR ***********)")
    n=int(input("Digite el numero base de la tabla: "))
    m=int(input(" Digite el limite del multiplicador: "))
    os.system("cls")
    print("---------------------------------------------")
    print(f"///////// TABLA DE MULTIPLICAR DEL 1 HASTA {n} ////////")
    for i in range(1,n-1,1):
        for j in range(1,m-1,1):
            print(f"{i} x {j} = {i*j}")
        print("\n")
    print("----------------------------------------------")
    
multiplicar()