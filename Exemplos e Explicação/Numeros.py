age = 23 
# message = "Happy" + age +  "rd Birthday!" | ao deixarmos a idade como valor inteiro como string, devemos colocar o str(), transformando valores em string 

message = "Happy " + str(age) + "rd Birthday"
print(message)
# Dessa maneira o python sabe que vc quer converter o valor em uma string e apresenta-lo como parte da mensagem.
