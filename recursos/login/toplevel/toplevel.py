import customtkinter
import PIL
import webbrowser 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.resizable(False,False)
        self.title("help")

        self.funçoes_init()
    def funçoes_init(self):
        self.fundo()
        self.texto()
    def fundo(self):    
        #plano de fundo
        plano_de_fundo=customtkinter.CTkLabel(self,bg_color="#242424",text="",width=600,height=500)
        plano_de_fundo.place(x=0,y=0)
    def texto(self):
        text="""usuario: admin | senha: admin"""
        label=customtkinter.CTkLabel(self,text=text,bg_color="#242424",text_color="white")
        label.place(x=200,y=100)

        agradecimentos="""   bem vindo ao meu projeto 
        fico muito feliz que esteja olhando esse projeto
        se estiver interessado nesse projeto ou em outros basta
        acessar meu github"""
        label_agra=customtkinter.CTkLabel(self,text=agradecimentos,font=("ariel",18),bg_color="#242424",text_color="white")
        label_agra.place(x=40,y=250)
    def abrir_navegador(self):
        



app = App()
app.mainloop()