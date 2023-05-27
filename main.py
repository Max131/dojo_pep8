from codebreaker import Codebreaker

INTENTOS_TOTALES = 10
codebreaker = Codebreaker()

intento = 0

print("Jugar Codebreaker!")

while intento != INTENTOS_TOTALES:
    number = input("Numero: ")
    resolve = codebreaker.adivinar(number)
    print(resolve)
    if resolve is True:
        print("You win!!")
        break
