#Utilizando alguma estrutura de loop, imprima todos os número de 0 até 100; +feito
#Modifique o código do item anterior para imprimir apenas os números pares. Note que o resto da divisão de um número par por 2 é igual a zero, algo que o operador modulo “%” pode te retornar; feito
#Utilize o seguinte código para criar uma lista com 100 números aleatórios:
#rom random import randint
#lista = [randint(1, 100) for _ in range(100)]

#Com um loop for, imprima:
#Todos os números da lista;
#Todos os números maiores que 10 da lista;
#Todos os números maiores que 10 e menores que 30 da lista;
#O dobro de todos os números que forem menores que 50;

#Utilizando de um loop while, conte:
#Quantos números ímpares possui a lista;
#Quantos números maiores que 50;
#Quantos número menores que 50;



#printando um numero de 0 a 100
for a in range(101):
    print(a)
#printando um numero que começa com 0 termina ate 100 pq antes do 1001 ele para e de 2 em 2, ou seja par
for u in range(0,101,2):
    print(u)

#randomizando numeros de 1 a 100 no radint e usando o for _ que fala não fazer nada e o in range mostrando 100 numeros
from random import randint
lista = [randint(1, 100) for _ in range(100)]
print(lista)
#usando o for para pegar so os numeros maior que 10 na lista acima
novalista = [lista for lista in lista if lista > 10]
print(novalista)
#usando o for para pegar os numeros maior que 10 e menor que 30 da lista randomizada
novalista2 = [numero for numero in lista if 10 < numero < 30]
print(novalista2)
#usando o for para mutiplicar por 2 os numeros menores que 50
novalista3 =[numero for numero in lista if numero < 50 * 2]
print(novalista3)



#usando o while
from random import randint
lista = [randint(1, 100) for _ in range(100)]
listawhile = [numero while numero in lista if]

#while lista % 2 !=0:
 #   print(lista)













