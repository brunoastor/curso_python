#Crie um programa que leia os catetos de um triangulo retangulo e calcule a hipotenusa

from math import pow, sqrt

ca1 = float(input('informe o valor do cateto a: '))
ca2 = float(input('informa o valor do cateto b: '))
valor = (pow(ca1, 2)+pow(ca2, 2))
valor = sqrt(valor)
print('Hipotenusa: {}' .format(valor))
