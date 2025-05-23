from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from recursos.banco_de_dados.criptografia.cripto import descriptografar_dados, criptografar_dados
import json


Base = declarative_base()
# Definir a tabela funcionarios
class Funcionarios_base(Base):
    """serve pra fazer as tabelas no arquivo sql"""
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    dados_funcionario=Column(String)

# Definir a tabela clientes
class Clientes_base(Base):
    """serve pra fazer as tabelas no arquivo sql"""
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    dados_clientes = Column(String)
# Classe de conexão com o banco de dados
class Conexao():
    def __init__(self):
        pass
    def sessao(self, caminho):
        """
        usa o banco de dados ou cria se nao tiver um banco de dados
    
        Args:
            caminho: caminho do diretorio
        except: mostar o erro
        """
        try:
            caminho_banco = caminho
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
        self.session = Conexao().sessao(caminho="recursos/banco_de_dados/banco.db")
    def novo_funcionarios(self, dados, chave_criptografar):
        """
        Adiciona um novo cliente ao banco de dados.
        """
        try:
            dados_json = json.dumps(dados)
            dados_criptografado = criptografar_dados(dados_json, chave_criptografar)
            novo_funcionario = Funcionarios_base(dados_funcionario=dados_criptografado)
            self.session.add(novo_funcionario)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"erro ao adicionar funcionario: {str(e)} ")  
    def lista_funcionario(self, numero, senha):
        """
        lista todos os clientes.
    
        Args:
            senha: senha necessaria pra descriptografar
        except: mostar o erro
        """
        try:
            funcionario = self.session.query(Funcionarios_base).all()
            if len(funcionario)==0:
                return False
            if funcionario:
                n1 = funcionario[numero].dados_funcionario
                dados_descriptografados = descriptografar_dados(n1, senha)
                dados = json.loads(dados_descriptografados)
                return dados
        except IndexError:
            return False
        except Exception as e:
            print(f"erro ao listar funcionarios: {str(e)}")
    
class Clientes():
    def __init__(self):
        self.session = Conexao().sessao(caminho="recursos/banco_de_dados/banco.db")
    def novos_clientes(self, dados, chave_criptografar):
        """
        Adiciona um novo cliente ao banco de dados.
        """
        try:
            dados_json = json.dumps(dados)
            dados_criptografado = criptografar_dados(dados_json, chave_criptografar)
            novo_cliente = Clientes_base(dados_clientes=dados_criptografado)
            self.session.add(novo_cliente)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"erro ao adicionar clientes: {str(e)} ")  
    def lista_clientes(self, numero, senha):
        """
        lista todos os clientes.
    
        Args:
            senha: senha necessaria pra descriptografar
        except: mostar o erro
        """
        try:
            cliente = self.session.query(Clientes_base).all()
            if len(cliente)==0:
                return False
            if cliente:
                n1 = cliente[numero].dados_clientes
                dados_descriptografados = descriptografar_dados(n1, senha)
                dados = json.loads(dados_descriptografados)
                return dados
        except IndexError:
            return False
        except Exception as e:
            print(f"erro ao listar clientes: {str(e)}")

