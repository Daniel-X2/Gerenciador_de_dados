import matplotlib.pyplot as plt

def grafico():
    x = [1,2,3,4,5,6,8,9,10,11]
    y = [10, 20, 25, 30,40,100,120,150,190,200]

    # Ajustar o tamanho da figura
    plt.figure(figsize=(8, 6))

    # Plotar o gráfico com personalização
    plt.plot(x, y, color="blue", linewidth=10, marker="o", markersize=10, markerfacecolor="red", label="Linha de Exemplo")

    # Adicionar título e rótulos
    plt.title("Exemplo de Gráfico Melhorado", fontsize=16)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")

    # Adicionar grade e legenda
    plt.grid(True)
    plt.legend()

    # Desativa os eixos completamente
    plt.axis('off')

    # Exibir e salvar o gráfico
    plt.savefig("recursos/grafico/imagem_grafico/grafico.png", dpi=1000)
    

grafico()