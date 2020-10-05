"""Elabore um programa para solicitar o nome de uma equipe de futebol, a quantidade de derrotas, empates e vitórias obtidas por ela no campeonato. No futebol, cada vitória vale três pontos e cada empate vale um ponto. Calcular e informar: a quantidade de pontos ganhos, a quantidade de pontos perdidos e o percentual de aproveitamento da equipe"""

nomeT = str(input("Digite o nome do time: "))
valorV = int(input("Quantidade de Vitorias: "))
valorE = int(input("Quantidade de Empates: "))
valorD = int(input("Quantidade de Derrotas: "))
valorPG = valorV *3 + valorE
valorPP = valorD *3 % valorV 
total = valorV + valorE 
percentual = total/100*100
print("Pontos Ganhos: ", (valorPG))
print("Pontos Perdidos: ", (valorPP))
print("O percentual de aproveitamento do time foi de: ", percentual, "%")
