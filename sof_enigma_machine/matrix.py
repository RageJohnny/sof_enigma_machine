import random as r
from colorama import init
from colorama import Fore
import time

init()

symbols = ["0", "1", " ", " "]
line = []
counter = 0

for i in range(118):
    x = r.randint(0, 3)
    line.append(symbols[x])

    counter += 1

for i in range(10000):
    if counter % 5 == 0:
        r_symbols = [r.randint(0, 117) for x in range(10)]

        for i in r_symbols:
            line[i] = symbols[r.randint(0, 3)]
    print(Fore.GREEN, *line)
    counter += 1
    time.sleep(0.01)
