import matplotlib.pyplot as plt

def grafico():
    x = [1,2,3,4,5,6,8,9,10,11]
    y = [10, 20, 25, 30,40,100,120,150,190,200]

    # Ajustar o tamanho da figura
    plt.figure(figsize=(8, 6),facecolor="gray")

    # Plotar o gráfico com personalização
    plt.plot(x, y, color="blue", linewidth=15, marker="o", markersize=10, markerfacecolor="red", label="")

    # Adicionar título e rótulos
    plt.title("", fontsize=16)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")

    # Adicionar grade e legenda

    

    # Desativa os eixos completamente
    #plt.axis('off')
    #plt.gca().set_facecolor("lightgray")
    # Exibir e salvar o gráfico
    plt.savefig("recursos/grafico/imagem_grafico/grafico.png", dpi=1000)
    

grafico()