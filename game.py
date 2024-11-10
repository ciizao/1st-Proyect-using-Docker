import os
import random

print("Bienvenido al Juego")
print("Opciones:")
options = ('piedra','papel','tijera') 

user = os.getenv("user_option", "piedra").lower()
computer = random.choice(options)
print("")
  
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