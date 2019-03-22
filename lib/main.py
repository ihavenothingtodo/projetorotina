from lib.utils import functions
from lib.utils import variables
from lib import jbr_crazy
from lib import kelvinds
import time


def execute_farms():
    functions.sell_cactus()
    time.sleep(variables.sell_sleep)
    functions.loja_jbr_crazy()
    time.sleep(variables.buy_sleep)
    jbr_crazy.start()

    functions.sell_cactus()
    time.sleep(variables.sell_sleep)
    functions.loja_kelvinds()
    time.sleep(variables.buy_sleep)
    kelvinds.start()
