nome = input("Digite o seu nome: ")
pesso = float(input("Digite o seu pesso em kg:" ))
altura = float(input("digite a sua altura em metros: "))

imc = pesso / (altura * altura) 
print(nome,"tem o imc igual a :",imc)
# if imc >=30:
#     print("cuidado com a saude") 
# else:
#     print("tudo ok")
if imc <18.5:
    print("abaixo do pesso.")   
elif imc <=24.9:
    print("pesso normal")
elif imc <=29.9:
    print("sobrepeso")
elif imc <=34.9:
    print("obesidade grau 1")
elif imc <=39.9:
    print("obesidade grau 2")
else:
    print("obesidade grau 3")