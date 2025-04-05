import customtkinter



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
        n1=customtkinter.CTkFrame(self,fg_color="#242424",width=200,height=800,corner_radius=0)
        font=Font(file="/media/daniel/projetos/PROJETOS/PYTHON/novo projeto/Ananda.ttf",family="Ananda")
        #n2=customtkinter.CTkLabel(n1,text="ola no frame",text_color="white",font=font)

        n2.place(x=50,y=10)
        n1.grid()
        

app=App()
app.mainloop()