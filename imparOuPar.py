import numpy as np

def main():
    choices = user_choices()
    odd_or_even(choices)


def machine_random_number():
    machine_rn = np.random.randint(0, 10)
    return machine_rn

def user_choices():
    choices = {}
    number = int(input("Escolha um número para jogar: "))
    choice = str(input("Escolha entre 'Par' ou 'Ímpar': "))

    choices["number"] = number
    choices["choice"] = choice

    return choices


def odd_or_even(choices):
    result = "Ímpar"
    machine = machine_random_number()

    # Somar o número randômico da máquina e o número escolhido pelo jogador
    total_sum = machine + choices["number"]

    # Verifica se o resto da divisão da soma dos número é zero para ditar se o número é PAR
    if total_sum % 2 == 0:
        result = "Par"

    print('================================')
    print(f"Máquina jogou: {machine}")
    print(f"Você jogou: {choices['number']}")
    print('================================')

    print(f"Resultado do jogo é: {total_sum} - {result}")
    print('================================')
    if result.upper() == choices["choice"].upper():
        print("você ganhou! :)")
    else:
        print("você perdeu! :(")