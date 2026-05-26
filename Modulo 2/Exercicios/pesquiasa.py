import pyautogui as at

def apertar_tab(qtd):
    for i in range(qtd):
        at.press("tab")
        at.sleep(0.02)

at.hotkey("win", "r")
at.write("Chrome", 0.2)
at.press("enter")
at.sleep(1)
at.write("stop", 0.2)
at.press("enter")
# at.sleep(4)
# apertar_tab(4)
# at.write("os parças 2",0.2)
# at.press("enter")
