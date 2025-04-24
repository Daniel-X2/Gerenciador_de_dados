from PIL import Image

import customtkinter



class DashBoard(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.bem_vindo()
        
        self.grafico()
        self.funcoes_iniciais()
    def bem_vindo(self):
        texto_bem_vindo = customtkinter.CTkLabel(self,text="Bem Vindo!",font=("arial",30,"bold"),text_color="black")
        texto_bem_vindo.place(x=40,y=30)
        texto_resumo=customtkinter.CTkLabel(self,text="Aqui esta o resumo das informaçoes do Sistema",font=("",15),text_color="black")
        texto_resumo.place(x=30,y=80)
    def grafico(self):
        img_grafico=customtkinter.CTkImage(Image.open("recursos/grafico/imagem_grafico/grafico.png"),size=(700,250))
        label_grafico=customtkinter.CTkLabel(self,text="",image=img_grafico,fg_color="#89CFF0",bg_color="#89CFF0",)
        label_grafico.place(x=200,y=234)
    def funcoes_iniciais(self):
        self.card_usuario()
        self.card_clientes()
        self.card_dolar()
        self.card_devolucao()
        self.card_sistema()
        self.card_reclamacao()
        self.frames()
        self.botoes_acao()
        self.status_sistema()
        self.atividade_recente()
        self.report()
    def frames(self):

        self.frame_acao=customtkinter.CTkFrame(self,corner_radius=10)
        self.frame_acao.place(x=50,y=500)

        self.frame_atividade=customtkinter.CTkFrame(self)
        self.frame_atividade.place(x=300,y=500)

        self.frame_report=customtkinter.CTkFrame(self)
        self.frame_report.place(x=600,y=500)


        self.frame_status=customtkinter.CTkFrame(self)
        self.frame_status.place(x=900,y=500)
    def report(self):
        titulo=customtkinter.CTkLabel(self.frame_report,text="Report",font=("arial",17,"italic"))
        titulo.place(x=0,y=0)
        texto_report=customtkinter.CTkLabel(self.frame_report,text="aqui aconteceu nada mane")
        texto_report.place(x=0,y=40)
    def atividade_recente (self):
        titulo=customtkinter.CTkLabel(self.frame_atividade,text="Atividade Recente",font=("arial",17,"italic"))
        titulo.place(x=0,y=0)
        texto_atividade=customtkinter.CTkLabel(self.frame_atividade,text="aqui aconteceu nada mane")
        texto_atividade.place(x=0,y=40)
    def status_sistema(self):
        titulo=customtkinter.CTkLabel(self.frame_status,text="Status do Sistema",font=("arial",17,"italic"))
        titulo.place(x=0,y=0)
        status_sys=customtkinter.CTkLabel(self.frame_status,text="nada aconteceu nessa bixiga",font=("arial",15,"italic"))
        status_sys.place(x=0,y=50)
    def botoes_acao(self):
        titulo=customtkinter.CTkLabel(self.frame_acao,text="Açao Rapida",font=("arial",17,"italic"))
        titulo.place(x=0,y=0)
        add_usuario=customtkinter.CTkButton(self.frame_acao,text="• Adicionar Usuario",font=("arial",15,"italic"),fg_color="#242424")
        add_usuario.place(x=20,y=40)
        reportar=customtkinter.CTkButton(self.frame_acao,text="• Reportar     ",font=("arial",15,"italic"),fg_color="#242424")
        reportar.place(x=20,y=70)
        configurar=customtkinter.CTkButton(self.frame_acao,text="• Settings",fg_color="#242424",font=("arial",15,"italic"))
        configurar.place(x=0,y=100)
    def card_usuario(self):
        #posso pegar uma label fazia e simular uma extensao dessa primeira label pra ficar algo mais boniyo
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="#a3d8be",corner_radius=5,width=120,height=70,text_color="black")   
        texto_usuario.place(x=60,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Novos Usuarios",fg_color="#a3d8be",corner_radius=5,width=120,bg_color="#a3d8be",text_color="black")
        texto_new.place(x=60,y=180)
    def card_clientes(self):
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="#2eb07e",corner_radius=5,width=120,height=70,text_color="black")   
        texto_usuario.place(x=245,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Clientes ativos",fg_color="#2eb07e",width=120,bg_color="#84e5df",text_color="black")
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
        texto_usuario=customtkinter.CTkLabel(self,text="""$5.50""",anchor="n",text_color="black",font=("",27),fg_color="#5ebeb7",corner_radius=5,width=120,height=70)   
        texto_usuario.place(x=425,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Valor do Dolar",text_color="black",fg_color="#5ebeb7",width=120)
        texto_new.place(x=425,y=180)
    def card_reclamacao(self):
        texto_usuario=customtkinter.CTkLabel(self,text_color="black",text="""17""",anchor="n",font=("",27),fg_color="#FF6F61",corner_radius=10,width=120,height=70,bg_color="#89CFF0")   
        texto_usuario.place(x=980,y=150)
        texto_new=customtkinter.CTkLabel(self,text_color="black",text="Reclamaçoes",fg_color="#FF6F61",corner_radius=0,width=120,bg_color="#89CFF0")
        texto_new.place(x=980,y=180)




class Users(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.entrada()
        usu_text=customtkinter.CTkLabel(self,text="Usuarios",text_color="black",font=("arial",25,"bold"))
        usu_text.place(x=500,y=50)

        adi=customtkinter.CTkLabel(self,text="Adicionar Usuario",text_color="black",font=("arial",19,"italic"))
        adi.place(x=50,y=120)
        self.scroll()
        
    def entrada(self):
        entrada_nome=customtkinter.CTkEntry(self,font=("arial",15),width=230,text_color="white",placeholder_text="nome",placeholder_text_color="gray")
        entrada_nome.place(x=50,y=160)
        entrada_email=customtkinter.CTkEntry(self,font=("arial",15),width=230,text_color="white",placeholder_text="Email",placeholder_text_color="gray")
        entrada_email.place(x=286,y=160)

        combo=customtkinter.CTkOptionMenu(self,values=["Funçao","estagiario","funcionario","Rh"])
        combo.place(x=530,y=160)

        combo1=customtkinter.CTkOptionMenu(self,values=["Nivel de acesso","Usuario","Adminitrador"])
        combo1.place(x=680,y=160)

        add=customtkinter.CTkButton(self,text="Add",corner_radius=20,width=60)
        add.place(x=830,y=160)
    def scroll(self):
        self.campo=customtkinter.CTkScrollableFrame(self,width=1138,height=504)
        self.campo.place(x=0,y=200)
        entra=customtkinter.CTkEntry(self.campo)
        entra.grid(row=0,column=0)
        entra=customtkinter.CTkEntry(self.campo)
        entra.grid(row=0,column=1)
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