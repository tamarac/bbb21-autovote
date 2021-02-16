import pyautogui
import time

#time.sleep(5)
print("iniciando votação")

while True:
    name_vote = pyautogui.locateOnScreen('nome.png')
    if name_vote:
        point=pyautogui.center(name_vote)
        pyautogui.click(point)
        checkpoint = pyautogui.locateOnScreen('checkpoint.png')
       
        if checkpoint:
            pointCheck=pyautogui.center(checkpoint)
            pyautogui.click(pointCheck)
            back = pyautogui.locateOnScreen('back.png')

            if back:
                backPoint=pyautogui.center(back)
                print("Achei botao voltar")
                pyautogui.click(backPoint)
                print("cliquei")
            pass
    pass      