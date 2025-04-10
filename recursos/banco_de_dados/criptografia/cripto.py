from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

def  gerar_chave(senha,salt):
    chave=PBKDF2(senha,salt,dkLen=32,count=100000)
    return chave

def criptografar_arquivo(nome_arquivo,nome_saida,senha):
    #gerar um salt aleatorio
    salt=get_random_bytes(16)
    chave=gerar_chave(senha,salt)
    #criar objeto de criptografia AES
    cipher=AES.new(chave,AES.MODE_CBC)
    iv=cipher.iv
    #LER OS DADOS DO ARQUIVO
    with open(nome_arquivo,"rb") as f:
        dados= f.read()
        #adiciona o padding aos dados
    dados_preenchidos=pad(dados,AES.block_size)
    #criptografa os dados
    dados_criptogrados=cipher.encrypt(dados_preenchidos)
    #salva o salt, iv e os dados criptografados no arquivo de saida

    with open(nome_saida,"wb") as f:
        f.write(salt+iv+dados_criptogrados)


def descriptografar_arquivo(nome_arquivo_criptografado,nome_arquivo_saida,senha):

    with open(nome_arquivo_criptografado,"rb") as f:
        conteudo=f.read()
    #extrai o salt, iv e os dados criptografados
    salt=conteudo[:16]
    iv=conteudo[16:32]
    dados_criptografados=conteudo[32:]
    #gerar a chave a partir da senha e do salt
    chave=gerar_chave(senha,salt)
    #cria o objeto de descriptografar aes
    cipher=AES.new(chave,AES.MODE_CBC,iv)

    #descriptografar os dados
    dados_preenchidos=cipher.decrypt(dados_criptografados)

    #remover o padding dos dados

    dados=unpad(dados_preenchidos,AES.block_size)

    with open(nome_arquivo_saida,"wb") as f:
        f.write(dados)




