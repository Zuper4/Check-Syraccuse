from termcolor import colored

for i in range(1, 10001):

    number = i

    while number != 1:
        if number % 2 == 0:
            number /= 2

        elif number % 2 == 1:
            number *= 3
            number += 1
            
    print(colored(i, "green"))

