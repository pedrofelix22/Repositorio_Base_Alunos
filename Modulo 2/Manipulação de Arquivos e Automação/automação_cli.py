import os 
import shutil
#os.getcwd() - mostra a pasta atual
#os.listdir() - lista arquivos e pastas 
#os. mkdir("pasta") - cria uma pasta
#os.remove("pasta") - remove uma pasta 
#shutil.move("origem", "destino") - move uma pasta da origem ao destino.
#os.system("comando") - executa um comando 

print("criador de pasta")
pasta = input("digite o nome da pasta que deseja criar: ")
os.mkdir(pasta)