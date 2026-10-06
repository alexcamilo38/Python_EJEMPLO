import random
import time
import os

GREEN = "\033[32m"
END = "\033[0m"


def buses(n1, n2):
    output = []

    output.append(115 * " ")

    # Bus 1
    output.append((n1 * " ") + "___________" + ((100 - n1) * " ") + "|")
    output.append((n1 * " ") + "|__|__|__|__|__" + ((97 - n1) * " ") + "|")
    output.append((n1 * " ") + "| Yilmer       |)" + ((96 - n1) * " ") + "|")
    output.append((n1 * " ") + "|o------------o|)" + ((95 - n1) * " ") + "|")

    output.append(115 * " ")

    # Bus 2
    output.append((n2 * " ") + "_____________" + ((100 - n2) * " ") + "|")
    output.append((n2 * " ") + "|__|__|__|__|__" + ((97 - n2) * " ") + "|")
    output.append((n2 * " ") + "| Carlos       |)" + ((96 - n2) * " ") + "|")
    output.append((n2 * " ") + "|o------------o|)" + ((95 - n2) * " ") + "|")

    output.append(115 * " ")

    return "\n".join(output)


n1 = 0
n2 = 0

while n1 < 95 and n2 < 95:

    print("\033[H\033[J", end="")

    print(buses(n1, n2))

    n1 += random.randint(1, 3)
    n2 += random.randint(1, 3)

    time.sleep(0.1)

print("\033[H\033[J", end="")
print(buses(n1, n2))

if n1 > n2:
    print("\n🏆 ¡Yilmer ganó!")
elif n2 > n1:
    print("\n🏆 ¡Carlos ganó!")
else:
    print("\n🤝 ¡Empate!")