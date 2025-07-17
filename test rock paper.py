
import random

# Diccionario para convertir números en emojis
options = {
    1: '✊',  # Rock
    2: '✋',  # Paper
    3: '✌️'  # Scissors
}

print("===================")
print("Rock Paper Scissors")
print("===================\n")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

# Solicitar opción al jugador
player = int(input("Pick a number: "))

# Verificar que la opción del jugador es válida
if player not in [1, 2, 3]:
    print("Opción no válida. Debe ser 1, 2 o 3.")
else:
    # Opción de la computadora
    computer = random.randint(1, 3)

    print(f"\nYou chose: {options[player]}")
    print(f"CPU chose: {options[computer]}")

    # Lógica del juego
    if player == computer:
        print("It's a tie!")
    elif (
        (player == 1 and computer == 3) or
        (player == 2 and computer == 1) or
        (player == 3 and computer == 2)
    ):
        print("The player won!")
    else:
        print("The CPU won!")
