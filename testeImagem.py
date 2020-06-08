from numba import jit, cuda, vectorize
# from PIL import ImageGrab
# from imagem import *
# from texto import *
# import cv2
# from time import sleep
# ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# alturaCelula = 32
# altura = 112
# P1_left = 4
# P2_left = 1633

# bbox = (P1_left, altura, P2_left, altura + alturaCelula)


@vectorize(['float64(float64)'], target="cuda")
def main():
    print("asdas")
    # img = prepararImagem(ImageGrab.grab(bbox), 1)
    # extrairTexto(img)

main()
