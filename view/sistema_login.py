import tkinter as tk
from datetime import datetime
from tkinter import Widget, ttk
from tkinter import messagebox
from view.elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens, Framecustomizado, Textcustomizado, Entrycustomizado, CheckButtoncustomizado
from imagens.imagens import load_images
class BaseCadastro:
    def __init__(self, root):
        self.root = root
        self.images = load_images()
        self.frame_secundario = tk.Canvas(self.root)
        self.frame_secundario.pack(expand='yes', fill="both")
        self.frame_caixa = tk.Canvas(self.frame_secundario, background='#020f59')
        self.frame_caixa.pack(expand='yes', fill="both")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.config(bg='#789048')
        self.entrada_nome()
        self.entrada_senha()
        self.entrada_data()
    
    
    def entrada_nome(self):
        self.nome_label = Labelcustomizada(self.frame_caixa, text='Digite seu nome:')
        self.nome_label.grid(row=1, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_entrada = Textcustomizado(self.frame_caixa)
        self.nome_entrada.grid(row=1, column=1, sticky=tk.NSEW, pady=5, padx=5)
    
    def entrada_senha(self):
        self.senha_label = Labelcustomizada(self.frame_caixa, text='Digite sua senha:')
        self.senha_label.grid(row=4, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_entrada = Entrycustomizado(self.frame_caixa)
        self.senha_entrada.grid(row=4, column=1, sticky=tk.NSEW, pady=5, padx=5)
        

    
    def entrada_data(self):
        self.data_label = Labelcustomizada(self.frame_caixa, text='Digite sua data de nascimento \n no formato dd-mm-YYYY :', justify='left')
        self.data_label.grid(row=8, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.data_entrada = Textcustomizado(self.frame_caixa)
        self.data_entrada.grid(row=8, column=1, sticky=tk.NSEW, pady=5, padx=5)
    
    def nome_get(self):
        return self.nome_entrada.get(1.0, tk.END).strip()
    
    def senha_get(self):
        return self.senha_entrada.get().strip()
    
    def data_get(self):
        return self.data_entrada.get(1.0, tk.END).strip()
    
    

 

class Registro(BaseCadastro):
    def __init__(self, root):
        super().__init__(root)
        self.root.title('REGISTRO')
        self.root.resizable(False,False)
        self.root.geometry("330x250")
        self.window = None
        self.button_enviar = Buttoncustomizado(self.frame_caixa, text='Cadastro', bg='#cdcfb7', fg='black')
        self.button_enviar.grid(row=12, column=0, pady=5, padx=5, columnspan=2)
        self.button_voltar = Buttoncustomizado(self.frame_caixa, text='Tela Principal', bg='#cdcfb7', fg='black')
        self.button_voltar.grid(row=13, column=0, pady=5, padx=5, columnspan=2)
        self.nome_dicas = Labelcustomizada(self.frame_caixa, text='Aviso:', font="Arial, 9")
        self.nome_dicas.grid(row=14, column=0, pady=5, padx=5, columnspan=3,rowspan=3)
        
class Login(BaseCadastro):
    def __init__(self, root):
        super().__init__(root)
        self.root.title('LOGIN')
        self.root.resizable(False,False)
        self.root.geometry("285x200")

        self.mostrar_senha = tk.Button(self.frame_caixa, image=self.images[16])
        self.mostrar_senha.grid(row=4, column=2, sticky=tk.NSEW, pady=5, padx=5)
        self.button_login = Buttoncustomizado(self.frame_caixa, text='Login', bg='#cdcfb7', fg='black')
        self.button_login.grid(row=5, column=0, pady=5, padx=5)
        
        self.label_reg = tk.Label(self.frame_caixa, text='Clique no botão para fazer cadastro caso seja sua primeira vez', font=("Arial", 8), wraplength=150, background='#cdcfb7')
        self.label_reg.grid(row=13, column=0, pady=5, padx=5,columnspan=2)
        
        self.button_reg = Buttoncustomizado(self.frame_caixa, text='Cadastro', bg='#cdcfb7', fg='black')
        self.button_reg.grid(row=5, column=1, pady=5, padx=5)
        
        self.button_voltar2 = Buttoncustomizado(self.frame_caixa, text='Tela Principal', bg='#cdcfb7', fg='black')
        self.button_voltar2.grid(row=14, column=0, pady=5, padx=5, columnspan=2)
        
    def entrada_data(self):
        pass

    def config_eventos(self):
        self.nome_entrada.bind('<KeyRelease>', self.dicas_nome)
        self.senha_entrada.bind('<KeyRelease>', self.dicas_senha)


