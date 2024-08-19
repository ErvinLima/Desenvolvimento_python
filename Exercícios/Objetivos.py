objetivos = ['praias', 'barretos', 'eua', 'nova zelandia', 'japao', 'nordeste', 'inglaterra']
quantidade = len(objetivos)

print('A quantidade de objetivos que tenho o objetivo de ir nos decorer da minha vida sao: ' + str(quantidade))
print('Esses sao os objetivos em ordem alfabetica: ')
print(sorted(objetivos))

print('o lugar que eu mais quero morar eh nos ' + objetivos[2].title())

objetivos.append('rodeio')
objetivos.insert(0, '2025')

print('No ano de ' + objetivos[0] + ' quero estar no ' + objetivos[-1] + ' que fica na cidade de ' + objetivos[2].title())

abrangente = objetivos.pop(1)
print('eu posso tirar ' + abrangente + ' da minha lista, pois os lugares que estarei indo contem ' + abrangente)

objetivos.remove('2025')


