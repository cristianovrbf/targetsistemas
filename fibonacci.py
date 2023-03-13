entrada = int(input("Digite um valor de entrada: "))
aux = 0
cont = aux + 1
lista = [aux, cont]
while (cont <= entrada):
    cont = cont + aux
    aux = cont - aux
    lista.append(cont)

if (aux == entrada):
    print("O valor informado, pertence a sequência de Fibonacci!")
else:
    print("O valor informado, não pertence a sequência de Fibonacci!")