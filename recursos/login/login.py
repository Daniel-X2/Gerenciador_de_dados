import customtkinter


class Tela_login(customtkinter.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("800x600")
        
        self.resizable(False,False)
        
        self.title("login CRUD")
        self.senha=customtkinter.StringVar()
        label=customtkinter.CTkEntry(self,fg_color="gray",textvariable=self.senha)
        label.place(x=90,y=50)
        self.verificar_senha()
    def verificar_senha(self):
        print(self.senha.get())
        self.after(2000,self.verificar_senha)
    def plano_de_fundo(self):
        caminho


tela_login=Tela_login()
tela_login.mainloop() 