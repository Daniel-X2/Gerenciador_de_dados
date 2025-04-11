from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import base64

# Função para gerar uma chave a partir de uma senha
def gerar_chave(senha, salt):
    """
    Gera uma chave criptográfica a partir de uma senha usando PBKDF2.
    
    Args:
        senha (str): A senha fornecida pelo usuário.
        salt (bytes): Um valor aleatório para tornar a chave única.
    
    Returns:
        bytes: Uma chave de 32 bytes (AES-256).
    """
    chave = PBKDF2(senha, salt, dkLen=32, count=100000)
    return chave

# Função para criptografar dados
def criptografar_dados(dados, senha):
    """
    Criptografa uma string usando AES e uma senha.
    
    Args:
        dados (str): Os dados a serem criptografados.
        senha (str): A senha para derivar a chave.
    
    Returns:
        str: Os dados criptografados em base64.
    """
    # Gerar um salt aleatório
    salt = get_random_bytes(16)
    chave = gerar_chave(senha, salt)
    # Criar o objeto de criptografia AES
    cipher = AES.new(chave, AES.MODE_CBC)
    iv = cipher.iv  # Vetor de inicialização (IV)
    # Adicionar padding aos dados
    dados_preenchidos = pad(dados.encode(), AES.block_size)
    # Criptografar os dados
    dados_criptografados = cipher.encrypt(dados_preenchidos)
    # Retornar os dados criptografados em base64 (salt + IV + dados criptografados)
    return base64.b64encode(salt + iv + dados_criptografados).decode()
# Função para descriptografar dados
def descriptografar_dados(dados_criptografados, senha):
    """
    Descriptografa uma string criptografada usando AES e uma senha.
    
    Args:
        dados_criptografados (str): Os dados criptografados em base64.
        senha (str): A senha para derivar a chave.
    
    Returns:
        str: Os dados descriptografados.
    """
    # Decodificar os dados criptografados de base64
    conteudo = base64.b64decode(dados_criptografados)

    # Extrair o salt, IV e os dados criptografados
    salt = conteudo[:16]
    iv = conteudo[16:32]
    dados_criptografados = conteudo[32:]

    # Gerar a chave a partir da senha e do salt
    chave = gerar_chave(senha, salt)

    # Criar o objeto de descriptografia AES
    cipher = AES.new(chave, AES.MODE_CBC, iv)

    # Descriptografar os dados
    dados_preenchidos = cipher.decrypt(dados_criptografados)

    # Remover o padding dos dados
    return unpad(dados_preenchidos, AES.block_size).decode()

# Exemplo de uso

