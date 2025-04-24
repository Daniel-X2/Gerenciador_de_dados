from PIL import Image

# Abrir a imagem
imagem = Image.open("recursos/grafico/imagem_grafico/grafico.png")

# Obter as dimensões da imagem
largura, altura = imagem.size

# Definir uma área de recorte central
margem = 490
area_de_recorte = ((margem+63), (margem+30), largura - margem, altura - (margem-50))

# Recortar a imagem
imagem_recortada = imagem.crop(area_de_recorte)

# Salvar ou exibir a imagem recortada
imagem_recortada.save("recursos/grafico/imagem_grafico/grafico.png")
#imagem_recortada.show()