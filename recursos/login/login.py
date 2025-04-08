import customtkinter
from PIL import Image, ImageTk
import os
import webbrowser 
class Tela_login(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("794x529")
        self.resizable(False,False)
        self.title("login CRUD")
        self.funçoes_init()
        #self.verificar_senha()
    def funçoes_init(self):
        self.plano_de_fundo()
        self.entrada()
        self.esqueceu_senha()
    def entrada(self):
        #text_usu.place(x=250,y=200)
        #entrada do usuario
        self.usuario=customtkinter.StringVar()
        entrada_usu=customtkinter.CTkEntry(self.bg_label,fg_color="gray",textvariable=self.usuario,border_color="gray",bg_color="gray",width=300,height=33,font=("arial",17))
        entrada_usu.place(x=250,y=230)
        
        
        #entrada da senha
        self.senha=customtkinter.StringVar()
        entrada_senha=customtkinter.CTkEntry(self.bg_label,fg_color="gray",textvariable=self.senha,border_color="gray",bg_color="gray",width=300,height=33,font=("arial",17))
        entrada_senha.place(x=250,y=310)
    def verificar_senha(self):
        print(self.senha.get())
        self.after(2000,self.verificar_senha)
    def plano_de_fundo(self):
        #encontrar o caminho do arquivo
        dirname=os.path.dirname(__file__)
        caminho=os.path.join(dirname,"imagens_login")
        caminhos=os.path.join(caminho,"1.png")
        #abrindo o aquivo
        imagem=Image.open(caminhos)
        imagem=imagem.resize((794,529))
        #aqui coloca a imagem 
        self.bg_image=customtkinter.CTkImage(imagem,size=(794,529))
        self.bg_label=customtkinter.CTkLabel(self,image=self.bg_image,text='')
        self.bg_label.place(x=0,y=0)
        #aqui fica os caminhos do png da aguia 
        dir_aguia=os.path.dirname(__file__)
        caminho_login=os.path.join(dir_aguia,"imagens_login")
        caminhos_aguia=os.path.join(caminho_login,"login.png")
        imagem_aguia=Image.open(caminhos_aguia)
        #aqui coloca a imagem
        aguia_img=customtkinter.CTkImage(imagem_aguia,size=(300,300))
        label_aguia=customtkinter.CTkLabel(self.bg_label,text="",image=aguia_img)
        #label_aguia.place(x=250,y=-40)
    def esqueceu_senha(self):
        botao_esqueceu=customtkinter.CTkButton(self.bg_label,text="esqueceu a senha?",width=80,corner_radius=0,command=self.abrir_github)
        botao_esqueceu.place(x=435,y=345)
    def abrir_github(self):
        url="https://github.com/Daniel-X2"
        webbrowser.open(url)



tela_login=Tela_login()
tela_login.mainloop() 