from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from recursos.banco_de_dados.criptografia.cripto import criptografar_dados,descriptografar_dados




#esta faltando incluir a libs logging pra ter um tratamento de erro melhor
#fazer as docstrings daas funçoes 
#fazer a validaçao do cpf 



Base=declarative_base()
# Definir a tabela funcionarios
class Funcionarios_base(Base):
    """serve pra fazer as tabelas no arquivo sql"""
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50))
    senha = Column(String(100))

# Definir a tabela clientes
class Clientes_base(Base):
    """serve pra fazer as tabelas no arquivo sql"""
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cpf = Column(String)
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
                print("erro")
            novo_cliente=Clientes_base(clientes_criptografado,cpf=cpf_criptografado)
            self.session.add(novo_cliente)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"erro ao adicionar clientes: {str(e)} ")  
    def lista_clientes(self,senha):
        """
        lista todos os clientes.
    
        Args:
            senha: senha necessaria pra descriptografar
        except: mostar o erro
        """
        try:
            clientes=self.session.query(Clientes_base).all()
            
            for cliente in clientes:
                print(f"ID: {cliente.id}, nome: {cliente.nome}, cpf: {cliente.cpf}")
            
        except Exception as e:
            print(f"erro ao listar clientes: {str(e)}")
            



