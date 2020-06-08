from PIL import ImageGrab
from imagem import *
from texto import *
import cv2
from time import sleep
import requests
from datetime import datetime
import json

ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

alturaCelula = 32
altura = 112
P1_left = 133
P2_left = 1500

bbox = (P1_left, altura, P2_left, altura + alturaCelula)

resultados = []

while True:
    for i in range(24):
        img = prepararImagem(ImageGrab.grab(bbox), 3)

        array = extrairTexto(img).split(' ')
        
        jsonObj = {
            "id": {
                "data": array[6] + " " + array[7] + array[8],
                "botNo": array[0]
            },
            "par": array[1],
            "ordem": array[2],
            "preco": array[3],
            "tp": array[4],
            "sl": array[5]
        }
        jsonObj = json.dumps(jsonObj)
        print(jsonObj)

        headers = {'content-type': 'application/json'}
        print(requests.post("http://localhost:8099/bot",
                            data=jsonObj, headers=headers))

        altura = altura + alturaCelula + 2
        bbox = (P1_left, altura, P2_left, altura + alturaCelula)
        
    altura = 112    


    # data = datetime.strptime(
    #     array[5] + array[6] + array[7], '%m/%d/%Y%H:%M:%S%p')


