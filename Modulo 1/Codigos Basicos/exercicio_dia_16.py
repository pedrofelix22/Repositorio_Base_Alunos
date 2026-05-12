numero_tabuada = int(input("digite o numero que deseja:"))
numero_inicial = int(input("digite onde a tabuada deve começar:"))
numero_final = int(input("digite onde a tabuada deve acabar:"))

for i in range(numero_inicial,numero_final + 1):
    print( numero_tabuada,"x",i, "=", numero_tabuada * i)

