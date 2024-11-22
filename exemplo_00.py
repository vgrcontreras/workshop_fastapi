import random
import time


def generate_random_num():
    return random.randint(1, 10)

def double_random_num(num):
    return num * 2

if __name__ == '__main__':
    while True:
        num = generate_random_num()
        result = double_random_num(num)
        print(f'O dobro de {num} é {result}')
        time.sleep(2)