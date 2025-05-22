from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from criptografia.cripto import descriptografar_dados,criptografar_dados
import json


Base=declarative_base()
# Definir a tabela funcionarios
class Funcionarios_base(Base):
    """serve pra fazer as tabelas no arquivo sql"""
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    nome=Column(String)
    email=Column(String)
    cargo=Column(String)
    nivel=Column(String)

# Definir a tabela clientes
class Clientes_base(Base):
    """serve pra fazer as tabelas no arquivo sql"""
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    dados_clientes=Column(String)
# Classe de conexão com o banco de dados
class Conexao():
    def __init__(self):
        pass
    def sessao(self,caminho):
        """
        usa o banco de dados ou cria se nao tiver um banco de dados
    
        Args:
            caminho: caminho do diretorio
        except: mostar o erro
        """
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
        """
        Adiciona um novo cliente ao banco de dados.
    
        Args:
            usuario: nome de usuario
            senha: senha do usuario
        except: mostar o erro
        """
        try:
            usuario_criptografado=criptografar_dados(usuario,chave_criptografar)
            senha_criptografado=criptografar_dados(senha,chave_criptografar)
        except:
            print("erro")
        try:
            novo_funcionario = Funcionarios_base(usuario=usuario_criptografado, senha=senha_criptografado)
            self.session.add(novo_funcionario)
            self.session.commit()
            print("Usuário inserido com sucesso!")
        except Exception as e:
            print(f"erro ao adicionar funcionarios: {str(e)} ")  
    
    def listar_funcionarios(self):
        """
        lista os funcionarios.

        porem lista o primeiro usuario 

        except: mostar o erro
        """
        try:
            usuarios = self.session.query(Funcionarios_base).all()
            for usuario in usuarios:
                return usuario.usuario,usuario.senha
        
        except Exception as e:
            print(f"erro ao tentar listar funcionarios: {str(e)} ")  
class Clientes():
    def __init__(self):
        self.session=Conexao().sessao(caminho="recursos/banco_de_dados/banco.db")
    def novos_clientes(self,dados,chave_criptografar):
        """
        Adiciona um novo cliente ao banco de dados.
    
        Args:
            nome: Nome do cliente
            cpf: CPF do cliente (apenas números)
        except: mostar o erro
        """
        try:
            try:
                dados_criptografado=criptografar_dados(dados,chave_criptografar)
            except:
                print("erro")
            dados_json = json.dumps(dados_criptografado)  # Serializa a lista para string
            novo_cliente = Clientes_base(dados_clientes=dados_json)
            self.session.add(novo_cliente)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"erro ao adicionar clientes: {str(e)} ")  
    def lista_clientes(self,numero,senha):
        """
        lista todos os clientes.
    
        Args:
            senha: senha necessaria pra descriptografar
        except: mostar o erro
        """
        try:

            cliente = self.session.query(Clientes_base).all()

            if cliente:
                n1=cliente[numero].dados_clientes
                dados = json.loads(n1) 
                dados_descriptografados=descriptografar_dados(dados,senha)
                # Desserializa para lista
                return dados_descriptografados
        except IndexError:
            return False
        except Exception as e:
            print(f"erro ao listar clientes: {str(e)}") 

n1=Clientes()
print(n1.lista_clientes(8,"admin"))