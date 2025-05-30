from PIL import Image
from recursos.login.login import Tela_login
import customtkinter
import webbrowser
from recursos.banco_de_dados.banco import Clientes,Funcionario
from recursos.banco_de_dados.criptografia.cripto import criptografar_dados,descriptografar_dados

class DashBoard(customtkinter.CTkFrame):
    """
    Frame principal do dashboard, exibe informações resumidas do sistema.
    """
    def __init__(self, master, **kwargs):
        """
        Inicializa o frame do dashboard e adiciona widgets principais.
        """
        super().__init__(master, **kwargs)
        self.bem_vindo()
        self.grafico()
        self.funcoes_iniciais()

    def bem_vindo(self):
        """
        Exibe mensagem de boas-vindas e resumo do sistema.
        """
        texto_bem_vindo = customtkinter.CTkLabel(self,text="Bem Vindo!",font=("arial",30,"bold"),text_color="black")
        texto_bem_vindo.place(x=40,y=30)
        texto_resumo=customtkinter.CTkLabel(self,text="Aqui esta o resumo das informaçoes do Sistema",font=("",15),text_color="black")
        texto_resumo.place(x=30,y=80)
    def grafico(self):
        """
        Exibe o gráfico principal no dashboard.
        """
        img_grafico=customtkinter.CTkImage(Image.open("recursos/grafico/imagem_grafico/grafico.png"),size=(700,250))
        label_grafico=customtkinter.CTkLabel(self,text="",image=img_grafico,fg_color="#89CFF0",bg_color="#89CFF0",)
        label_grafico.place(x=200,y=234)
    def funcoes_iniciais(self):
        """
        Inicializa os cards, frames e botões de ação do dashboard.
        """
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
        """
        Cria e posiciona os frames de ação, atividade, report e status.
        """

        self.frame_acao=customtkinter.CTkFrame(self,corner_radius=10)
        self.frame_acao.place(x=50,y=500)

        self.frame_atividade=customtkinter.CTkFrame(self)
        self.frame_atividade.place(x=300,y=500)

        self.frame_report=customtkinter.CTkFrame(self)
        self.frame_report.place(x=600,y=500)


        self.frame_status=customtkinter.CTkFrame(self)
        self.frame_status.place(x=900,y=500)
    def report(self):
        """
        Exibe informações de report no dashboard.
        """
        titulo=customtkinter.CTkLabel(self.frame_report,text="Report",font=("arial",17,"italic"))
        titulo.place(x=0,y=0)
        texto_report=customtkinter.CTkLabel(self.frame_report,text="problemas no Support")
        texto_report.place(x=0,y=40)
    def atividade_recente (self):
        """
        Exibe informações sobre a atividade recente do sistema.
        """
        titulo=customtkinter.CTkLabel(self.frame_atividade,text="Atividade Recente",font=("arial",17,"italic"))
        titulo.place(x=0,y=0)
        texto_atividade=customtkinter.CTkLabel(self.frame_atividade,text="adicionou 1 novo cliente")
        texto_atividade.place(x=0,y=40)
    def status_sistema(self):
        """
        Exibe o status atual do sistema.
        """
        titulo=customtkinter.CTkLabel(self.frame_status,text="Status do Sistema",font=("arial",17,"italic"))
        titulo.place(x=0,y=0)
        status_sys=customtkinter.CTkLabel(self.frame_status,text="Sistema esta ok")
        status_sys.place(x=0,y=40)
    def botoes_acao(self):
        """
        Cria botões de ações rápidas no dashboard.
        """
        titulo=customtkinter.CTkLabel(self.frame_acao,text="Açao Rapida",font=("arial",17,"italic"),corner_radius=50)
        titulo.place(x=10,y=0)
        add_usuario=customtkinter.CTkButton(self.frame_acao,text="• Adicionar Usuario",font=("arial",15,"italic"),fg_color="#242424",command=lambda:self.mudar_frame())
        add_usuario.place(x=0,y=40)
        reportar=customtkinter.CTkButton(self.frame_acao,text="• reportar                 ",font=("arial",15,"italic"),fg_color="#242424")
        reportar.place(x=0,y=70)
        configurar=customtkinter.CTkButton(self.frame_acao,text="• Settings                 ",fg_color="#242424",font=("arial",15,"italic"))
        configurar.place(x=0,y=100)
    
        
    def card_usuario(self):
        """
        Exibe o card de novos usuários.
        """
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="#a3d8be",corner_radius=5,width=120,height=70,text_color="black")
        texto_usuario.place(x=60,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Novos Usuarios",fg_color="#a3d8be",corner_radius=5,width=120,bg_color="#a3d8be",text_color="black")
        texto_new.place(x=60,y=180)
    def card_clientes(self):
        """
        Exibe o card de clientes ativos.
        """
        texto_usuario=customtkinter.CTkLabel(self,text="""1""",anchor="n",font=("",27),fg_color="#2eb07e",corner_radius=5,width=120,height=70,text_color="black")
        texto_usuario.place(x=245,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Clientes ativos",fg_color="#2eb07e",width=120,bg_color="#84e5df",text_color="black")
        texto_new.place(x=245,y=180)
    def card_sistema(self):
        """
        Exibe o card de carga do sistema.
        """
        texto_usuario=customtkinter.CTkLabel(self,text="""69%""",anchor="n",font=("",27),text_color="black",fg_color="#FB8C00",corner_radius=5,width=120,height=70)
        texto_usuario.place(x=785,y=150)
        texto_new=customtkinter.CTkLabel(self,text="System Load",fg_color="#FB8C00",width=120,bg_color="gray",text_color="black")
        texto_new.place(x=785,y=180)
    def card_devolucao(self):
        """
        Exibe o card de devolução.
        """
        texto_usuario=customtkinter.CTkLabel(self,text="""10%""",anchor="n",font=("",27),fg_color="#EEDC82",corner_radius=5,width=120,height=70,text_color="black")
        texto_usuario.place(x=605,y=150)
        texto_new=customtkinter.CTkLabel(self,text="devoluçao",fg_color="#EEDC82",width=120,bg_color="#EEDC82",text_color="black")
        texto_new.place(x=605,y=180)
    def card_dolar(self):
        """
        Exibe o card do valor do dólar.
        """
        texto_usuario=customtkinter.CTkLabel(self,text="""$5.50""",anchor="n",text_color="black",font=("",27),fg_color="#5ebeb7",corner_radius=5,width=120,height=70)
        texto_usuario.place(x=425,y=150)
        texto_new=customtkinter.CTkLabel(self,text="Valor do Dolar",text_color="black",fg_color="#5ebeb7",width=120)
        texto_new.place(x=425,y=180)
    def card_reclamacao(self):
        """
        Exibe o card de reclamações.
        """
        texto_usuario=customtkinter.CTkLabel(self,text_color="black",text="""17""",anchor="n",font=("",27),fg_color="#FF6F61",corner_radius=10,width=120,height=70,bg_color="#89CFF0")
        texto_usuario.place(x=980,y=150)
        texto_new=customtkinter.CTkLabel(self,text_color="black",text="Reclamaçoes",fg_color="#FF6F61",corner_radius=0,width=120,bg_color="#89CFF0")
        texto_new.place(x=980,y=180)

        
class Users(customtkinter.CTkFrame):
    """
    Frame para gerenciamento de usuários do sistema.
    """
    def __init__(self, master, **kwargs):
        """
        Inicializa o frame de usuários e seus componentes.
        """
        super().__init__(master, **kwargs)
        self.frame_scroll()
        self.funcoes_entrada()
        self.texto_coluna()
        self.linha = 0
        self.continuar = True
        self.texto()
        self.criar_users()

    def criar_users(self):
        """
        Cria e exibe os usuários cadastrados na tabela.
        """
        funcionario=Funcionario()
        try:
            lista_funcionario=funcionario.lista_funcionario(self.linha,"admin")
            if lista_funcionario==False:
                self.continuar=False
                return False
        except:
            self.continuar=False
            
        #n1=descriptografar_dados(self.lista[1].dados_clientes[self.linha],"admin")
        self.adicionar_usuario_na_tabela(self.linha+1,lista_funcionario[0],lista_funcionario[1],self.linha+1,lista_funcionario[2],lista_funcionario[3])
        
        if self.continuar==True:
            self.linha+=1
            self.after(100,self.criar_users)
    def funcoes_entrada(self):
        """
        Cria os campos de entrada para adicionar novos usuários.
        """
        self.var_nome=self.criar_var("Nome")
        self.criar_entrada(var=self.var_nome,x=55,y=160)
        self.var_email=self.criar_var("Email")
        self.criar_entrada(var=self.var_email,x=285,y=160,wi=270)
        self.var_cargo=self.criar_var("Cargo")
        self.criar_entrada(var=self.var_cargo,x=555,y=160,verificar=1)
        self.var_nivel=self.criar_var("Nivel acesso")
        self.criar_entrada(var=self.var_nivel,x=693,y=160,verificar=1,text=["nivel de acesso","usuario","administrador"])
        add=customtkinter.CTkButton(self,text="Add",corner_radius=20,width=60,command=self.adicionar_usu)
        add.place(x=850,y=160)
        
        #55,285,555,693,850
    def criar_var(self,string):
        """
        Cria uma variável do tipo StringVar para campos de entrada.

        Args:
            string (str): Valor inicial da variável.

        Returns:
            customtkinter.StringVar: Variável criada.
        """
        variavel=customtkinter.StringVar(value=string)
        return variavel
    def criar_entrada(self,var,x,y,verificar=0,text=["Cargo","estagiario","funcionario","Rh"],wi=230):
        """
        Cria um campo de entrada ou menu de opções para os formulários.

        Args:
            var (StringVar): Variável associada ao campo.
            x (int): Posição x.
            y (int): Posição y.
            verificar (int): Se 1, cria um menu de opções; se 0, cria um campo de texto.
            text (list): Lista de opções para o menu.
            wi (int): Largura do campo.
        """
        if verificar==0:
            entrada=customtkinter.CTkEntry(self,textvariable=var,corner_radius=0,font=("arial",15),width=wi,text_color="gray")
            entrada.place(x=x,y=y)
        else:
            cargo=customtkinter.CTkOptionMenu(self,variable=var,values=text,corner_radius=0)
            cargo.place(x=x,y=y)

    def texto(self):
        """
        Exibe os textos e avisos na tela de usuários.
        """
        client_text=customtkinter.CTkLabel(self,text="Usuarios",text_color="black",font=("arial",25,"bold"))
        client_text.place(x=500,y=50)
        aviso=customtkinter.CTkLabel(self,text_color="black",text="as modificaçoes sera aplicada somente na proxima sessao")
        aviso.place(x=0,y=0)
        texto_adicionar=customtkinter.CTkLabel(self,text="Adicionar Usuarios",text_color="black",font=("arial",19,"italic"))
        texto_adicionar.place(x=50,y=120)
    def adicionar_usu(self):#tenho que criar um botao pra refazer a lista
        """
        Adiciona um novo usuário ao banco de dados.
        """
        adi=Funcionario()
        var_lista=[self.var_nome.get(),self.var_email.get(),self.var_cargo.get(),self.var_nivel.get()]
        
        adi.novo_funcionario(var_lista,"admin")
    def texto_coluna(self):
        """
        Cria os títulos das colunas da tabela de usuários.
        """
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
    
    def frame_scroll(self):
        """
        Cria o frame rolável para exibição dos usuários.
        """
        self.campo=customtkinter.CTkScrollableFrame(self,width=1138,height=504)
        self.campo.place(x=0,y=200)
    
        
        numero=customtkinter.CTkLabel(self.campo,width=140,text="Nivel de acesso",corner_radius=0,bg_color="#565b5e")
        numero.grid(row=0,column=4)
        numero=customtkinter.CTkLabel(self.campo,width=140,text="Cargo",corner_radius=0,bg_color="#565b5e")

        numero.grid(row=0,column=3)
    def adicionar_usuario_na_tabela(self,idd,nome,email,linha,cargo,estado):
        """
        Adiciona um usuário na tabela visual.

        Args:
            idd (int): ID do usuário.
            nome (str): Nome do usuário.
            email (str): Email do usuário.
            linha (int): Linha da tabela.
            cargo (str): Cargo do usuário.
            estado (str): Estado do usuário.
        """
        id_var=customtkinter.StringVar(value=idd)
        id=customtkinter.CTkEntry(self.campo,width=50,textvariable=id_var,corner_radius=0)
        id.grid(row=linha,column=0)
        n1=customtkinter.StringVar(value=nome)
        entra=customtkinter.CTkEntry(self.campo,font=("arial",14),width=230,placeholder_text="nome",textvariable=n1,corner_radius=0)
        entra.grid(row=linha,column=1)
        n2=customtkinter.StringVar(value=email)
        entra2=customtkinter.CTkEntry(self.campo,font=("arial",14),width=270,textvariable=n2,corner_radius=0)
        entra2.grid(row=linha,column=2)

        combo_var=customtkinter.StringVar(value=cargo)
        combo=customtkinter.CTkOptionMenu(self.campo,variable=combo_var,values=["cargo","estagiario","funcionario","rh","outro"],corner_radius=0,fg_color="#242424")
        combo.grid(row=linha,column=3)

        combo_var2=customtkinter.StringVar(value=estado)
        combo1=customtkinter.CTkOptionMenu(self.campo,variable=combo_var2,values=["inativo","ativo"],corner_radius=0,fg_color="#242424")
        combo1.grid(row=linha,column=4)

        
        img_excluir=customtkinter.CTkImage(Image.open("excluir.png"),size=(20,20))
        botao_excluir=customtkinter.CTkButton(self.campo,text="",image=img_excluir,width=0,height=0,fg_color="#242424",command=lambda:self.delete(self.linha,linha,id,entra,entra2,combo,combo1,botao_excluir))
        botao_excluir.grid(row=linha,column=5)
    def delete(self,id_delete,row,id,ctkentry1,ctkentry2,ctkmenu1,ctkmenu2,botao_excluir):
        """
        Remove um usuário do banco de dados e da tabela visual.

        Args:
            id_delete (int): ID do usuário a ser removido.
            row (int): Linha da tabela.
            id, ctkentry1, ctkentry2, ctkmenu1, ctkmenu2, botao_excluir: Widgets a serem destruídos.
        """
        client=Funcionario()
        client.delete(id_delete)
        self.remover_botao(id,ctkentry1,ctkentry2,ctkmenu1,ctkmenu2,botao_excluir)
    def remover_botao(self,id,entry1,entry2,menu1,menu2,botao_excluir):
        """
        Remove widgets da tabela visual de usuários.

        Args:
            id, entry1, entry2, menu1, menu2, botao_excluir: Widgets a serem destruídos.
        """
        id.destroy()
        entry1.destroy()
        entry2.destroy()
        menu1.destroy()
        menu2.destroy()
        botao_excluir.destroy()
class Client(customtkinter.CTkFrame):
    """
    Frame para gerenciamento de clientes do sistema.
    """
    def __init__(self, master, **kwargs):
        """
        Inicializa o frame de clientes e seus componentes.
        """
        super().__init__(master, **kwargs)
        self.scroll()
        self.texto_coluna()
        self.texto()
        self.linha = 0
        self.continuar = True
        self.funçoes_entrada()
        self.criar_cliente()
        
    def adicionar_clientes(self):#tenho que criar um botao pra refazer a lista
        """
        Adiciona um novo cliente ao banco de dados.
        """
        client=Clientes()
        var_lista=[self.var_nome.get(),self.var_email.get(),self.var_cargo.get(),self.var_ativo.get()]
        client.novos_clientes(var_lista,"admin")
    def criar_cliente(self):
        """
        Cria e exibe os clientes cadastrados na tabela.
        """
        client=Clientes()
        try:
            lista_client=client.lista_clientes(self.linha,"admin")
            if lista_client==False:
                self.continuar=False
                return False
        except:
            self.continuar=False
            
        #descriptografar_dados(self.lista[1].dados_clientes[self.linha],senha)
        self.cliente(self.linha+1,lista_client[0],lista_client[1],self.linha+1,lista_client[2],lista_client[3])
        
        if self.continuar==True:
            self.linha+=1
            self.after(100,self.criar_cliente)
    
        
        #falta tirar a criptografia
    def texto(self):
        """
        Exibe os textos e avisos na tela de clientes.
        """
        client_text=customtkinter.CTkLabel(self,text="Clientes",text_color="black",font=("arial",25,"bold"))
        client_text.place(x=500,y=50)
        aviso=customtkinter.CTkLabel(self,text_color="black",text="as modificaçoes sera aplicada somente na proxima sessao")
        aviso.place(x=0,y=0)
        texto_adicionar=customtkinter.CTkLabel(self,text="Adicionar Clientes",text_color="black",font=("arial",19,"italic"))
        texto_adicionar.place(x=50,y=120)
    def texto_coluna(self):
        """
        Cria os títulos das colunas da tabela de clientes.
        """
        texto_id=customtkinter.CTkLabel(self.campo,width=50,text="id",corner_radius=0,bg_color="#565b5e")
        texto_id.grid(row=0,column=0)
        texto_nome=customtkinter.CTkLabel(self.campo,width=230,text="Nome",corner_radius=0,bg_color="#565b5e")
        texto_nome.grid(row=0,column=1)
        texto_email=customtkinter.CTkLabel(self.campo,width=270,text="Email",corner_radius=0,bg_color="#565b5e")
        texto_email.grid(row=0,column=2)
    def funçoes_entrada(self):
        """
        Cria os campos de entrada para adicionar novos clientes.
        """
        self.var_nome=self.criar_var("Nome")
        self.criar_entrada(var=self.var_nome,x=55,y=160)
        self.var_email=self.criar_var("Email")
        self.criar_entrada(var=self.var_email,x=285,y=160,widt=270)
        self.var_cargo=self.criar_var("Cargo")
        self.criar_entrada(var=self.var_cargo,x=555,y=160,verificar=1)
        self.var_ativo=self.criar_var("ativo")
        self.criar_entrada(var=self.var_ativo,x=693,y=160,verificar=1,text=["ativo","inativo"])
        add=customtkinter.CTkButton(self,text="Add",corner_radius=20,width=60,command=self.adicionar_clientes)
        add.place(x=850,y=160)
        
    def criar_var(self,string):
        """
        Cria uma variável do tipo StringVar para campos de entrada.

        Args:
            string (str): Valor inicial da variável.

        Returns:
            customtkinter.StringVar: Variável criada.
        """
        variavel=customtkinter.StringVar(value=string)
        return variavel
    def criar_entrada(self,var,x,y,verificar=0,text=["Cargo","estagiario","funcionario","Rh"],widt=230):
        """
        Cria um campo de entrada ou menu de opções para os formulários.

        Args:
            var (StringVar): Variável associada ao campo.
            x (int): Posição x.
            y (int): Posição y.
            verificar (int): Se 1, cria um menu de opções; se 0, cria um campo de texto.
            text (list): Lista de opções para o menu.
            widt (int): Largura do campo.
        """
        if verificar==0:
            entrada=customtkinter.CTkEntry(self,width=widt,textvariable=var,corner_radius=0,font=("arial",15),text_color="gray")
            entrada.place(x=x,y=y)
        else:
            cargo=customtkinter.CTkOptionMenu(self,variable=var,values=text,corner_radius=0)
            cargo.place(x=x,y=y)
        

    def scroll(self):
        """
        Cria o frame rolável para exibição dos clientes.
        """
        self.label = customtkinter.CTkLabel(self,text="client")
        self.campo=customtkinter.CTkScrollableFrame(self,width=1138,height=504)
        self.campo.place(x=0,y=200)

        numero=customtkinter.CTkLabel(self.campo,width=140,text="Nivel de acesso",corner_radius=0,bg_color="#565b5e")
        numero.grid(row=0,column=4)
        numero=customtkinter.CTkLabel(self.campo,width=140,text="Cargo",corner_radius=0,bg_color="#565b5e")

        numero.grid(row=0,column=3)
    def cliente(self,idd,nome,email,linha,cargo,estado):
        """
        Adiciona um cliente na tabela visual.

        Args:
            idd (int): ID do cliente.
            nome (str): Nome do cliente.
            email (str): Email do cliente.
            linha (int): Linha da tabela.
            cargo (str): Cargo do cliente.
            estado (str): Estado do cliente.
        """
        id_var=customtkinter.StringVar(value=idd)
        id=customtkinter.CTkEntry(self.campo,width=50,textvariable=id_var,corner_radius=0)
        id.grid(row=linha,column=0)
        
        var_nome=customtkinter.StringVar(value=nome)
        entra=customtkinter.CTkEntry(self.campo,font=("arial",14),width=230,placeholder_text="nome",textvariable=var_nome,corner_radius=0)
        entra.grid(row=linha,column=1)
        n2=customtkinter.StringVar(value=email)
        entra2=customtkinter.CTkEntry(self.campo,font=("arial",14),width=270,textvariable=n2,corner_radius=0)
        entra2.grid(row=linha,column=2)

        combo_var=customtkinter.StringVar(value=cargo)
        combo=customtkinter.CTkOptionMenu(self.campo,variable=combo_var,values=["cargo","estagiario","funcionario","rh","outro"],corner_radius=0,fg_color="#242424")
        combo.grid(row=linha,column=3)

        combo_var2=customtkinter.StringVar(value=estado)
        combo1=customtkinter.CTkOptionMenu(self.campo,variable=combo_var2,values=["inativo","ativo"],corner_radius=0,fg_color="#242424")
        combo1.grid(row=linha,column=4)
        
        img_excluir=customtkinter.CTkImage(Image.open("excluir.png"),size=(20,20))
        botao_excluir=customtkinter.CTkButton(self.campo,text="",image=img_excluir,width=0,height=0,fg_color="#242424",command=lambda:self.delete(self.linha,linha,id,entra,entra2,combo,combo1,botao_excluir))
        botao_excluir.grid(row=linha,column=5)
    def delete(self,id_delete,row,id,ctkentry1,ctkentry2,ctkmenu1,ctkmenu2,botao_excluir):
        """
        Remove um cliente do banco de dados e da tabela visual.

        Args:
            id_delete (int): ID do cliente a ser removido.
            row (int): Linha da tabela.
            id, ctkentry1, ctkentry2, ctkmenu1, ctkmenu2, botao_excluir: Widgets a serem destruídos.
        """
        client=Clientes()
        client.delete(id_delete)
        self.remover_botao(id,ctkentry1,ctkentry2,ctkmenu1,ctkmenu2,botao_excluir)
    def remover_botao(self,id,entry1,entry2,menu1,menu2,botao_excluir):
        """
        Remove widgets da tabela visual de clientes.

        Args:
            id, entry1, entry2, menu1, menu2, botao_excluir: Widgets a serem destruídos.
        """
        id.destroy()
        entry1.destroy()
        entry2.destroy()
        menu1.destroy()
        menu2.destroy()
        botao_excluir.destroy()
class Settings(customtkinter.CTkFrame):
    """
    Frame para configurações do sistema.
    """
    def __init__(self, master, **kwargs):
        """
        Inicializa o frame de configurações e seus componentes.
        """
        super().__init__(master, **kwargs)
        self.primeira_fileira()
        self.text()
        self.segunda_fileira()
        self.botaos()

    def primeira_fileira(self):
        """
        Cria e posiciona os frames da primeira fileira de configurações.
        """
        self.frame1=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame1.place(x=50,y=500)

        self.frame2=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame2.place(x=350,y=500)

        self.frame3=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame3.place(x=750,y=500)

        self.frame4=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame4.place(x=1000,y=500)
    def segunda_fileira(self):
        """
        Cria e posiciona os frames da segunda fileira de configurações.
        """
        self.frame5=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame5.place(x=50,y=200)

        self.frame6=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame6.place(x=350,y=200)

        self.frame7=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame7.place(x=750,y=200)

        self.frame8=customtkinter.CTkFrame(self,width=150,height=150)
        self.frame8.place(x=1000,y=200)
    def botaos(self):
        """
        Cria e posiciona os botões de configuração em cada frame.
        """
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
        """
        Cria um botão do tipo Switch ou CheckBox em um frame de configuração.

        Args:
            frame: Frame onde o botão será adicionado.
            text (str): Texto do botão.
            y (int): Posição y do botão.
            verificar (int): Se 1, cria um Switch; se 0, cria um CheckBox.
        """
        if verificar==1:
            botao_frame3=customtkinter.CTkSwitch(frame,text=text)
            botao_frame3.place(x=0,y=y)
        else:
            botao_frame1=customtkinter.CTkCheckBox(frame,corner_radius=20,text=text,font=("",18))
            botao_frame1.place(x=0,y=y)
        
    def text(self):
        """
        Exibe textos de boas-vindas e informações de configuração.
        """
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
        """
        Abre o link do GitHub do autor no navegador padrão.
        """
        url="https://github.com/Daniel-X2"
        webbrowser.open(url)
