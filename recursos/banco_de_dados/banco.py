from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from criptografia.cripto import criptografar_dados,descriptografar_dados

Base=declarative_base()
# Definir a tabela funcionarios
class Funcionarios(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    senha = Column(String(100))

# Definir a tabela clientes
class Clientes(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cpf = Column(String)
# Classe de conexão com o banco de dados
class Conexao():
    def __init__(self):
        pass
    def sessao(self,caminho):
        # Criar o engine e a sessão
        try:
            caminho_banco=caminho
            self.engine = create_engine(f"sqlite:///{caminho_banco}")
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
        except FileNotFoundError:
            print("erro na criaçao ")
        except Exception as e:
            print(f"erro ao tentar criar o banco de dados: {str(e)} ")  
        # Criar as tabelas no banco de dados
        Base.metadata.create_all(self.engine)
        return self.session
class Funcionario():
    def __init__(self):
        super().__init__()
        self.session=Conexao().sessao(caminho="recursos/banco_de_dados/banco.db")

    def novo_funcionarios(self, usuario, senha,chave_criptografar):
        # Criar um novo usuário
        try:
            usuario_criptografado=criptografar_dados(usuario,chave_criptografar)
            senha_criptografado=criptografar_dados(senha,chave_criptografar)
            try:
                novo_funcionario = Funcionarios(usuario=usuario_criptografado, senha=senha_criptografado)
                self.session.add(novo_funcionario)
                self.session.commit()
                print("Usuário inserido com sucesso!")
            except Exception as e:
                print(f"erro ao adicionar funcionarios: {str(e)} ")  
        except:
            print
    def listar_funcionarios(self):
        # Listar todos os usuários
        try:
            usuarios = self.session.query(Funcionarios).all()
            for usuario in usuarios:
                return usuario.usuario,usuario.senha
        
        except Exception as e:
            print(f"erro ao tentar listar funcionarios: {str(e)} ")  
class Clientes():
    def novos_clientes(self,clientes,cpf,chave_criptografar):
        """
        Adiciona um novo cliente ao banco de dados.
    
        Args:
            nome: Nome do cliente
            cpf: CPF do cliente (apenas números)
        except: mostar o erro
        """
        try:
            try:
                clientes_criptografado=criptografar_dados(clientes,cpf,chave_criptografar)
                cpf_criptografado=criptografar_dados(clientes,cpf,chave_criptografar)
            except:
                print
            novo_cliente=Clientes(cliente=clientes_criptografado,cpf=cpf_criptografado)
            self.session.add(novo_cliente)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"erro ao adicionar clientes: {str(e)} ")  
    def lista_clientes(self,senha):
        try:
            clientes=self.session.query(Clientes).all()
            
            for cliente in clientes:
                print(f"ID: {cliente.id}, nome: {cliente.nome}, cpf: {cliente.cpf}")
            
        except Exception as e:
            print(f"erro ao listar clientes: {str(e)}")
            


n2=Funcionario().listar_funcionarios()
print(descriptografar_dados(n2[1],"admin"))