# Usaremos o laço de repetição FOR para percorrermos todos os itens da lista, independente do seu tamanho e caso mais elementos sejam acrescentados

magicians = ['alice', 'david', 'carolina']

# ao definirmos o laco, ele diz pra linguagem extrair um nome da lista e armazena-lo na variavel MAGICIAN
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see yout next trick, " + magician.title() + "\n")
# conforme colocado duas instruções print, cada linha sera executada uma vez para cada magico da lista 

print("Thank you everyone. That was a great magic show!")