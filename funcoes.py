#função recebe os paramentros a e b e soma eles 
def soma(a, b):
    return a + b
print(soma(5, 2))
#função recebe os paraemtros c e d multipla eles no return, e depois faz outra função chamado quadruplica que retorna a funcão multiplica coms os parametros x e 4
#que é dado o valor de x depois
def multiplica(c, d):
    return c * d

def quadruplica(x):
    return multiplica(x, 4)
print(quadruplica(10))
    