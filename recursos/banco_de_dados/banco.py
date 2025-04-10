from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from hashlib import sha256
# Definir a base para as tabelas
Base_funcionario = declarative_base()
Base_clientes=declarative_base()
# Definir a classe Usuario
class Funcionarios(Base_funcionario):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    senha = Column(String(100))

# Definir a classe Clientes
class Clientes(Base_clientes):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cpf = Column(Integer)

# Classe de conexão com o banco de dados
class Conexao_funcionario:
    def __init__(self):
        # Criar o engine e a sessão
        self.engine = create_engine("sqlite:///funcionarios.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Criar as tabelas no banco de dados
        Base_funcionario.metadata.create_all(self.engine)
    def novo_funcionarios(self, usuario, senha):
        # Criar um novo usuário
        novo_funcionario = Funcionarios(usuario=usuario, senha=senha)
        self.session.add(novo_funcionario)
        self.session.commit()
        print("Usuário inserido com sucesso!")
    def listar_funcionarios(self):
        # Listar todos os usuários
            usuarios = self.session.query(Funcionarios).all()
            for usuario in usuarios:
                return usuario.usuario,usuario.senha
        
class Conexao_clientes:
    def __init__(self):
        # Criar o engine e a sessão
        self.engine = create_engine("sqlite:///clientes.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        # Criar as tabelas no banco de dados
        Base_clientes.metadata.create_all(self.engine)
    def novos_clientes(self,clientes,Cpf):
        novo_cliente=Clientes(cliente=clientes,cpf=Cpf)
        self.session.add(novo_cliente)
        self.session.commit()
    def lista_clientes(self):
        clientes=self.session.query(Clientes).all()
        for cliente in clientes:
            print(f"ID: {cliente.id}, nome: {cliente.nome}, cpf: {cliente.cpf}")
minha_senha="admin".encode()
senha_criptografada=sha256(minha_senha).digest()
#print(senha_criptografada)


# Exemplo de uso


#conexao.novo_funcionarios(senha_criptografada,senha_criptografada)
#conexao.listar_usuarios()
#conexao.novo_usuario("admin","admin")