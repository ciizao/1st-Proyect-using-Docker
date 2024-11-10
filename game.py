import random

print("Bienvenido al Juego")
print("Escriba una de estas opciones:")
options = ('piedra','papel','tijera') 

user = input('piedra, papel, tijera\n')
user = user.lower()
computer = random.choice(options)
print("")

if not user in options:
  print("¡Opción Incorrecta!")
  
print('Player =>',user)
print('Sistem => ',computer)

if user == computer:
  print('Empate😐')
elif user == 'piedra':
  if computer == 'tijera':
    print('Piedra gana a tijera')
    print('Win👏')
  else:
    print('Papel gana a piedra ')
    print( 'Lose😔 ')
elif user == 'papel':
  if computer == 'piedra':
    print('Papel gana a piedra')
    print('Win👏')
  else:
    print('Tijera gana a  papel ')
    print( 'Lose😔 ')
elif user == 'tijera':
  if computer == 'papel':
    print('Tijera gana a papel')
    print('Win👏')
  else:
    print('Piedra gana a tijera ')
    print('Lose😔 ')