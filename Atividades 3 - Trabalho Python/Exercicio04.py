"""Faça um programa que leia dois números e mostre qual o maior dos dois. O programa deve informar caso sejam iguais."""

num1 = float(input("Digite um Número: "))
num2 = float(input("Digite um Número: "))
igual = num1==num2
if num1>num2: 
    print("Este número é o maior: ",num1)
else:
    if num1<num2:
        print("Este número é o maior: ", num2)

if igual:
    print("Estes números são iguais")

      