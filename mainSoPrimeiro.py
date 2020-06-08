from PIL import ImageGrab
from imagem import *
from texto import *
import cv2
from time import sleep
from telegramBot import sendMessage
ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

alturaCelula = 32
altura = 112
P1_left = 218
P2_left = 1253

bbox = (P1_left, altura, P2_left, altura + alturaCelula)

resultados = []

img = prepararImagem(ImageGrab.grab(bbox), 3)
resultadoAnterior = extrairTexto(img)
resultados.append(resultadoAnterior)

while True:
    img = prepararImagem(ImageGrab.grab(bbox), 3)
    texto = extrairTexto(img)
    if(resultadoAnterior != texto):
        resultados.append(texto)
        resultadoAnterior = texto

        json = extrairTexto(img).split(' ')
        print(json)
        
        print(sendMessage(texto))
    # sleep(1)
