valor = input('Digite algo:')
print('O tipo primitivo dessa valor é: {}'.format(valor.__init_subclass__()))
print('Só tem espaços? {}'.format(valor.isspace()))
print('É um número? {}'.format(valor.isnumeric()))
print('É alfabético? {}'.format(valor.isalpha()))
print('É alfanumérico? {}'.format(valor.isalnum()))
print('Esta em maiúsculas? {}'.format(valor.isupper()))
print('Esta em minúsculas? {}'.format(valor.islower()))
print('Esta capitalizada? {}'.format(valor.istitle()))
