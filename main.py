from PIL import ImageGrab
from imagem import *
from porcentagem import *
from texto import *
import cv2
from timeit import default_timer as timer
import requests
from datetime import datetime
import json

ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

alturaCelula = 32
altura = 112
P1_left = 25
P2_left = 1625

bbox = (P1_left, altura, P2_left, altura + alturaCelula)

resultados = []

while True:
    for i in range(24):
        start = timer()
        img = prepararImagem(ImageGrab.grab(bbox), 3)
        duration = timer() - start
        print('Preparar Imagem: ' + str(duration))

        start = timer()
        array = extrairTexto(img).split(' ')
        duration = timer() - start
        print('Extrair Texto: ' + str(duration))

        jsonObj = {
            "id": {
                "data": array[6] + " " + array[7] + array[8],
                "botNo": array[0]
            },
            "par": array[1],
            "ordem": array[2],
            "preco": array[3],
            "tp": array[4],
            "sl": array[5],
            "percentage": extrairPorcentagem(array[1])
        }
        jsonObj = json.dumps(jsonObj)
        print(jsonObj)

        headers = {'content-type': 'application/json'}
        requests.post("http://localhost:8099/bot",
                            data=jsonObj, headers=headers)

        altura = altura + alturaCelula + 2
        bbox = (P1_left, altura, P2_left, altura + alturaCelula)
        
    altura = 112    


