from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes





# Função para criptografar um arquivo
def criptografar_arquivo(nome_arquivo, nome_arquivo_saida, chave):
    # Ler o conteúdo do arquivo
    with open(nome_arquivo, "rb") as f:
        dados = f.read()
    
    # Criar o objeto de criptografia AES
    cipher = AES.new(chave, AES.MODE_CBC)
    iv = cipher.iv  # Vetor de inicialização (IV)

    # Criptografar os dados
    dados_criptografados = cipher.encrypt(pad(dados, AES.block_size))

    # Salvar o IV e os dados criptografados no arquivo de saída
    with open(nome_arquivo_saida, "wb") as f:
        f.write(iv + dados_criptografados)

# Função para descriptografar um arquivo
def descriptografar_arquivo(nome_arquivo_criptografado, nome_arquivo_saida, chave):
    # Ler o conteúdo do arquivo criptografado
    with open(nome_arquivo_criptografado, "rb") as f:
        conteudo = f.read()
    
    # Separar o IV e os dados criptografados
    iv = conteudo[:16]  # O IV tem 16 bytes
    dados_criptografados = conteudo[16:]

    # Criar o objeto de descriptografia AES
    cipher = AES.new(chave, AES.MODE_CBC, iv)

    # Descriptografar os dados
    dados = unpad(cipher.decrypt(dados_criptografados), AES.block_size)

    # Salvar os dados descriptografados no arquivo de saída
    with open(nome_arquivo_saida, "wb") as f:
        f.write(dados)

# Exemplo de uso
if __name__ == "__main__":
    # Gerar uma chave de 16 bytes (AES-128)
    chave = get_random_bytes(16)

    # Arquivos de entrada e saída
    arquivo_original = "/home/daniel/Desktop/PROJETOS/PYTHON/novo projeto/recursos/criptografia/arquivo.txt"
    arquivo_criptografado = "arquivo_criptografado.bin"
    arquivo_descriptografado = "arquivo_descriptografado.txt"

    # Criptografar o arquivo
    criptografar_arquivo(arquivo_original, arquivo_criptografado, chave)
    print(f"Arquivo '{arquivo_original}' criptografado como '{arquivo_criptografado}'.")

    # Descriptografar o arquivo
    descriptografar_arquivo(arquivo_criptografado, arquivo_descriptografado, chave)
    #print(f"Arquivo '{arquivo_criptografado}' descriptografado como '{arquivo_descriptografado}'.")