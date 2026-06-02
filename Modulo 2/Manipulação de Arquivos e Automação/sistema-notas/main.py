import os
def limpar_tela():
    os.system("cls")

print("seja bem-vindo ao sistema de notas, ta reprovado ou não")
while True:
 opcao = input ("[1] - Cadastra aluno e nota \n"\
    nome = input("digite o nome do(a) aluno(a):")
    idade = int(input("Digite a nota do(a) aluno(a): "))
    nota = float(input("Digite a noata do(a) aluno(a): "))
    withopen("alunos.csv","a",newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([nome,idade,nota])
    
"[2]- lista aluno \n" \
"[3] - listar alunos com nota acima de 8\n" \
 "[0]- sair \n sua opção: ")

 if opcao == "1":
    print("cadastrar aluno")
 elif opcao == "2":
    print("listrar alunos")
 elif opcao == "3":
    print("listar aluno com nota acima de 8")
 elif opcao == "0":
    print("Saindo.............")
    break
 else:
    print("Opção invalida.")   

input("Aperte ENTER para continuar")
limpar_tela()