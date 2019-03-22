import pyautogui
import time
import numpy as np

pyautogui.FAILSAFE = True


def farm(seconds, process_start):
    process = time.perf_counter()
    clicks = 7
    click_interval = .14
    while process != (process_start + seconds):

        pyautogui.click(clicks=clicks, interval=click_interval)

        pyautogui.keyDown('a')
        pyautogui.keyDown('w')

        time.sleep(np.random.uniform(low=0, high=.4, size=1)[0])

        pyautogui.keyUp('a')
        pyautogui.keyDown('d')

        pyautogui.click(clicks=clicks, interval=click_interval)

        time.sleep(np.random.uniform(low=0, high=.4, size=1)[0])

        pyautogui.keyUp('d')
        pyautogui.keyDown('a')

        pyautogui.click(clicks=clicks, interval=click_interval)

        process = time.perf_counter()

    pyautogui.keyUp('a')
    pyautogui.keyUp('w')


if __name__ == '__main__':
    while True:
        try:
            action_times = input('Qual a quantidade de vezes que deseja repetir o processo? \n')
            print('Iniciando a farm de blaze rod. Dando tempo para organização.')
            time.sleep(4)
            i = 0
            while i < int(action_times):
                start = int(time.perf_counter())
                farm(120, start)
                i += 1
            break
        except KeyboardInterrupt:
            print('[Keyboard Interrupt] Saindo.')
            break
        except pyautogui.FailSafeException:
            print('[Failsafe] Saindo.')
            break
