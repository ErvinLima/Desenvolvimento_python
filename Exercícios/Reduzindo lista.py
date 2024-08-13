convidados = ['luigi', 'pedro', 'anthony', 'danilo', 'andre', 'vitoria', 'gabi', 'lindsay', 'carlos cadu']

convidados[4] = 'igor'
convidados.insert(7, 'joao')
convidados.insert(9, 'bryan')
convidados.append('bruno')

print('Pessoal infelizmente a mesa que incomendei nao chegara a tempo para acomodar todos os convidados, a lista atualizada ainda sera enviada logo.')

convidado_1 = convidados.pop(11)
convidado_2 = convidados.pop(10)
convidado_3 = convidados.pop(9)
convidado_4 = convidados.pop(7)
convidado_5 = convidados.pop(6)
convidado_6 = convidados.pop(5)
convidado_7 = convidados.pop(4)
convidado_8 = convidados.pop(3)
convidado_9 = convidados.pop(2)
convidado_10 = convidados.pop(1)

print('\n' + convidado_1.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_2.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_3.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_4.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_5.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_6.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_7.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_8.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_9.title() + ' infelizmente nao poderei estar lhe convidando para meu jantar.')
print(convidado_10.title() + ' infelizmente nao poderei estar lhe convidadndo para meu jantar.')

print('\n' + convidados[0] + ' voce ainda continua na lista de convidados para o jantar.')
print(convidados[1] + ' voce ainda continua na lista de convidados para o jantar.')

del convidados[0]
del convidados[0]
print(convidados)