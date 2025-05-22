from PIL import Image

import customtkinter
import webbrowser
from recursos.banco_de_dados.banco import Clientes
from recursos.banco_de_dados.criptografia.cripto import criptografar_dados,descriptografar_dados

class DashBoard(customtkinter.CTkFrame):#aqui tem algo
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

class Users(customtkinter.CTkFrame):#aqui tem algo
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.entrada()
        usu_text=customtkinter.CTkLabel(self,text="Usuarios",text_color="black",font=("arial",25,"bold"))
        usu_text.place(x=500,y=50)

        adi=customtkinter.CTkLabel(self,text="Adicionar Usuario",text_color="black",font=("arial",19,"italic"))
        adi.place(x=50,y=120)

        self.scroll()


        n1=customtkinter.CTkImage(Image.open("excluir.png"),size=(20,20))
        n2=customtkinter.CTkButton(self.campo,text="",image=n1,width=0,height=0,fg_color="#242424")
        n2.grid(row=1,column=5)

    def texto_coluna(self):
        texto_id=customtkinter.CTkLabel(self.campo,width=50,text="id",corner_radius=0,bg_color="#565b5e")
        texto_id.grid(row=0,column=0)
        texto_nome=customtkinter.CTkLabel(self.campo,width=230,text="Nome",corner_radius=0,bg_color="#565b5e")
        texto_nome.grid(row=0,column=1)
        texto_email=customtkinter.CTkLabel(self.campo,width=270,text="Email",corner_radius=0,bg_color="#565b5e")
        texto_email.grid(row=0,column=2)
        numero=customtkinter.CTkLabel(self.campo,width=140,text="Nivel de acesso",corner_radius=0,bg_color="#565b5e")
        numero.grid(row=0,column=4)
        numero=customtkinter.CTkLabel(self.campo,width=140,text="Cargo",corner_radius=0,bg_color="#565b5e")

        numero.grid(row=0,column=3)
    def entrada(self):
        entrada_nome=customtkinter.CTkEntry(self,corner_radius=0,font=("arial",15),width=230,text_color="white",placeholder_text="nome",placeholder_text_color="gray")
        entrada_nome.place(x=55,y=160)
        entrada_email=customtkinter.CTkEntry(self,corner_radius=0,font=("arial",15),width=270,text_color="white",placeholder_text="Email",placeholder_text_color="gray")
        entrada_email.place(x=285,y=160)

        combo=customtkinter.CTkOptionMenu(self,values=["Cargo","estagiario","funcionario","Rh"],corner_radius=0)
        combo.place(x=555,y=160)

        combo1=customtkinter.CTkOptionMenu(self,values=["Nivel de acesso","Usuario","Adminitrador"],corner_radius=0)
        combo1.place(x=693,y=160)

        add=customtkinter.CTkButton(self,text="Add",corner_radius=20,width=60)
        add.place(x=850,y=160)
    def scroll(self):
        self.campo=customtkinter.CTkScrollableFrame(self,width=1138,height=504)
        self.campo.place(x=0,y=200)
        num=customtkinter.StringVar(value="1")
        numero=customtkinter.CTkEntry(self.campo,width=50,textvariable=num,corner_radius=0)
        numero.grid(row=1,column=0)
        self.texto_coluna()

        n1=customtkinter.StringVar(value="anthony ferreira de lima")
        entra=customtkinter.CTkEntry(self.campo,font=("arial",14),width=230,placeholder_text="nome",textvariable=n1,corner_radius=0)
        entra.grid(row=1,column=1)
        n2=customtkinter.StringVar(value="athony.g2455@gmail.com")
        entra=customtkinter.CTkEntry(self.campo,font=("arial",14),width=270,textvariable=n2,corner_radius=0)
        entra.grid(row=1,column=2)



        combo=customtkinter.CTkOptionMenu(self.campo,values=["Cargo","estagiario","funcionario","Rh"],corner_radius=0,fg_color="#242424")
        combo.grid(row=1,column=3)



        combo1=customtkinter.CTkOptionMenu(self.campo,values=["Nivel de acesso","Usuario","Adminitrador"],corner_radius=0,fg_color="#242424")
        combo1.grid(row=1,column=4)

