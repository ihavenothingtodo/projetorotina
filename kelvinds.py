import time
import pyautogui
pyautogui.FAILSAFE = True


def walk(walk_time):
    pyautogui.keyDown("w")
    time.sleep(walk_time)
    pyautogui.keyUp("w")
    time.sleep(.4)


def turnright():
    pyautogui.moveRel(300)
    pyautogui.moveRel(300)


def turnbottom():
    pyautogui.moveRel(yOffset=210)


def buy(buy_times):
    i = 0
    while i < buy_times:
        pyautogui.click(button="right")
        pyautogui.keyDown("a")
        time.sleep(.05)
        pyautogui.keyUp("a")
        i += 1


def kelvinds():
    pyautogui.press("t")
    pyautogui.press("up")
    pyautogui.press("up")
    pyautogui.press("enter")
    time.sleep(8.5)


def farmmoney():
    pyautogui.press("t")
    pyautogui.press("up")
    pyautogui.press("up")
    pyautogui.press("enter")
    time.sleep(8.5)
    pyautogui.click()


def farm(farm_times):
    i = 0
    while i < farm_times:
        walk(.3)
        turnright()

        time.sleep(0.3)
        walk(.8)

        time.sleep(0.5)
        if i <= 40:
            turnbottom()

        time.sleep(0.8)
        buy(40)

        farmmoney()
        kelvinds()

        i += 1


if __name__ == "__main__":
    while True:
        try:
            print("[Farm] Iniciando. Dando tempo para organização.")
            time.sleep(3)

            print("[Farm] Começando.")
            farm(80)
            break
        except KeyboardInterrupt:
            print("[Keyboard Interrupt] Saindo.")
            break
        except pyautogui.FailSafeException:
            print("[FailSafe Exception] Saindo.")
            break
