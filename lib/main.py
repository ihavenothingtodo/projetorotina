from lib.utils import functions
from lib import jbr_crazy
import pyautogui
import time


def execute_farms():
    functions.sell_cactus()
    time.sleep(5)
    functions.loja_jbr_crazy()
    time.sleep(5)
    jbr_crazy.start()