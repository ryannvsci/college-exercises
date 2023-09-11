#3. Crie um programa que solicite ao usuário duas listas de números inteiros e crie dois sets com 
#essas listas. Em seguida, determine e exiba os números que estão presentes nos dois sets (interseção).

fim_lista = 1
lista1 = []
lista2 = []
while fim_lista != 2:
    fim_lista = int(input("Deseja inserir numero na lista 1? | 1 = Sim | 2 = Não: "))
    if fim_lista == 1:
        num_int = int(input("Insira número inteiro para lista: "))
        lista1.append(num_int)
    elif fim_lista == 2:
        print("Lista 1 finalizada!")
    else:
        print("ERRO OPÇÃO NÃO DISPONÍVEL")
print("HORA DA LISTA 2!")
fim_lista = 1
while fim_lista != 2:
    fim_lista = int(input("Deseja inserir numero na lista 2? | 1 = Sim | 2 = Não"))
    if fim_lista == 1:
        num_int = int(input("Insira número inteiro para lista: "))
        lista2.append(num_int)
    elif fim_lista == 2:
        print("Lista 1 finalizada!")
    else:
        print("ERRO OPÇÃO NÃO DISPONÍVEL")

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
analise1 = set(lista1)
analise2 = set(lista2)
print(f"Os números iguais na lista de inteiros são :{analise1.intersection(analise2)}")