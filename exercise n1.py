#1. Crie um programa que solicite ao usuário uma lista de números inteiros e retorne a soma de todos os 
#elementos da lista.

numbers = []
resp = "s"
soma = 0
while resp == "s":
    num = int(input('Digite um número: '))
    soma += num
    numbers.append(num)
    resp = input("Deseja continuar: [s/n]")
print(f"{numbers} a soma destes números é {soma}")