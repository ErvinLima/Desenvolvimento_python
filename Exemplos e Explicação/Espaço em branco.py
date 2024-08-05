#para remover um valor em branco na string do lado direito usa-se rstrip()

favorite_lenguage = 'python '
favorite_lenguage

# vai imprirmir este valor = 'python ', mas ao adicionarmos:
favorite_lenguage.rstrip()
# o valor final devera ficar desta maneira 'python', e para manter o valor de modo permanente deve-se deixar desta maneira:
favorite_lenguage = 'python '
favorite_lenguage = favorite_lenguage.rsplit()
favorite_lenguage

# Para remover um espaço em branco do lado esquerdo da string usa-se o lstrip()
favorite_lenguage = ' python '
favorite_lenguage.rstrip()
# ' python'
favorite_lenguage.lstrip()
# 'python '

# Para remover espaços em branco dos dois lados de uma string usa-se apenas o strip()
favorite_lenguage.strip()
# 'python'

# Essas funções de remoção são usadas com mais frequência para limpar entradas de usuário antes de armazená-las em um programa