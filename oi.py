from hashlib import sha256

minha_senha="admin".encode()
senha_criptografada=sha256(minha_senha).digest()

