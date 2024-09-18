import math 

lista_variavels = []
n = int(input("Insera quantas variavels võce quer : "))
contador = 0
while contador < n:
    i = int(input("Insira a variavel : "))
    lista_variavels += [i]
    contador += 1
    print(lista_variavels)
    
    
print (math.gcd(*lista_variavels))