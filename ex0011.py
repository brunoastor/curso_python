#Leia a altura e a largura de uma parede e calcule a quantidade de tinta para pinta-la, cada m² nescessita de 1l de tinta

base = float(input('Informe a Base da parede: '))
altura = float(input('Informe a Altura da parede: '))
print('Area da Parede: {}\nQuantidade de Tinta: {:.0f} Litros' .format(base*altura, (base*altura)/2))
