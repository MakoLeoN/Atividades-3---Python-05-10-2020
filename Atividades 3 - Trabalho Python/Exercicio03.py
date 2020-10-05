"""Faça um programa para solicitar o nome e as duas notas e um aluno. Calcular sua média e informá-la. Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado"."""

nome = str(input("Digite o seu nome: "))
nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print ("Sua media foi: ", media)
if media >= 7:
    print("Você foi Aprovado")
else:
    if media <7:
        print("Você foi Reprovado")

