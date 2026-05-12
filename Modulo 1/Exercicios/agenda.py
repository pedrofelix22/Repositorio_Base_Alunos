import os 

def limpa_tela():
     os.system("cls")

def adciona_nome (lista_nomes,nome):
    lista_nomes.append(nome)
    print(f"{nome} foi adcionado ")

def remover_nome(lista_nome, nome):

      if nome in lista_nome:
            lista_nome.remove(nome)
            print(f"{nome} foi deletado ad lista.") 
      else:
            print(f"{nome} não foi encontrado.")
     


def mostra_nomes(lista_nomes):
      for nome in lista_nomes:
            print(nome)
limpa_tela()
nomes = []

menu = input("escolha sua opção:\n[1] - listar nomes\n[2] - adicionar nomes\n[3] - remover nomes\nsua opção: ")

while True:
      limpa_tela()
      menu = input("Escolha sua opção:\n[1] - Listar nomes\n[2] - Adicionar nomes\n[3] - Remover nomes\n[0] - Sair\nSua opção: ")
      if menu == "0":
            break
      elif menu == "1":
            mostra_nomes(nomes)
            input("Aperte enter para continuar ")
      elif menu =="2":
            nome_salvar = input("digite o nome que deseja adicionar: ")
            adciona_nome(nomes,nome_salvar)
      elif menu == "3":
            nome_remover = input("digite o nome que deseja remover: ")
            input("Aperte enter para continuar ")
            remover_nome(nomes, nome_remover)  
         
      else:
            print("opção invalida.")
            input("Aperte enter para continuar")