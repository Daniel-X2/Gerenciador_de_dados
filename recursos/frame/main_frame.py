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
        self.bem_vindo()
        self.frames()
        self.grafico()
    def bem_vindo(self):
        texto_bem_vindo = customtkinter.CTkLabel(self,text="Bem Vindo!",font=("arial",30,"bold"),text_color="black")
        texto_bem_vindo.place(x=40,y=30)
        texto_resumo=customtkinter.CTkLabel(self,text="Aqui esta o resumo das informaçoes do Sistema",font=("",15),text_color="black")
        texto_resumo.place(x=30,y=80)
    def grafico(self):
        img_grafico=customtkinter.CTkImage(Image.open("recursos/grafico/imagem_grafico/grafico.png"),size=(700,250))
        label_grafico=customtkinter.CTkLabel(self,text="",image=img_grafico,fg_color="#89CFF0",bg_color="#89CFF0",)
        label_grafico.place(x=200,y=234)
            
    def frames(self):

        frame_acao=customtkinter.CTkFrame(self,corner_radius=10)
        frame_acao.place(x=50,y=500)

        frame_atividade=customtkinter.CTkFrame(self)
        frame_atividade.place(x=300,y=500)

        frame_report=customtkinter.CTkFrame(self)
        frame_report.place(x=600,y=500)


        frame_status=customtkinter.CTkFrame(self)
        frame_status.place(x=900,y=500)
    def card_usuario(self):
        #posso pegar uma label fazia e simular uma extensao dessa primeira label pra ficar algo mais boniyo
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="#4DA8DA",corner_radius=5,width=120,height=70,text_color="black")   
        texto_usuario.place(x=60,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Novos Usuarios",fg_color="#4DA8DA",corner_radius=5,width=120,bg_color="#4DA8DA",text_color="black")
        texto_new.place(x=60,y=180)
    def card_clientes(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="#4CAF50",corner_radius=5,width=120,height=70,text_color="black")   
        texto_usuario.place(x=245,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Clientes ativos",fg_color="#4CAF50",width=120,bg_color="#4CAF50",text_color="black")
        texto_new.place(x=245,y=180)
    def card_sistema(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""69%""",anchor="n",font=("",27),text_color="black",fg_color="#FB8C00",corner_radius=5,width=120,height=70)   
        texto_usuario.place(x=785,y=150)
        texto_new=customtkinter.CTkLabel(self,text="System Load",fg_color="#FB8C00",width=120,bg_color="gray",text_color="black")
        texto_new.place(x=785,y=180)
    def card_devolucao(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""10%""",anchor="n",font=("",27),fg_color="#EEDC82",corner_radius=5,width=120,height=70,text_color="black")   
        texto_usuario.place(x=605,y=150)
        texto_new=customtkinter.CTkLabel(self,text="devoluçao",fg_color="#EEDC82",width=120,bg_color="#EEDC82",text_color="black")
        texto_new.place(x=605,y=180)
    def card_dolar(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""$5.50""",anchor="n",text_color="black",font=("",27),fg_color="#00BFA6",corner_radius=5,width=120,height=70)   
        texto_usuario.place(x=425,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Valor do Dolar",text_color="black",fg_color="#00BFA6",width=120)
        texto_new.place(x=425,y=180)
    def card_reclamacao(self):
        texto_usuario=customtkinter.CTkLabel(self,text_color="black",text="""17""",anchor="n",font=("",27),fg_color="#FF6F61",corner_radius=10,width=120,height=70,bg_color="#89CFF0")   
        texto_usuario.place(x=980,y=150)
        texto_new=customtkinter.CTkLabel(self,text_color="black",text="Reclamaçoes",fg_color="#FF6F61",corner_radius=0,width=120,bg_color="#89CFF0")
        texto_new.place(x=980,y=180)
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