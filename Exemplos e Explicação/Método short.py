# é um método que faz com que seja relativamente facil ordenar uma lista

cars = ['bmw', 'audi', 'toyota', 'subaro']

# o metodo altera a ordem da lista de fomra permanente alfabeticamente, a forma de como forem ordenados nao pode voltar a sua ordem original
cars.sort()
print(cars)

# da mesma maneira que esta em ordem alfabetica conseguimos colocas em ordem contraria incluindo o seguinte comando:
cars.sort(reverse=True)
print(cars)
