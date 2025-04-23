from PIL import Image

import customtkinter
class DashBoard(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text="dashboard")
        self.label.place(x=0,y=0)
        n1=customtkinter.CTkButton(self)
        n1.place(x=50,y=50)
        






class OverView(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text="Bem Vindo!",font=("",30),text_color="black")
        self.label.place(x=40,y=30)
        texto=customtkinter.CTkLabel(self,text="Aqui esta o resumo das informaçoes do Sistema",font=("",15),text_color="black")
        texto.place(x=30,y=80)

        self.fileira_um()
        self.fileira_dois()
        self.fileira_tres()
        self.fileira_quarto()
        self.frame()
        self.fileira_quinta()
        self.fileira_sexta()
        self.grafico()
    def grafico(self):
        img_grafico=customtkinter.CTkImage(Image.open("recursos/grafico/imagem_grafico/grafico.png"),size=(400,200))
        label_grafico=customtkinter.CTkLabel(self,text="",image=img_grafico,fg_color="gray",bg_color="white",corner_radius=5,width=410,height=210)
        label_grafico.place(x=300,y=250)    
    def frame(self):

        frame=customtkinter.CTkFrame(self,corner_radius=10)
        frame.place(x=50,y=500)

        frame1=customtkinter.CTkFrame(self)
        frame1.place(x=300,y=500)

        frame2=customtkinter.CTkFrame(self)
        frame2.place(x=600,y=500)


        frame3=customtkinter.CTkFrame(self)
        frame3.place(x=900,y=500)
    def fileira_um(self):
        #posso pegar uma label fazia e simular uma extensao dessa primeira label pra ficar algo mais boniyo
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=70)   
        texto_usuario.place(x=30,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Novos Usuarios",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=30,y=180)
    def fileira_dois(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=70)   
        texto_usuario.place(x=200,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Clientes ativos",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=200,y=180)
    def fileira_tres(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""69%""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=70)   
        texto_usuario.place(x=750,y=150)
        texto_new=customtkinter.CTkLabel(self,text="System Load",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=750,y=180)
    def fileira_quarto(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""10%""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=70)   
        texto_usuario.place(x=900,y=150)
        texto_new=customtkinter.CTkLabel(self,text="devoluçao",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=900,y=180)
    def fileira_quinta(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""$5.50""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=70)   
        texto_usuario.place(x=350,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Valor do Dolar",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=350,y=180)
    def fileira_sexta(self):
        texto_usuario=customtkinter.CTkLabel(self,text_color="black",text="""17""",anchor="n",font=("",27),fg_color="#70CFF9",corner_radius=10,width=120,height=70,bg_color="#89CFF0")   
        texto_usuario.place(x=520,y=150)
        texto_new=customtkinter.CTkLabel(self,text_color="black",text="Reclamaçoes",fg_color="#70CFF9",corner_radius=0,width=120,bg_color="#89CFF0")
        texto_new.place(x=520,y=180)
class Users(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text="users")
        self.label.place(x=0,y=0)



class Client(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text="client")
        
class Analytic(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text="analitic")
class Settings(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text="setting")

class Support(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text="Suport")

class Report (customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self,text="report")