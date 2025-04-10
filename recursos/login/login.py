import customtkinter
from hashlib import sha256
from PIL import Image, ImageTk
import os
from recursos.login.toplevel import toplevel
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
        entrada_usu=customtkinter.CTkEntry(self,fg_color="gray",textvariable=self.usuario,border_color="gray",bg_color="gray",width=300,height=33,font=("arial",17))
        entrada_usu.place(x=250,y=230)

        #entrada da senha
        entrada_senha=customtkinter.CTkEntry(self,fg_color="gray",textvariable=self.senha,border_color="gray",bg_color="gray",width=300,height=33,font=("arial",17))
        entrada_senha.place(x=250,y=310)
    def plano_de_fundo(self):
        #abrindo o aquivo
        imagem=self.caminho("imagens_login","1.png",794,529)
        #aqui coloca a imagem
        self.bg_label=customtkinter.CTkLabel(self,image=imagem,text='')
        self.bg_label.place(x=0,y=0)
    def esqueceu_senha(self):
        botao_esqueceu=customtkinter.CTkButton(self,text="esqueceu a senha?",width=0,corner_radius=10,command=self.texto,bg_color="#c19073")
        botao_esqueceu.place(x=435,y=355)
    def botao_config(self):
        imagem=self.caminho("imagens_login","canto.png",50,50)
        botao=customtkinter.CTkButton(self,text="",width=50,height=50,corner_radius=0,image=imagem,border_width=0,border_spacing=0,fg_color="#323e50",command=self.abrir_janela)
        botao.place(x=0,y=480)
    def abrir_janela(self):
        if self.top is None or not self.top.winfo_exists():
            self.top=toplevel.Apptop()
        else:
            self.top.focus()
    def texto(self):
        text="""usuario: admin | senha: admin"""
        label=customtkinter.CTkLabel(self,text=text,bg_color="#242424",text_color="white")
        label.place(x=0,y=400)
        #ele vai chamar a funçao pra destruir a label depois de 6 segundos
        self.after(6000,label.destroy)
    def botao_veri(self):
        botao=customtkinter.CTkButton(self,text="confirmar",width=50,corner_radius=0,command=self.verificar_senha)
        botao.place(x=370,y=400)
    def verificar_senha(self):
        #preferi fazer uma validaçao simples do que criptografar
        self.verificar_senha_usu=sha256(self.senha.get().encode()).digest()
        self.verificar_usuario=sha256(self.usuario.get().encode()).digest()
        usuario_banco=""
        senha_banco=""
        #primeira verificaçao do usuario
        if usuario_banco==self.verificar_usuario and self.verificar_senha_usu==senha_banco:
            self.destruiu = True
            self.destruir()
        else:
            print
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