from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Conexão com o banco
engine = create_engine("sqlite:///meubanco.db")
Base = declarative_base()

# Definir o modelo
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(100))

# Criar a tabela no banco
Base.metadata.create_all(engine)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criar um novo usuário
novo_usuario = Usuario(nome="Maria", email="maria@example.com")
session.add(novo_usuario)
session.commit()

usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")