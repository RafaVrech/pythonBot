from PIL import ImageGrab
from imagem import *
from texto import *

P1_left = 1740
P2_left = 1820

P1_EURUSD_right = 270
P2_EURUSD_right = 300
P1_GBPUSD_right = 471
P2_GBPUSD_right = 510
P1_EURGBP_right = 670
P2_EURGBP_right = 708
P1_USDJPY_right = 880
P2_USDJPY_right = 913


def extrairPorcentagem(par):

    boxSwitcher = {
        "EURUSD": eurusd,
        "GBPUSD": gbpusd,
        "EURGBP": eurgbp,
        "USDJPY": usdjpy
    }

    img = prepararImagem(ImageGrab.grab(
        boxSwitcher.get(par, default)()), 3)
    
    texto = ocr.image_to_string(
        img, config="--psm 4 -c tessedit_char_whitelist=0123456789")

    return texto


def eurusd():

    bbox = (P1_left, P1_EURUSD_right, P2_left, P2_EURUSD_right)

    return bbox


def gbpusd():
    bbox = (P1_left, P1_GBPUSD_right, P2_left, P2_GBPUSD_right)

    return bbox


def eurgbp():
    bbox = (P1_left, P1_EURGBP_right, P2_left, P2_EURGBP_right)

    return bbox


def usdjpy():
    bbox = (P1_left, P1_USDJPY_right, P2_left, P2_USDJPY_right)

    return bbox

def default():
    return (0, 1, 2, 3)
