from random import randint

minimo = int(input("indique minimo: "))
maximo = int(input("indique maximo: "))
nRandom = randint(minimo, maximo)

if nRandom % 2 != 0:
    print(f"su numero aleatorio es {nRandom}, el cual es impar")
    nRandom -= 1
    print(f"se utilizara {nRandom} para generar la tabla de multiplicar.")
else:
    print(f"su numero aleatorio es: {nRandom}")
    
print(f"1 x {nRandom} = {nRandom * 1}")
print(f"2 x {nRandom} = {nRandom * 2}")
print(f"3 x {nRandom} = {nRandom * 3}")
print(f"4 x {nRandom} = {nRandom * 4}")
print(f"5 x {nRandom} = {nRandom * 5}")
print(f"6 x {nRandom} = {nRandom * 6}")
print(f"7 x {nRandom} = {nRandom * 7}")
print(f"8 x {nRandom} = {nRandom * 8}")
print(f"9 x {nRandom} = {nRandom * 9}")
print(f"10 x {nRandom} = {nRandom * 10}")
print(f"11 x {nRandom} = {nRandom * 11}")
print(f"12 x {nRandom} = {nRandom * 12}")