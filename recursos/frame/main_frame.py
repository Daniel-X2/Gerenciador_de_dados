from pydoc import text
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
        self.label = customtkinter.CTkLabel(self,text="Bem Vindo!",font=("",30))
        self.label.place(x=40,y=30)
        texto=customtkinter.CTkLabel(self,text="Aqui esta o resumo das informaçoes do Sistema",font=("",15))
        texto.place(x=30,y=80)
        self.fileira_um()
        self.fileira_dois()
        self.fileira_tres()
        self.fileira_quarto()
    def fileira_um(self):
        #posso pegar uma label fazia e simular uma extensao dessa primeira label pra ficar algo mais boniyo
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=90)   
        texto_usuario.place(x=30,y=200)
        texto_new=customtkinter.CTkLabel(self,text="Novos Usuarios",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=30,y=250)
    def fileira_dois(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=90)   
        texto_usuario.place(x=200,y=200)
        texto_new=customtkinter.CTkLabel(self,text="Novos Usuarios",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=200,y=250)
    def fileira_tres(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=90)   
        texto_usuario.place(x=350,y=200)
        texto_new=customtkinter.CTkLabel(self,text="Novos Usuarios",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=350,y=250)
    def fileira_quarto(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="gray",corner_radius=5,width=120,height=90)   
        texto_usuario.place(x=500,y=200)
        texto_new=customtkinter.CTkLabel(self,text="Novos Usuarios",fg_color="gray",corner_radius=5,width=120,bg_color="gray")
        texto_new.place(x=500,y=250)    
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