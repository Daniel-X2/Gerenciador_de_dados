
import customtkinter
from recursos.banco_de_dados.criptografia.cripto import criptografar_dados,descriptografar_dados
from PIL import Image, ImageTk
import os
from recursos.login.toplevel import toplevel
from recursos.banco_de_dados.banco import Funcionario,Clientes

class Tela_login(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("794x529")
        self.resizable(False,False)
        self.title("login CRUD")
        self.variaveis_iniciais()
        self.funçoes_init()
    def funçoes_init(self):
        self.plano_de_fundo()
        self.entrada()
        self.esqueceu_senha()
        self.botao_config()
        self.botao_veri()       
    def variaveis_iniciais(self):
        #inicia a variavel de verificaçao se foi destruido
        self.destruiu=False
        #aqui se refere ao toplevel para que ele nao inicie na doida
        self.top=None
        #string da entrada do usuario
        self.usuario=customtkinter.StringVar()
        #string da entrada da senha
        self.senha=customtkinter.StringVar()
    def entrada(self):
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
        if self.top is None or not self.top.winfo_exists():
            self.top=toplevel.Apptop()
        else:
            self.top.focus()
    def texto(self):
        text="""usuario: admin | senha: admin"""
        label=customtkinter.CTkLabel(self,
                                     text=text,
                                     bg_color="#242424",
                                     text_color="white")
        label.place(x=0,y=400)
        #ele vai chamar a funçao pra destruir a label depois de 6 segundos
        self.after(6000,label.destroy)
    def botao_veri(self):
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
        #preferi fazer uma validaçao simples do que criptografar
        self.verificar_senha_usu=self.usuario.get()
        self.verificar_usuario=self.senha.get()
        
        funcionario=Funcionario()
    
        usuario_banco=descriptografar_dados(funcionario.listar_funcionarios()[0],self.verificar_usuario)
        senha_banco=descriptografar_dados(funcionario.listar_funcionarios()[1],self.verificar_senha_usu)
        
        #primeira verificaçao do usuario
        if usuario_banco==self.verificar_usuario and self.verificar_senha_usu==senha_banco:
            self.destruiu = True
            self.destruir()
        else:
            pass
    def caminho(self,path,file,x,y):
        diretorio=os.path.dirname(__file__)
        caminho=os.path.join(diretorio,path)
        arquivo=os.path.join(caminho,file)
        imagem=Image.open(arquivo)
        #aqui coloca a imagem
        img_ctk=customtkinter.CTkImage(imagem,size=(x,y))
        return img_ctk
    def destruir(self):
        self.usuario_atual=self.usuario.get()
        self.senha_atual=self.senha.get()
        
        Tela_login.destroy(self)