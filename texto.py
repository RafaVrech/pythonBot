import pytesseract as ocr
# from numba import jit, cuda

# @jit(target="cuda")
def extrairTexto(img):
    texto = ocr.image_to_string(img, config="--psm 4")
    print(texto)
    return texto
