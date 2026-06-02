import pyautogui as at

at.hotkey("win", "r")
programa = at.prompt("Digite o nome do programa que deseja abrir: ")
at.write(programa, 0.2)
at.press("enter")










# programa = at.prompt("Digite o nome do programa que deseja abrir: ")
# at.write(programa, 0.2)

# at.hotkey("win", "r")
# at.write("Chome", 0.2)
# at.press("enter")
# at.sleep(1)
# at.write("Youtube.com")
# at.press("enter")