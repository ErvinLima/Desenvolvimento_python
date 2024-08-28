class Pessoa:
    def __init__(self, andar, nome):
        self.altura = 1.80
        self.idade = 20
        self.parque = andar
        self.name = nome

    def info(self):
        print(self.altura)
        print(self.idade)
        print(self.name)

    def correr(self):
        print(self.parque)
        print("essa pessoa consegue correr mais de 5km sem perder o ritmo.")
        return "essa sao as informacoes dessa pessoa"
    
    def comer(self, comida):
        self.correr()
        print("a comida favorita dessa pessoa eh: " + comida)


minha_classe = Pessoa("andar no parque ao por do sol, traz uma sensacao de paz", 'ervin')
minha_classe.comer("japonesa")

response = minha_classe.correr()
print(response)
