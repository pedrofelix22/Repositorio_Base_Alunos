# arquivo = open("texto.txt", "r", encoding="utf-8")
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close()

with open("texto.txt", "r",encoding= "utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open("texto.txt", "a",encoding= "utf-8") as arquivo:
    texto = "\nFutebol sem bola, piu-piu sem frajola.sou eu assim sem você."
    arquivo.write(texto)