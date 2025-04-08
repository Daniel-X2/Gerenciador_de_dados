import customtkinter
import os
from PIL import Image
import webbrowser 
class Apptop(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.resizable(False,False)
        self.title("help")

        self.funçoes_init()
    def funçoes_init(self):
        self.fundo()
        self.falçao()
        self.botao_github()
       
    def fundo(self):    
        #plano de fundo
        plano_de_fundo=customtkinter.CTkLabel(self,bg_color="#242424",text="",width=600,height=500)
        plano_de_fundo.place(x=0,y=0)

        agradecimentos="""   Bem vindo ao meu projeto 
        fico muito feliz que esteja olhando esse projeto
        se estiver interessado nesse projeto ou em outros basta
        acessar meu github"""
        label_agra=customtkinter.CTkLabel(self,text=agradecimentos,font=("ariel",18),bg_color="#242424",text_color="white")
        label_agra.place(x=40,y=250)
    def botao_github(self):
        dirname=os.path.dirname(__file__)
        caminho_git=os.path.join(dirname,"imagem_top")
        caminho_absoluto=os.path.join(caminho_git,"git.png")
        imagem=customtkinter.CTkImage(Image.open(caminho_absoluto),size=(50,50))
        botao=customtkinter.CTkButton(self,text="",image=imagem,width=0,height=0,fg_color="#242424",command=self.abrir_github)
        botao.place(x=520,y=420)
    def abrir_github(self):
        url="https://github.com/Daniel-X2"
        webbrowser.open(url)
    def falçao(self):
        dirname=os.path.dirname(__file__)
        caminho_falcao=os.path.join(dirname,"imagem_top")
        caminho_absoluto=os.path.join(caminho_falcao,"login.png")
        imagem=customtkinter.CTkImage(Image.open(caminho_absoluto),size=(200,200))
        label=customtkinter.CTkLabel(self,text="", image=imagem,bg_color="#242424")
        label.place(x=200,y=0)

