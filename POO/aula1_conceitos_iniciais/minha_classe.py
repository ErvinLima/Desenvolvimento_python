class MinhaClasse: 
# Dentro desse metodo vamos definir nossos atributos em si
    def __init__(self, info, elem): # Metodo construtor
        self.atributo_1 = "meu atributo"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "a"]
        self.novo_atributo = info
        print(self.novo_atributo)

#como primeira propriedade e indicando que esse metodo esta dentro da minha classe coloco a palavra SELF reservada dentro do metodo_1, 
    def metodo_1(self):
        print("minha acao 1")
        print("minha acao 2")
        print(self.atributo_2)
        return "ola mundo"

# sempre coloque o self tanto nos atributos quanto nos metodos, para indicar que estamos dentro da classe 
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[1] + numero)


# obejeto        # classe -> a partir de uma classe eu posso instanciar um objeto
minha_classe = MinhaClasse('retorno do meu novo atributo', 231)

minha_classe.metodo_2(3)
