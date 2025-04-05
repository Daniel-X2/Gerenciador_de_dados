
from PIL import Image, ImageTk, ImageDraw, ImageFont
# Caminho para o arquivo .ttf
caminho_fonte = "/home/daniel/Desktop/nnn/Ananda Personal Use.ttf"
# Criando uma imagem com Pillow
largura, altura = 400, 200
imagem = Image.new("RGB", (largura, altura), "white")
draw = ImageDraw.Draw(imagem)
# Carregando a fonte TTF
fonte = ImageFont.truetype(caminho_fonte, size=40)
# Renderizando texto na imagem
texto = "CRUD sincero"
draw.text((50, 70), texto, font=fonte, fill="black")
# Convertendo a imagem para o formato compatível com Tkinter
imagem_tk = ImageTk.PhotoImage(imagem)