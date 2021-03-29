import pyautogui
import time

time.sleep(5)
print("iniciando votação")

while True:
    time.sleep(5)
    name_vote = pyautogui.locateOnScreen('nome.png')
    checkpoint = pyautogui.locateOnScreen('checkpoint.png')
    back = pyautogui.locateOnScreen('back.png')

    if name_vote:
        print("achou o emparedado")
        point=pyautogui.center(name_vote)
        pyautogui.click(point)
      
    if checkpoint:
        print("achou o sou humano")
        pointCheck=pyautogui.center(checkpoint)
        pyautogui.click(pointCheck)

    if back:
        print("achou o botao voltar")
        backPoint=pyautogui.center(back)
        pyautogui.click(backPoint)

    pass      
    time.sleep(25)