from PIL import Image, ImageDraw, ImageFont


def fontes(caminho,text):
    caminho_fonte = caminho
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