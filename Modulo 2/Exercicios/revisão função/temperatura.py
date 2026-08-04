def c (temperatura):
    return temperatura * 9 / 5 + 32

numero_1 = float(input("digite a temperatura que deseja comverter para fahrenheit: "))

print(f"{numero_1} graus comvetido para fahrenheit fica: {c(numero_1)}")