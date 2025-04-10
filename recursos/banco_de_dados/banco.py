from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from hashlib import sha256
import logging
# Definir a base para as tabelas
Base_funcionario = declarative_base()
Base_clientes=declarative_base()
# Definir a tabela funcionarios
class Funcionarios(Base_funcionario):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    senha = Column(String(100))

# Definir a tabela clientes
class Clientes(Base_clientes):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cpf = Column(Integer)

# Classe de conexão com o banco de dados
class Conexao_funcionario:
    def __init__(self):
        # Criar o engine e a sessão
        try:
            caminho_banco="recursos/banco_de_dados/funcionarios.db"
            self.engine = create_engine(f"sqlite:///{caminho_banco}")
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
        except FileNotFoundError:
            print("erro na criaçao ")
        except Exception as e:
            print(f"erro ao tentar criar o banco de dados: {str(e)} ")  

        # Criar as tabelas no banco de dados
        Base_funcionario.metadata.create_all(self.engine)
    def novo_funcionarios(self, usuario, senha):
        # Criar um novo usuário
        try:
            novo_funcionario = Funcionarios(usuario=usuario, senha=senha)
            self.session.add(novo_funcionario)
            self.session.commit()
            print("Usuário inserido com sucesso!")
        except Exception as e:
            print(f"erro ao adicionar funcionarios: {str(e)} ")  
        
    def listar_funcionarios(self):
        # Listar todos os usuários
        try:
            usuarios = self.session.query(Funcionarios).all()
            for usuario in usuarios:
                return usuario.usuario,usuario.senha
        
        except Exception as e:
            print(f"erro ao tentar listar funcionarios: {str(e)} ")  
        
class Conexao_clientes:
    def __init__(self):
        # Criar o engine e a sessão
        try:
            caminho_banco="recursos/banco_de_dados/clientes.bin"
            self.engine = create_engine(f"sqlite:///{caminho_banco}")
            self.Session = sessionmaker(bind=self.engine)
            self.session = self.Session()
        # Criar as tabelas no banco de dados
            Base_clientes.metadata.create_all(self.engine)
        except Exception as e:
            print(f"erro ao tentar criar o banco de dados: {str(e)} ")  
        
    def novos_clientes(self,clientes,Cpf):
        """
        Adiciona um novo cliente ao banco de dados.
    
        Args:
            nome: Nome do cliente
            cpf: CPF do cliente (apenas números)
        except: mostar o erro
        """
        try:
            novo_cliente=Clientes(cliente=clientes,cpf=Cpf)
            self.session.add(novo_cliente)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"erro ao adicionar clientes: {str(e)} ")  
    def lista_clientes(self):
        try:
            clientes=self.session.query(Clientes).all()
            
            for cliente in clientes:
                print(f"ID: {cliente.id}, nome: {cliente.nome}, cpf: {cliente.cpf}")
            
        except Exception as e:
            print(f"erro ao listar clientes: {str(e)}")
            
c=Conexao_clientes()
c.lista_clientes()