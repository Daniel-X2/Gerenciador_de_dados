import os

import customtkinter
from PIL import Image

from recursos.banco_de_dados.banco import Clientes, Funcionario
from recursos.banco_de_dados.criptografia.cripto import (criptografar_dados,
                                                         descriptografar_dados)
from recursos.frame.main_frame import (Client, DashBoard, Settings, Support,
                                       Users)
from recursos.login.login import Tela_login

# exportar o resto aqui


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.funcoes_iniciais()

    def funcoes_iniciais(self):
        self.funcoes_da_janela()
        self.img_falcao()
        self.label()
        self.frame_atual = ""
        self.frames()
        self.botoes_laterais()
        self.logica_frame(self.frame_Settings)

    def frames(self):
        # n1=customtkinter.CTkFrame()

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

    def logica_frame(self, frame):
        if frame.place_info():
            pass
        elif self.frame_atual != frame and self.frame_atual != "":
            self.frame_atual.place_forget()
            if self.frame_atual == frame:
                pass
            else:
                frame.place(x=205, y=0)
                self.frame_atual = frame
        else:
            if self.frame_atual == frame:
                pass
            else:
                frame.place(x=205, y=0)
                self.frame_atual = frame
    
    def botoes_laterais(self):
        # botao dashboard
        img_dashboard = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/camadas.png"), size=(25, 25)
        )
        botao_dashboard = customtkinter.CTkButton(
            self,
            text="  DashBoard        ",
            fg_color="#101a55",
            bg_color="#101a55",
            hover_color="#101a55",
            font=("", 20),
            image=img_dashboard,
            corner_radius=5,
            command=lambda: self.logica_frame(frame=self.frame_Dash),
       )  
        botao_dashboard.place(x=0, y=260)
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
            command=lambda: self.logica_frame(frame=self.frame_Users),
        )
        # foi necessario colocar um lambda para que a funçao podesse colocar um parametro sem causa bug
        botao_usuario.place(x=0, y=305)
        # Clientes
        # img_clientes=customtkinter.CTkImage(Image.open())
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
            command=lambda: self.logica_frame(frame=self.frame_Client),
        )
        botao_cliente.place(x=0, y=345)

        # analises

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
            command=lambda: self.logica_frame(frame=self.frame_Settings),
        )
        botao_config.place(x=0, y=425)
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
            command=lambda: self.logica_frame(frame=self.frame_Support),
        )
        botao_suporte.place(x=0, y=465)

        # foto de perfil usuario
        img_perfil = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/usuario-de-perfil.png")
        )
        botao_perfil = customtkinter.CTkButton(
            self,
            image=img_perfil,
            command=lambda: self.logica_frame(frame=self.overview),
        )
        botao_perfil.place(x=0, y=600)

    def verificar(self):
        usuario_atual = tela_login.usuario_atual
        senha_atual = tela_login.senha_atual
        funcionario = Funcionario()
        usuario_banco = funcionario.listar_funcionarios()[0]
        senha_banco = funcionario.listar_funcionarios()[1]
        if senha_atual == senha_banco and usuario_atual == usuario_banco:
            pass
        else:
            self.destroy()

    def funcoes_da_janela(self):
        self.geometry(f"{1000}x{1000}")
        self.minsize(height=self.winfo_screenheight(), width=self.winfo_screenwidth())
        self.lateral()

    def lateral(self):
        # criaçao do frame
        imagem_lateral = customtkinter.CTkFrame(
            self, fg_color="#101a55", width=204, height=800, corner_radius=0
        )
        imagem_lateral.place(x=0, y=0)

    def caminho_arquivo(self, path, file):
        diretorio = os.path.dirname(__file__)
        caminho = os.path.join(diretorio, path)
        arquivo = os.path.join(caminho, file)
        return arquivo

    def imagem(self, pasta, pasta2, arquivo, x, y):
        dirname = os.path.dirname(__file__)
        caminho = os.path.join(dirname, pasta)
        caminho2 = os.path.join(caminho, pasta2)
        caminho_absoluto = os.path.join(caminho, arquivo)

    def label(self):
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

    def img_falcao(self):
        imagem = customtkinter.CTkImage(
            Image.open("recursos/imagens_main/falcao_main.png"), size=(200, 200)
        )
        falcao = customtkinter.CTkLabel(self, text="", image=imagem, fg_color="#101a55")
        falcao.place(x=1, y=0)


# aqui inicia a tela de login

# tela_login=Tela_login()
# tela_login.mainloop()

# se a tela de login foi destruida inicia a tela do crud
app = App()
app.mainloop()


if 1 == 2:  # tela_login.destruiu==True:
    # segunda verificaçao do usuario
    try:
        # pega a senha e o usuario atual e verifica se sao os mesmos
        usuario_atual = tela_login.usuario_atual
        senha_atual = tela_login.senha_atual
        # aqui tenta descriptografar o usuario do funcionario pra verificar se a senha esta correta
        funcionario = Funcionario()
        usuario_banco = descriptografar_dados(
            funcionario.listar_funcionarios()[0], usuario_atual
        )
        senha_banco = descriptografar_dados(
            funcionario.listar_funcionarios()[1], senha_atual
        )
        # aqui ira iniciar somente caso a senha do banco de dados e a senha atual conbinar
        if senha_atual == senha_banco and usuario_atual == usuario_banco:
            app = App()
            app.mainloop()
        else:
            pass
    except:
        print("erro no login")
else:
    pass
