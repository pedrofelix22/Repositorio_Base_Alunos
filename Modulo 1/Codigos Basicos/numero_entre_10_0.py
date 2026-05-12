nota = float(input("Digite a sua nota (nota valida de 0 ate 10): "))

while nota < 0 or nota > 10:
    nota = float(input( "invaqlido,digite uma nota entre 0 e 10: "))

    print(f"sua nota foi: {nota}")