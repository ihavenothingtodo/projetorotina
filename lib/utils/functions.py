import pyautogui


# Essa função retorna o n-ésimo comando efetuado, começando do último.
def command_above(times_up):
    pyautogui.press('t')
    for i in range(1, times_up):
        pyautogui.press('up')
    pyautogui.press('enter')


def warp_loja():
    pyautogui.press('t')
    pyautogui.write('/warp loja')


def sell_cactus():
    pyautogui.press('t')
    pyautogui.write('/loja farmmoney')


def sell_blaze_rod():
    pyautogui.press('t')
    pyautogui.write('/loja jifd')
