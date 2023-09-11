#2. Escreva um programa que crie uma tupla com os meses do ano. Em seguida, peça ao usuário para 
#digitar um número de 1 a 12 e retorne o mês correspondente.

meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
num_user = int(input("Digite um número e consulte o mês: "))
num_system = num_user - 1
if num_user > 0 and num_user <= 12:
    print(f"O Mês do numero {num_user} é {meses[num_system]}")
else:
    print(f"[ERROR] NUM {num_user} NÃO POSSUI MÊS ATRIBUIDO")