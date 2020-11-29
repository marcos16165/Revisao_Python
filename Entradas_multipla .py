
#Armazenando entrada(escolhida pelo usuário) em uma lista 

x = int(input("Digite a quantidade de entradas: "))

lista = [int(input()) for i in range(x)]

for i in lista:
    print(i)

