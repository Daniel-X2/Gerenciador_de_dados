import customtkinter
from recursos.banco_de_dados.criptografia.cripto import criptografar_dados,descriptografar_dados
from PIL import Image, ImageTk
import os
from recursos.login.toplevel import toplevel
from recursos.banco_de_dados.banco import Funcionario,Clientes

class Tela_login(customtkinter.CTk):
    """
    Janela de login principal do sistema CRUD.
    Permite autenticação do usuário e acesso à aplicação principal.
    """

    def __init__(self, fg_color = None, **kwargs):
        """
        Inicializa a janela de login, configura o layout e variáveis iniciais.

        Args:
            fg_color (str, opcional): Cor de fundo da janela.
            **kwargs: Argumentos adicionais para customtkinter.CTk.
        """
        super().__init__(fg_color, **kwargs)
        self.geometry("794x529")
        self.resizable(False,False)
        self.title("login CRUD")
        self.variaveis_iniciais()
        self.funcoes_init()

    def funcoes_init(self):
        """
        Inicializa os componentes da interface, como plano de fundo,
        campos de entrada, botões e eventos.
        """
        self.plano_de_fundo()
        self.entrada()
        self.esqueceu_senha()
        self.botao_config()
        self.botao_veri()       

    def variaveis_iniciais(self):
        """
        Define variáveis iniciais para controle de estado e campos de entrada.
        """
        #inicia a variavel de verificaçao se foi destruido
        self.destruiu=False
        #aqui se refere ao toplevel para que ele nao inicie na doida
        self.top=None
        #string da entrada do usuario
        self.usuario=customtkinter.StringVar()
        #string da entrada da senha
        self.senha=customtkinter.StringVar()

    def entrada(self):
        """
        Cria e posiciona os campos de entrada de usuário e senha na tela.
        """
        #entrada do usuario
        texto_usu=customtkinter.CTkLabel(self,text="USUARIO",fg_color="#4714b2")
        texto_usu.place(x=250,y=200)
        entrada_usu=customtkinter.CTkEntry(self,fg_color="white",
                                            textvariable=self.usuario,
                                            bg_color="#4714b2",
                                            width=300,
                                            height=33,
                                            font=("arial",17),
                                            corner_radius=10,text_color="black")
        entrada_usu.place(x=250,y=230)
        texto_senha=customtkinter.CTkLabel(self,text="SENHA",fg_color="#4714b2")
        texto_senha.place(x=250,y=280)
        #entrada da senha
        entrada_senha=customtkinter.CTkEntry(self,fg_color="white",
                                                textvariable=self.senha,
                                                bg_color="#4714b2",
                                                width=300,
                                                height=33,
                                                font=("arial",17),
                                                corner_radius=10,
                                                text_color="black",
                                                )
        entrada_senha.place(x=250,y=310)

    def plano_de_fundo(self):
        """
        Configura o plano de fundo da tela de login e exibe a imagem do falcão.
        """
        self.bg_label=customtkinter.CTkLabel(self,text='',
                                             bg_color="#4714b2",
                                             width=794,
                                             height=529)
        self.bg_label.place(x=0,y=0)


        imagem=self.caminho("imagens_login","falcao_main.png",200,200)
        aguia=customtkinter.CTkLabel(self,text="",
                                     bg_color="#4714b2",
                                     image=imagem)
        aguia.place(x=300,y=0)

    def esqueceu_senha(self):
        """
        Cria o botão 'esqueceu a senha?' e define sua ação.
        """
        botao_esqueceu=customtkinter.CTkButton(self,
                                                text="esqueceu a senha?",
                                                width=0,
                                                corner_radius=50,
                                                command=self.texto,
                                                bg_color="#4714b2",
                                                fg_color="white",
                                                text_color="black",
                                                font=("ariel",13),
                                                hover_color="#4c6ef6")
        botao_esqueceu.place(x=420,y=355)

    def botao_config(self):
        """
        Cria o botão de configurações e define sua ação para abrir a janela de configurações.
        """
        imagem=self.caminho("imagens_login","definicoes1.png",40,40)
        botao=customtkinter.CTkButton(self,text="",
                                      width=10,
                                      height=10,
                                      corner_radius=50,
                                      image=imagem,
                                      border_width=0,
                                      bg_color="#4714b2",
                                      fg_color="#4714b2",
                                      hover_color="#4c6ef6",
                                      command=self.abrir_janela)
        botao.place(x=0,y=485)

    def abrir_janela(self):
        """
        Abre a janela de configurações (toplevel) se ainda não estiver aberta.
        """
        if self.top is None or not self.top.winfo_exists():
            self.top=toplevel.Apptop()
        else:
            self.top.focus()

    def texto(self):
        """
        Exibe temporariamente na tela as credenciais padrão do sistema.
        """
        text="""usuario: admin | senha: admin"""
        label=customtkinter.CTkLabel(self,
                                     text=text,
                                     bg_color="#242424",
                                     text_color="white")
        label.place(x=0,y=400)
        #ele vai chamar a funçao pra destruir a label depois de 6 segundos
        self.after(6000,label.destroy)

    def botao_veri(self):
        """
        Cria o botão de confirmação de login e define sua ação.
        """
        botao=customtkinter.CTkButton(self,text="confirmar ",
                                        width=50,
                                        corner_radius=50,
                                        command=self.verificar_senha,
                                        bg_color="#4714b2",
                                        fg_color="white",
                                        text_color="black",
                                        hover_color="#4c6ef6")
        botao.place(x=353,y=400)

    def verificar_senha(self):
        """
        Realiza a verificação da senha e encerra a tela de login.
        """
        self.destruiu = True
        self.destruir()
        
    def caminho(self, path, file, x, y):
        """
        Monta o caminho absoluto para uma imagem e retorna um objeto CTkImage.

        Args:
            path (str): Subdiretório onde está a imagem.
            file (str): Nome do arquivo de imagem.
            x (int): Largura da imagem.
            y (int): Altura da imagem.

        Returns:
            customtkinter.CTkImage: Imagem carregada e redimensionada.
        """
        diretorio=os.path.dirname(__file__)
        caminho=os.path.join(diretorio,path)
        arquivo=os.path.join(caminho,file)
        imagem=Image.open(arquivo)
        #aqui coloca a imagem
        img_ctk=customtkinter.CTkImage(imagem,size=(x,y))
        return img_ctk

    def destruir(self):
        """
        Salva o usuário e senha digitados e destrói a janela de login.
        """
        self.usuario_atual=self.usuario.get()
        self.senha_atual=self.senha.get()
        
        Tela_login.destroy(self)