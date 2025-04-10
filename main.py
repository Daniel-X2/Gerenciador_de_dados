import customtkinter
import os
from hashlib import sha256
from recursos.login.login import  Tela_login
from recursos.banco_de_dados.banco import Conexao_clientes,Conexao_funcionario

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.funçoes_da_janela()
        self.funçao_inicial()
    def funçao_inicial():
        print
    def funçoes_da_janela(self):
        self.geometry(f"{self._max_height}x{self._max_width}")
        self.minsize(height=self.winfo_screenheight(),width=self.winfo_screenwidth())
        self.frame()
    def frame(self):
        #criaçao do frame
        frame_lateral=customtkinter.CTkFrame(self,fg_color="#242424",width=200,height=800,corner_radius=0)
        frame_lateral.grid()
        
#aqui inicia a tela de login
tela_login=Tela_login()
tela_login.mainloop()
#se a tela de login foi destruida inicia a tela do crud

if tela_login.destruiu==True:
    #segunda verificaçao do usuario
    usuario_atual=sha256(tela_login.usuario_atual.encode()).digest()
    senha_atual=sha256(tela_login.senha_atual.encode()).digest()
    
    app=App()
    app.mainloop()
else:
    pass

