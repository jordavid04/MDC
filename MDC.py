import math #biblioteca de funcoes matematicas

lista_variavels = []  #lista com os valores armazenados

#lista com os valores armazenados
n = int(input("Insera quantas variavels võce quer : "))
contador = 0

#sistema de repeticao
while contador < n:              
    i = int(input("Insira a variavel : "))
    lista_variavels += [i]
    contador += 1
    print(lista_variavels)
    
#Resultado do MCD     
print (math.gcd(*lista_variavels))