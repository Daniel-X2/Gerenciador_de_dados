import os

import customtkinter
from PIL import Image

from recursos.banco_de_dados.banco import Clientes, Funcionario
from recursos.banco_de_dados.criptografia.cripto import (criptografar_dados,
                                                        descriptografar_dados)
from recursos.frame.main_frame import DashBoard,Client,Settings,Support,Users
from recursos.login.login import Tela_login

# exportar o resto aqui


class App(customtkinter.CTk):
    """
    Classe principal da aplicação. Responsável por inicializar e gerenciar a interface gráfica principal,
    alternar entre os frames, criar botões laterais, configurar a janela e exibir elementos visuais.
    """

    def __init__(self):
        """
        Inicializa a aplicação principal, configura a cor de fundo e chama as funções de inicialização.
        """
        super().__init__(fg_color="#82b3f0")
        self.inicializar_funcoes()

    def inicializar_funcoes(self):
        """
        Inicializa os componentes principais da interface:
        configura a janela, exibe o falcão, cria labels, inicializa os frames,
        cria os botões laterais e exibe o frame inicial.
        """
        self.configurar_janela()
        self.exibir_falcao()
        self.criar_labels()
        self.frame_atual = ""
        self.inicializar_frames()
        self.criar_botoes_laterais()
        self.alternar_frame(self.frame_Dash)

    def inicializar_frames(self):
        """
        Inicializa os frames principais da aplicação (Dashboard, Users, Client, Settings, Support).
        Define tamanho e cor de fundo de cada frame.
        """
        self.frame_Dash = DashBoard(
            master=self, width=1200, height=900, fg_color="#82b3f0"
        )
        self.frame_Users = Users(
            master=self, width=1200, height=900, fg_color="#84e5df"
        )
        self.frame_Client = Client(
            master=self, width=1200, height=900, fg_color="#89CFF0"
        )
        self.frame_Settings = Settings(
            master=self, width=1200, height=900, fg_color="#89CFF0"
        )
        self.frame_Support = Support(
            master=self, width=1200, height=900, fg_color="#89CFF0"
        )

    def alternar_frame(self, frame):
        """
        Alterna entre os frames principais, ocultando o anterior e exibindo o novo.

        Args:
            frame: Frame a ser exibido.
        """
        if frame.place_info():
            pass
        elif self.frame_atual != frame and self.frame_atual != "":
            if self.frame_atual == frame:
                pass
            else:
                frame.place(x=205, y=0)
                self.frame_atual.place_forget()
                self.frame_atual = frame
        else:
            if self.frame_atual == frame:
                pass
            else:
                frame.place(x=205, y=0)
                self.frame_atual = frame

    def criar_botoes_laterais(self):
        """
        Cria os botões laterais de navegação (Dashboard, Users, Client, Settings, Support)
        e define seus ícones, cores e comandos de alternância de frame.
        """
        espacamento = 60
        y_inicial = 260

        # botao dashboard
        img_dashboard = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/camadas.png"), size=(25, 25)
        )
        botao_dashboard = customtkinter.CTkButton(
            self,
            text="  DashBoard        ",
            fg_color="#101a55",
            bg_color="#101a55",
            hover_color="#101a95",
            font=("", 20),
            image=img_dashboard,
            corner_radius=5,
            command=lambda: self.alternar_frame(frame=self.frame_Dash),
        )
        botao_dashboard.place(x=0, y=y_inicial)

        # botao Users
        img_usuario = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/usuarios.png"), size=(25, 25)
        )
        botao_usuario = customtkinter.CTkButton(
            self,
            text="  Users                   ",
            fg_color="#101a55",
            bg_color="#101a55",
            hover_color="#101a95",
            font=("", 20),
            image=img_usuario,
            corner_radius=5,
            command=lambda: self.alternar_frame(frame=self.frame_Users),
        )
        botao_usuario.place(x=0, y=y_inicial + espacamento)

        # Clientes
        img_clientes = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/client.png"), size=(25, 25)
        )
        botao_cliente = customtkinter.CTkButton(
            self,
            text="  Client                  ",
            fg_color="#101a55",
            bg_color="#101a55",
            hover_color="#101a95",
            font=("", 20),
            image=img_clientes,
            corner_radius=5,
            command=lambda: self.alternar_frame(frame=self.frame_Client),
        )
        botao_cliente.place(x=0, y=y_inicial + espacamento * 2)

        # configuraçao
        img_config = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/config.png"), size=(25, 25)
        )
        botao_config = customtkinter.CTkButton(
            self,
            text="  Settings             ",
            image=img_config,
            fg_color="#101a55",
            bg_color="#101a55",
            hover_color="#101a95",
            font=("", 20),
            corner_radius=5,
            command=lambda: self.alternar_frame(frame=self.frame_Settings),
        )
        botao_config.place(x=0, y=y_inicial + espacamento * 3)

        # suporte
        img_suporte = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/boia.png"), size=(25, 25)
        )
        botao_suporte = customtkinter.CTkButton(
            self,
            text="  Support              ",
            image=img_suporte,
            fg_color="#101a55",
            bg_color="#101a55",
            hover_color="#101a95",
            font=("", 20),
            corner_radius=5,
            command=lambda: self.alternar_frame(frame=self.frame_Support),
        )
        botao_suporte.place(x=0, y=y_inicial + espacamento * 4)
        
        

    

    def configurar_janela(self):
        """
        Configura o tamanho, o tamanho mínimo e adiciona o frame lateral da janela principal.
        """
        self.geometry(f"{1000}x{1000}")
        self.minsize(height=self.winfo_screenheight(), width=self.winfo_screenwidth())
        self.lateral()

    def lateral(self):
        """
        Cria o frame lateral colorido da interface.
        """
        imagem_lateral = customtkinter.CTkFrame(
            self, fg_color="#101a55", width=204, height=800, corner_radius=0
        )
        imagem_lateral.place(x=0, y=0)

    def caminho_arquivo(self, path, file):
        """
        Retorna o caminho absoluto de um arquivo a partir do diretório atual.

        Args:
            path (str): Caminho relativo da pasta.
            file (str): Nome do arquivo.

        Returns:
            str: Caminho absoluto do arquivo.
        """
        diretorio = os.path.dirname(__file__)
        caminho = os.path.join(diretorio, path)
        arquivo = os.path.join(caminho, file)
        return arquivo

    def imagem(self, pasta, pasta2, arquivo, x, y):
        """
        Monta o caminho absoluto para uma imagem e pode ser usado para carregar imagens.

        Args:
            pasta (str): Nome da pasta principal.
            pasta2 (str): Nome da subpasta.
            arquivo (str): Nome do arquivo de imagem.
            x (int): Largura da imagem.
            y (int): Altura da imagem.
        """
        dirname = os.path.dirname(__file__)
        caminho = os.path.join(dirname, pasta)
        caminho2 = os.path.join(caminho, pasta2)
        caminho_absoluto = os.path.join(caminho, arquivo)

    def criar_labels(self):
        """
        Cria e posiciona labels de separação e o texto 'Overview' na interface.
        """
        linha = customtkinter.CTkLabel(
            self,
            text="__________________________________",
            fg_color="#101a55",
            text_color="white",
        )
        linha.place(x=0, y=0)

        linha2 = customtkinter.CTkLabel(
            self,
            text="__________________________________",
            fg_color="#101a55",
            text_color="white",
        )
        linha2.place(x=0, y=187)

        texto_overview = customtkinter.CTkLabel(
            self,
            text="Overview",
            font=("arial Bold", 17),
            fg_color="#101a55",
            text_color="white",
            bg_color="#101a55",
        )

        texto_overview.place(x=61, y=170)

    def exibir_falcao(self):
        """
        Exibe a imagem do falcão no topo da barra lateral.
        """
        imagem = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/falcao_main.png"), size=(200, 200)
        )
        falcao = customtkinter.CTkLabel(self, text="", image=imagem, fg_color="#101a55")
        falcao.place(x=1, y=0)


# aqui inicia a tela de login

tela_login=Tela_login()
tela_login.mainloop()




if tela_login.destruiu==True:
    """aqui verifica se a tela foi 
    destruida pra iniciar a outra tela
    """

    app = App()
    app.mainloop()
        
else:
    pass
