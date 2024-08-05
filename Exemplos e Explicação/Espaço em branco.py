# Como remover um valor em branco na string:
favorite_lenguage = 'python '
favorite_lenguage
# vai imprirmir este valor = 'python ', mas ao adicionarmos rstrip() para remover o espaco em branco do lado direito, fica assim:

favorite_lenguage.rstrip()
# o valor final devera ficar desta maneira 'python', e para manter o valor de modo permanente deve-se deixar desta maneira:

favorite_lenguage = 'python '
favorite_lenguage = favorite_lenguage.rstrip()
# o valor impresso devera ser 'python'

# Para remover um espaço em branco do lado esquerdo da string usa-se o lstrip()
favorite_lenguage = ' python '
favorite_lenguage = favorite_lenguage.lstrip()
# o valor impresso devera ser 'python '

# Para remover espaços em branco dos dois lados de uma string usa-se apenas o strip()
favorite_lenguage = ' python '
favorite_lenguage = favorite_lenguage.strip()
# o valor impresso devera ser 'python'

# Essas funções de remoção são usadas com mais frequência para limpar entradas de usuário antes de armazená-las em um programa