import matplotlib.pyplot as plt

def grafico():
    x = [1,2,3,4,5,6,8,9,10,11]
    y = [10, 20, 25, 30,40,100,120,150,190,200]

    # Ajustar o tamanho da figura
    
    plt.figure(figsize=(8, 6),facecolor="#82b3f0")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    # Plotar o gráfico com personalização
    plt.plot(x, y, color="#2253cb", linewidth=3, marker="o", markersize=8, markerfacecolor="#2253cb", label="")
    plt.gca().set_facecolor("#82b3f0")
    plt.xticks([])
    # Adicionar título e rótulos
    plt.title("", fontsize=16)
    plt.xlabel("")
    plt.ylabel("")
    plt.grid(True)
    # Adicionar grade e legenda

    

    # Desativa os eixos completamente
    #plt.axis('off')
    #plt.gca().set_facecolor("lightgray")
    # Exibir e salvar o gráfico
    #plt.show()
    plt.savefig("recursos/grafico/imagem_grafico/grafico.png", dpi=1000)
    

grafico()