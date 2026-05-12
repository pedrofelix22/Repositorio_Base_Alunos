#  {
#   funcao inicio() {
#     cadeia nome
#     real nota1
#     real nota2
#     real nota3programa
#     real media
#     escreva("Digite o nome do aluno: ")
#     leia(nome)
#     escreva("Digite o valor da primeira nota: ")
#     leia(nota1)
#     escreva("Digite o valor da segunda nota: ")
#     leia (nota2)
#     escreva("Digite o valor da terceira nota: ")
#     leia(nota3)

#     media=(nota1+nota2+nota3) /3

#     escreva("A media das notas de ", nome," foi ", media)
#   }
# }

nome = input("Digite o seu nome: ")

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("digite a segunda nota: "))

nota3 = float(input("digite a terceira nota"))

media = (nota1 + nota2 + nota3) /3    
print("a meedia de ", nome, "foi:", media)
