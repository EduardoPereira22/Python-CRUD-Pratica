#soma entre duas variaveis
x = 20
y = 30
j= x + y
print(j)

#printar sring
nome ="Eduardo Pereira"
print(nome)

#procurar o indice do u na variavel nome
nome.find("u")

print(nome.find("u"))

#quantas vezes o elemento E tem no nome
print(nome.count("E"))
#Procurar o elemento no indice 4
print(nome[4])

#definindo a variavel
Pernambuco = ["Recife", "Jaboatão", "Abreu-e-lima"]
#procurando o indice de jaboatão na lista
print(Pernambuco.index("Jaboatão"))
#adicionando candeias na lista
Pernambuco.append("Candeias")

print(Pernambuco)
#botando a lista ao contrario
Pernambuco.reverse()

print(Pernambuco)

# se for verdadeiro prinar oi
if True:
    print("oi")

idade = 18
#usando o if para ver se a informação pe verdadeira
if idade >= 18:
    print("você é maior de idade")
else:
    print("você é menor de idade")

comida = "boa"
preçodacomida = "barato"

if comida == "boa" and preçodacomida == "barato":
    print("a comida vale a pena")
elif comida == "ruim" and preçodacomida == "barato":
    print("a comida vale um pouco a pena")
elif comida == "boa" and preçodacomida == "caro":
    print("talvez vale a pena")
else:
    print("a comida não vale a pena")


cidades = ['Porto de galinhas','Carneiros','Tamandare']
#printando a lista de cidade e usando o template string para completar o texto
for cidades in cidades:
    print("praias boas é em {cidades}!")
#usando o for e o in range para fazer a contagem que vai ate o 8 como esta definido no in range
for i in range(8):
    print(i)
#usando o for e o in range para definir no parentese o 10 é a posição incial , o 16 é o final e o 2 é a contagem de 2 em 2
for u in range(10,16,2):
    print(u)
#botando o indice em cada item da lista cidade "rever isso"
for idx, cidade in enumerate(cidades):
    print(idx, cidade)
#enquanto for True vai printar hello, mas tem que se usar o break pra não se tornar ifinito
while True:
    print("Helllo")
    break
#enquanto x for menor de que 10 ele vai adiconando um no x +=1
x=0
while x < 10:
    print(x)
    x +=1
#usa-se o try esperando que algo funcione ou não e existe excepet para tratar erro ,sem que ele pare o servidor

try:
    x = 1/0
except:
    print("error")

#usando o raise para parar o servidor quando der erro junto com a mensagem de erro do except deixei comentado para nao parar o servidor

#try:
    #x = 1/0
#except:
    #print("error")
    #raise


#mesmo uso do try com o else caso der certo e o uso do finally ele semre executa se der erro ou não

try:
    x = 10
except:
    print("error")
else:
   print("Deu Certo")
finally:
    print("sempre executa")


