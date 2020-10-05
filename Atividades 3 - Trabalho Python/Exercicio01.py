"""Faça um programa que dado o valor da temperatura em graus FARENHEIT, calcular
e escrever o valor da temperatura em graus CELSIUS.
Fórmula: C = 5/9 * (F - 32)"""

grauFah = int(input("Digite o grau em farenheit: "))
Celsius = (grauFah - 32) * 5//9
print("A temperatura em graus celsius é: ", Celsius, "ºc")
