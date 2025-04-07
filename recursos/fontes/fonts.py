from PIL import Image, ImageDraw, ImageFont
import os

def fontes(text):
    #aqui acha o diretorio e as pastas e o arquivo necessario
    diretorio_font=os.path.dirname(os.path.realpath(__file__))
    pasta_fonte=os.path.join(diretorio_font,"lyster")
    caminho_fonte=os.path.join(pasta_fonte,"Lyster_PERSONAL_USE_ONLY.ttf")
    
    # Criando uma imagem com Pillow
    #largura, altura = 400, 200
    largura, altura = 700, 400
    imagem = Image.new("RGB", (largura, altura), "#242424")
    draw = ImageDraw.Draw(imagem)
    # Carregando a fonte TTF
    fonte = ImageFont.truetype(caminho_fonte, size=200)
    # Renderizando texto na imagem
    texto = text
    draw.text((50, 70), texto, font=fonte, fill="black")
    return imagem