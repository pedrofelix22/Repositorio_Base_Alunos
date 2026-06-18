import os
from datetime import datetime

#Limpar tela
os.system("cls")
print(datetime.now())

hora = datetime.now().hour
# hora = int(input(Digite a hora logal:))
if hora < 12:
 mensagem ="BOM DIA ⛅ "

elif hora < 18:
    mensagem = ("BOA TARDE 🌞")

else:
   mensagem = "BOA NOITE 🥱😴💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤💤"

os.system(f"start cmd /k echo {mensagem}")
