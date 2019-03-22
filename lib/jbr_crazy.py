import pyautogui
import time
from lib.utils import variables
from lib.utils import functions

pyautogui.FAILSAFE = True


def buy(n):
    i = 0
    while i < n:
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
        print("[Farm] Iniciando processo nº " + str(i) + ".")
        # Passos para a compra de cactos na loja do Jbr_Crazy
        # Andar para frente
        print("[Farm] Andando para frente.")
        pyautogui.keyDown("w")
        time.sleep(1)
        pyautogui.keyUp("w")

        # Andar para o lado direito
        print("[Farm] Andando para a direita.")
        pyautogui.keyDown("d")
        time.sleep(2.1)
        pyautogui.keyUp("d")

        # Abaixar a visão
        print("[Farm] Procurando os baús inferiores.")
        if i < 28:
            pyautogui.moveRel(yOffset=200)
        elif i > 38:
            pyautogui.moveRel(yOffset=-170)

        # Comprar
        print("[Farm] Comprando cactos.")
        buy(28)

        # Ir para a /loja FarmMoney para revender os cactos
        print("[Farm] Indo para a /warp loja para revender cactos.")
        sell()

        # Voltar para a loja
        functions.command_above(2)
        i += 1
        time.sleep(variables.buy_sleep)


if __name__ == "__main__":
    while True:
        try:
            print("[Farm] Inicializando... Dando tempo para preparação.")
            # Tempo para preparação
            time.sleep(3)
            
            print("[Farm] Iniciando processo de Farm.")

            # pyautogui.moveRel(yOffset=-300)
            farm(40)

            break
        except KeyboardInterrupt:
            print("[Keyboard Interrupt] Saindo.")
            break
        except pyautogui.FailSafeException:
            print("[FailSafe] Saindo.")
            break
