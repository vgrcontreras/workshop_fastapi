import random
import time


def gerar_numero_aleatorio():
    num = random.randint(1, 10)

    with open('numeros.txt', 'a') as file:
        file.write(f'{num}\n')

if __name__ == '__main__':
    while True:
        gerar_numero_aleatorio()
        time.sleep(2)