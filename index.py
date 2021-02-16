import pyautogui
import time

time.sleep(5)
print("iniciando votação")

while True:
    time.sleep(5)
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
                pyautogui.click(backPoint)
            pass
    
    time.sleep(30)
    pass      