class Client(customtkinter.CTkFrame):#aqui tem algo
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.scroll()
        self.entrada()
        self.texto_coluna()
        self.entrada()
        self.linha=0
        self.continuar=True
        self.criar_cliente()
        

    def criar_cliente(self):
        n1=Clientes()
        try:
            n2=n1.lista_clientes(self.linha)
            if n2==False:
                self.continuar=False
                return False
        except:
            self.continuar=False
            
        #descriptografar_dados(self.lista[1].dados_clientes[self.linha],senha)
        self.cliente(self.linha+1,n2,"qual",self.linha+1,"ss","ss")
        
        if self.continuar==True:
            self.linha+=1
            self.after(100,self.criar_cliente)
    
        
        #falta tirar a criptografia
    def texto(self):
        client_text=customtkinter.CTkLabel(self,text="Clientes",text_color="black",font=("arial",25,"bold"))
        client_text.place(x=500,y=50)

        texto_adicionar=customtkinter.CTkLabel(self,text="Adicionar Clientes",text_color="black",font=("arial",19,"italic"))
        texto_adicionar.place(x=50,y=120)
    def texto_coluna(self):
        texto_id=customtkinter.CTkLabel(self.campo,width=50,text="id",corner_radius=0,bg_color="#565b5e")
        texto_id.grid(row=0,column=0)
        texto_nome=customtkinter.CTkLabel(self.campo,width=230,text="Nome",corner_radius=0,bg_color="#565b5e")
        texto_nome.grid(row=0,column=1)
        texto_email=customtkinter.CTkLabel(self.campo,width=270,text="Email",corner_radius=0,bg_color="#565b5e")
        texto_email.grid(row=0,column=2)
    def entrada(self):
        entrada_nome=customtkinter.CTkEntry(self,corner_radius=0,font=("arial",15),width=230,text_color="white",placeholder_text="nome",placeholder_text_color="gray")
        entrada_nome.place(x=55,y=160)
        entrada_email=customtkinter.CTkEntry(self,corner_radius=0,font=("arial",15),width=270,text_color="white",placeholder_text="Email",placeholder_text_color="gray")
        entrada_email.place(x=285,y=160)

        combo=customtkinter.CTkOptionMenu(self,values=["Cargo","estagiario","funcionario","Rh"],corner_radius=0)
        combo.place(x=555,y=160)

        combo1=customtkinter.CTkOptionMenu(self,values=["ativo","inativo"],corner_radius=0)
        combo1.place(x=693,y=160)

        add=customtkinter.CTkButton(self,text="Add",corner_radius=20,width=60)
        add.place(x=850,y=160)

    def scroll(self):
        self.label = customtkinter.CTkLabel(self,text="client")
        self.campo=customtkinter.CTkScrollableFrame(self,width=1138,height=504)
        self.campo.place(x=0,y=200)

        numero=customtkinter.CTkLabel(self.campo,width=140,text="Nivel de acesso",corner_radius=0,bg_color="#565b5e")
        numero.grid(row=0,column=4)
        numero=customtkinter.CTkLabel(self.campo,width=140,text="Cargo",corner_radius=0,bg_color="#565b5e")

        numero.grid(row=0,column=3)
    def cliente(self,idd,nome,email,linha,cargo,estado):
        id_var=customtkinter.StringVar(value=idd)
        id=customtkinter.CTkEntry(self.campo,width=50,textvariable=id_var,corner_radius=0)
        id.grid(row=linha,column=0)
        n1=customtkinter.StringVar(value=nome)
        entra=customtkinter.CTkEntry(self.campo,font=("arial",14),width=230,placeholder_text="nome",textvariable=n1,corner_radius=0)
        entra.grid(row=linha,column=1)
        n2=customtkinter.StringVar(value=email)
        entra=customtkinter.CTkEntry(self.campo,font=("arial",14),width=270,textvariable=n2,corner_radius=0)
        entra.grid(row=linha,column=2)

        combo_var=customtkinter.StringVar(value=cargo)
        combo=customtkinter.CTkOptionMenu(self.campo,variable=combo_var,values=["cargo","estagiario","funcionario","rh","outro"],corner_radius=0,fg_color="#242424")
        combo.grid(row=linha,column=3)

        combo_var2=customtkinter.StringVar(value=estado)
        combo1=customtkinter.CTkOptionMenu(self.campo,variable=combo_var2,values=["inativo","ativo"],corner_radius=0,fg_color="#242424")
        combo1.grid(row=linha,column=4)

        n1=customtkinter.CTkImage(Image.open("excluir.png"),size=(20,20))
        n2=customtkinter.CTkButton(self.campo,text="",image=n1,width=0,height=0,fg_color="#242424")
        n2.grid(row=linha,column=5)

