import csv
import os

ARQUIVO = "alunos.csv"


if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "Idade", "Nota"])


def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, nota])

    print("Aluno cadastrado com sucesso!\n")


def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  

        encontrou = False
        for linha in leitor:
            print(f"Nome: {linha[0]} | Idade: {linha[1]} | Nota: {linha[2]}")
            encontrou = True

        if not encontrou:
            print("Nenhum aluno cadastrado.")

    print()


def listar_alunos_acima_8():
    print("\n--- ALUNOS COM NOTA ACIMA DE 8 ---")

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  

        encontrou = False
        for linha in leitor:
            if float(linha[2]) > 8:
                print(f"Nome: {linha[0]} | Idade: {linha[1]} | Nota: {linha[2]}")
                encontrou = True

        if not encontrou:
            print("Nenhum aluno com nota acima de 8.")

    print()


while True:
    print("===== MENU =====")
    print("[1] - Cadastrar aluno e nota")
    print("[2] - Listar alunos")
    print("[3] - Listar alunos com nota acima de 8")
    print("[0] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        listar_alunos_acima_8()
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!\n")