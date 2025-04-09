import customtkinter
import os
from recursos.fontes import fonts
from recursos.login.login import  Tela_login

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.funçoes_da_janela()
        self.funçao_inicial()
        
    def funçoes_da_janela(self):
        self.geometry(f"{self._max_height}x{self._max_width}")
        self.minsize(height=self.winfo_screenheight(),width=self.winfo_screenwidth())
        self.frame()
        
    def funçao_inicial(self):
        print
    def frame(self):
        #criaçao do frame
        frame_lateral=customtkinter.CTkFrame(self,fg_color="#242424",width=200,height=800,corner_radius=0)
        frame_lateral.grid()
        #criaçao da label com fonte personalizada
        fonte=fonts.fontes("CRUD")#esse e uma funçao que faz o necessario pra colocar a fonte, o unico parametro e do texto
        image=customtkinter.CTkImage(fonte,size=(100,100))
        label_font=customtkinter.CTkLabel(frame_lateral,text="",image=image)
        label_font.place(x=50,y=10)
#aqui inicia a tela de login
tela_login=Tela_login()
tela_login.mainloop()
#se a tela de login foi destruida inicia a tela do crud
if tela_login.destruiu==True:
    app=App()
    app.mainloop()
else:
    pass

