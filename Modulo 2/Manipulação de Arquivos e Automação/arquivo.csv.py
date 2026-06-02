import csv 

with open("dados.csv" "r", encoding= "utf-8") as arquivo:
    dados = csv.reader(arquivo)

    for linha in dados:
        print(linha)
        print("{nome:^15}|{idade:^10}|{nota:^10} ")