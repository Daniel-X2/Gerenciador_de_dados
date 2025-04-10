from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Definir a base para as tabelas
Base = declarative_base()
# Definir a classe Usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    senha = Column(String(100))

# Definir a classe Clientes
class Clientes(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cpf = Column(Integer)

# Classe de conexão com o banco de dados
class Conexao:
    def __init__(self):
        # Criar o engine e a sessão
        self.engine = create_engine("sqlite:///meubanco.db")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Criar as tabelas no banco de dados
        Base.metadata.create_all(self.engine)
    def novos_clientes(self,clientes,Cpf):
        novo_cliente=Clientes(cliente=clientes,cpf=Cpf)
        self.session.add(novo_cliente)
        self.session.commit()
    def novo_usuario(self, usuario, senha):
        # Criar um novo usuário
        novo_usuario = Usuario(usuario=usuario, senha=senha)
        self.session.add(novo_usuario)
        self.session.commit()
        print("Usuário inserido com sucesso!")

    def listar_usuarios(self):
        # Listar todos os usuários
        try:
            usuarios = self.session.query(Usuario).all()
            for usuario in usuarios:
                print(f"ID: {usuario.id}, Usuário: {usuario.usuario}, Senha: {usuario.senha}")
        except:
            print("erro na lista de usuarios")
    def lista_clientes(self):
        clientes=self.session.query(Clientes).all()
        for cliente in clientes:
            print(f"ID: {cliente.id}, nome: {cliente.nome}, cpf: {cliente.cpf}")



# Exemplo de uso

conexao = Conexao()
conexao.novo_usuario()
conexao.listar_usuarios()