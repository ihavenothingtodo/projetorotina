import pyautogui
import lib.utils.variables


# Essa função retorna o n-ésimo comando efetuado, começando do último.
def command_above(times_up):
    pyautogui.press('t')
    for i in range(0, times_up):
        pyautogui.press('up')
    pyautogui.press('enter')


def warp_loja():
    pyautogui.press('t')
    pyautogui.write('/warp loja')
    pyautogui.press('enter')


def loja_jbr_crazy():
    pyautogui.press('t')
    pyautogui.write('/loja jbr_crazy')
    pyautogui.press('enter')


def loja_kelvinds():
        pyautogui.press('t')
        pyautogui.write('/loja kelvinds')
        pyautogui.press('enter')


def sell_cactus():
    pyautogui.press('t')
    pyautogui.write('/loja farmmoney')
    pyautogui.press('enter')


def sell_blaze_rod():
    pyautogui.press('t')
    pyautogui.write('/loja jifd')
    pyautogui.press('enter')
