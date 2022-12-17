from collections import defaultdict, Counter
#Dando dados ao dicionario
dados = {"nome": "eduardo",
"curso": "Python",
"escola": "Tera",
"idade": 31,
"cidade": "Recife",

}
#acessando os valores no dicionario
print(dados["nome"])
print(dados["escola"])
print(dados["cidade"])

#dando um novo valor a cidade
dados["cidade"] = "jaboatão Dos Guararapes"

print(dados["cidade"])

print("cidade" in dados)

#adicionando novas chaves e valores
dados.update({"comida favorita":"pizza", "hobbies":"jogar"}
)
print(dados)

#pegando todas as chaves no dicionario 
print(dados.keys())

#retornar todos os valores no dicionario
print(dados.values())

#retornar pares de chaves e valor
print(dados.items())


