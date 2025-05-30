from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from recursos.banco_de_dados.criptografia.cripto import descriptografar_dados, criptografar_dados
import json

#
Base = declarative_base()
# Definir a tabela funcionarios
class Funcionarios_base(Base):
    """
    Modelo da tabela 'funcionarios' para o banco de dados.
    Armazena os dados criptografados dos funcionários.
    """
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    dados_funcionario = Column(String)

# Definir a tabela clientes
class Clientes_base(Base):
    """
    Modelo da tabela 'clientes' para o banco de dados.
    Armazena os dados criptografados dos clientes.
    """
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    dados_clientes = Column(String)

# Classe de conexão com o banco de dados
class Conexao():
    """
    Classe responsável por criar e gerenciar a conexão com o banco de dados.
    Cria o banco caso não exista.
    """
    def __init__(self):
        """
        Inicializa a classe Conexao.
        """
        pass

    def sessao(self, caminho):
        """
        Cria uma sessão com o banco de dados SQLite no caminho especificado.
        Se o banco não existir, ele será criado.

        Args:
            caminho (str): Caminho do arquivo do banco de dados.

        Returns:
            session: Sessão do SQLAlchemy para interações com o banco.
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
    """
    Classe para operações CRUD relacionadas aos funcionários no banco de dados.
    """
    def __init__(self):
        """
        Inicializa a classe Funcionario e cria uma sessão com o banco de dados.
        """
        super().__init__()
        self.session = Conexao().sessao(caminho="recursos/banco_de_dados/banco.db")

    def novo_funcionario(self, dados, chave_criptografar):
        """
        Adiciona um novo funcionário ao banco de dados.

        Args:
            dados (dict): Dados do funcionário a serem salvos.
            chave_criptografar (str): Senha para criptografar os dados.
        """
        try:
            dados_json = json.dumps(dados)
            dados_criptografados = criptografar_dados(dados_json, chave_criptografar)
            novo_funcionario = Funcionarios_base(dados_funcionario=dados_criptografados)
            self.session.add(novo_funcionario)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"erro ao adicionar funcionario: {str(e)} ")  

    def lista_funcionario(self, numero, senha):
        """
        Lista e descriptografa os dados de um funcionário pelo índice.

        Args:
            numero (int): Índice do funcionário na lista.
            senha (str): Senha necessária para descriptografar os dados.

        Returns:
            dict|bool: Dados do funcionário descriptografados ou False se não encontrado/erro.
        """
        try:
            funcionario = self.session.query(Funcionarios_base).all()
            if len(funcionario)==0:
                return False
            if funcionario:
                var_funcionario = funcionario[numero].dados_funcionario
                
                dados_descriptografados = descriptografar_dados(var_funcionario, senha)
                print(dados_descriptografados)
                dados = json.loads(dados_descriptografados)
                
                return dados
        except IndexError:
            return False
        except Exception as e:
            print(f"erro ao listar funcionarios: {str(e)}")

    def delete(self, id):
        """
        Deleta um funcionário do banco de dados pelo ID.

        Args:
            id (int): ID do funcionário a ser deletado.

        Returns:
            bool: True se deletado com sucesso, False caso contrário.
        """
        try:
            Funcionario_deletado = self.session.query(Funcionarios_base).filter_by(id=id).first()
            if Funcionario_deletado:
                self.session.delete(Funcionario_deletado)
                self.session.commit()
                return True
            else:
                return False
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao deletar cliente: {str(e)}")
            return False
    
class Clientes():
    """
    Classe para operações CRUD relacionadas aos clientes no banco de dados.
    """
    def __init__(self):
        """
        Inicializa a classe Clientes e cria uma sessão com o banco de dados.
        """
        self.session = Conexao().sessao(caminho="recursos/banco_de_dados/banco.db")

    def novos_clientes(self, dados, chave_criptografar):
        """
        Adiciona um novo cliente ao banco de dados.

        Args:
            dados (dict): Dados do cliente a serem salvos.
            chave_criptografar (str): Senha para criptografar os dados.
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
        Lista e descriptografa os dados de um cliente pelo índice.

        Args:
            numero (int): Índice do cliente na lista.
            senha (str): Senha necessária para descriptografar os dados.

        Returns:
            dict|bool: Dados do cliente descriptografados ou False se não encontrado/erro.
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

    def delete(self, iD):
        """
        Deleta um cliente do banco de dados pelo ID.

        Args:
            iD (int): ID do cliente a ser deletado.

        Returns:
            bool: True se deletado com sucesso, False caso contrário.
        """
        try:
            cliente_deletado = self.session.query(Clientes_base).filter_by(id=iD).first()
            if cliente_deletado:
                self.session.delete(cliente_deletado)
                self.session.commit()
                return True
            else:
                return False
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao deletar cliente: {str(e)}")
            return False
