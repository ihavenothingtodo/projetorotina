import pyautogui
import time
from lib.utils import variables
from lib.utils import functions

pyautogui.FAILSAFE = True


def buy(times_left):
    i = 0

    while i < times_left:
        pyautogui.keyDown("a")
        time.sleep(variables.one_block)
        pyautogui.keyUp("a")
        pyautogui.click(button='right')
        i += 1


def sell():
    functions.command_above(2)
    time.sleep(variables.sell_sleep)
    pyautogui.click()


def farm(repetitions):
    i = 0
    while i < repetitions:
        # Andar para frente
        pyautogui.keyDown("w")
        time.sleep(1)
        pyautogui.keyUp("w")

        # Andar para o lado direito
        pyautogui.keyDown("d")
        time.sleep(2.1)
        pyautogui.keyUp("d")

        # Abaixar a visão
        if i < 28:
            pyautogui.moveRel(yOffset=200)
        elif i > 38:
            pyautogui.moveRel(yOffset=-170)

        # Comprar
        buy(28)

        # Ir para a /loja FarmMoney para revender os cactos
        sell()

        # Voltar para a loja
        functions.command_above(2)
        i += 1
        time.sleep(variables.buy_sleep)


def start():
    while True:
        try:
            farm(40)
        except KeyboardInterrupt:
            break
        except pyautogui.FailSafeException:
            break
