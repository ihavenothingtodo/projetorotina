import pyautogui
import time

# Posições: (89,5 / 0,5)

pyautogui.FAILSAFE = True


def turny(offset):
    pyautogui.moveRel(yOffset=offset)


def placeblock(position=None, place_times=1):
    i = 0
    while i < place_times:
        if position is not None:
            pyautogui.press(str(position))
        pyautogui.rightClick()
        i += 1

def turnx(offset):
    pyautogui.moveRel(xOffset=offset)

def construct():
    # Base de pedra
    turny(150)
    time.sleep(.1)
    placeblock(place_times=3)
    turny(20)
    turnx(-140)
    placeblock()
    turnx(310)
    placeblock()

    # Base de areia
    turny(-100)
    placeblock(2)

if __name__ == "__main__":
    while True:
        try:
            print(
                "[Criação] Iniciando a criação de farm de cacto. Dando tempo para organização.")
            time.sleep(3)
            print("[Criação] Começando.")
            construct()
            break
        except KeyboardInterrupt:
            print("[Keyboard Interrupt] Saindo.")
            break
        except pyautogui.FailSafeException:
            print("[Failsafe Exception] Saindo.")
            break