class Settings(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.primeira_fileira()
        
        self.text()
        self.segunda_fileira()
        self.botaos()
    def primeira_fileira(self):
        self.frame1=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame1.place(x=50,y=500)

        self.frame2=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame2.place(x=350,y=500)

        self.frame3=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame3.place(x=750,y=500)

        self.frame4=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame4.place(x=1000,y=500)
    def segunda_fileira(self):
        self.frame5=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame5.place(x=50,y=200)

        self.frame6=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame6.place(x=350,y=200)

        self.frame7=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame7.place(x=750,y=200)

        self.frame8=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame8.place(x=1000,y=200)
    def botaos(self):
        #botoes do primeiro frame
        self.criar_botao(self.frame1,"teste",0,0)
        self.criar_botao(self.frame1,"teste",36,0)
        self.criar_botao(self.frame1,"teste",80,0)
        #botoes do segundo frame
        self.criar_botao(self.frame2,"teste",0,1)
        self.criar_botao(self.frame2,"teste",36,1)
        self.criar_botao(self.frame2,"teste",80,1)
        #botoes do terceiro frame
        self.criar_botao(self.frame3,"teste",0,1)
        self.criar_botao(self.frame3,"teste",36,1)
        self.criar_botao(self.frame3,"teste",80,1)
        #botoes do quarto frame
        self.criar_botao(self.frame4,"teste",0,1)
        self.criar_botao(self.frame4,"teste",36,1)
        self.criar_botao(self.frame4,"teste",80,1)
        #botoes do quinto frame
        self.criar_botao(self.frame5,"teste",0,1)
        self.criar_botao(self.frame5,"teste",36,1)
        self.criar_botao(self.frame5,"teste",80,1)
        #botoes do sexto frame
        self.criar_botao(self.frame6,"teste",0,1)
        self.criar_botao(self.frame6,"teste",36,0)
        self.criar_botao(self.frame6,"teste",80,1)
        #botoes do 7 frame
        self.criar_botao(self.frame7,"teste",0,1)
        self.criar_botao(self.frame7,"teste",36,1)
        self.criar_botao(self.frame7,"teste",80,0)
        #botoes do 8 frame
        self.criar_botao(self.frame8,"teste",0,1)
        self.criar_botao(self.frame8,"teste",36,1)
        self.criar_botao(self.frame8,"teste",80,1)
    def criar_botao(self,frame,text,y,verificar):
        if verificar==1:
            botao_frame3=customtkinter.CTkSwitch(frame,text=text)
            botao_frame3.place(x=0,y=y)
        else:
            botao_frame1=customtkinter.CTkCheckBox(frame,corner_radius=20,text=text,font=("",18))
            botao_frame1.place(x=0,y=y)
        
    def text(self):
        texto=customtkinter.CTkLabel(self,text="Seja Bem vindo ",text_color="black",font=("",25))
        texto.place(x=0,y=0)

        config=customtkinter.CTkLabel(self,text="as configuraçoes",text_color="black",font=("",18))
        config.place(x=20,y=30)
class Support(customtkinter.CTkFrame):#aqui tem algo
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets onto the frame, for example:
        img_git=customtkinter.CTkImage(Image.open("recursos/imagens_main/git.png"),size=(120,120))
        label_git=customtkinter.CTkLabel(self,image=img_git,text="")
        label_git.place(x=500,y=200)
        git_menor=customtkinter.CTkImage(Image.open("recursos/imagens_main/git.png"),size=(120,120))
        agradecimentos="""   Bem vindo ao meu projeto
        fico muito feliz que esteja olhando esse projeto
        se estiver interessado nesse projeto ou em outros basta
        acessar meu github"""
        label_agra=customtkinter.CTkLabel(self,text=agradecimentos,font=("ariel",18),text_color="black")
        label_agra.place(x=300,y=350)

        imagem=customtkinter.CTkImage(Image.open("recursos/imagens_main/git.png"),size=(50,50))
        botao=customtkinter.CTkButton(self,text="clique em mim",image=imagem,width=0,height=0,command=self.abrir_github)
        botao.place(x=0,y=660)
    def abrir_github(self):
        url="https://github.com/Daniel-X2"
        webbrowser.open(url)
