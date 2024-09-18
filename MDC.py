#biblioteca de funcoes matematicas
import math 

#lista com os valores armazenados

lista_variavels = []  

#contador e quantidade de variavels
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
