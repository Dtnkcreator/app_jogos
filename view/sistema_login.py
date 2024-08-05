import tkinter as tk
from datetime import datetime
from tkinter import Widget, ttk
from tkinter import messagebox
from view.elementos_tkinter import Labelcustomizada, LabelcustomizadaTitulo, Buttoncustomizado, Mensagens, Framecustomizado, Textcustomizado, Entrycustomizado, CheckButtoncustomizado

class BaseCadastro:
    def __init__(self, root):
        self.root = root
        self.frame_caixa = Framecustomizado(self.root,width=400, height=400)
        self.frame_caixa.grid(row=0, column=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.config(bg='#789048')
        self.entrada_nome()
        self.entrada_senha()
        self.entrada_data()
    
    
    def entrada_nome(self):
        self.nome_titulo = LabelcustomizadaTitulo(self.frame_caixa, text='CAMPO NOME.')
        self.nome_titulo.grid(row=0, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_label = Labelcustomizada(self.frame_caixa, text='Digite seu nome :')
        self.nome_label.grid(row=1, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_entrada = Textcustomizado(self.frame_caixa)
        self.nome_entrada.grid(row=1, column=1, sticky=tk.NSEW, pady=5, padx=5)

        self.nome_dicas = Labelcustomizada(self.frame_caixa)
        self.nome_dicas.grid(row=2, column=0, sticky=tk.NSEW, pady=5, padx=5)
    
    def entrada_senha(self):
        self.senha_titulo = LabelcustomizadaTitulo(self.frame_caixa, text='CAMPO SENHA.')
        self.senha_titulo.grid(row=3, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_label = Labelcustomizada(self.frame_caixa, text='Digite sua senha :')
        self.senha_label.grid(row=4, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_entrada = Entrycustomizado(self.frame_caixa)
        self.senha_entrada.grid(row=4, column=1, sticky=tk.NSEW, pady=5, padx=5)
        
        
        self.mostrar_senha = CheckButtoncustomizado(self.frame_caixa, text='Ocultar senha', bg='white')
        self.mostrar_senha.grid(row=5, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.senha_dicas = Labelcustomizada(self.frame_caixa)
        self.senha_dicas.grid(row=6, column=0, sticky=tk.NSEW, pady=5, padx=5)

    
    def entrada_data(self):
        self.data_titulo = LabelcustomizadaTitulo(self.frame_caixa, text='CAMPO DATA.')
        self.data_titulo.grid(row=7, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.data_label = Labelcustomizada(self.frame_caixa, text='Digite sua data de nascimento \n no formato dd-mm-YYYY :', justify='left')
        self.data_label.grid(row=8, column=0, sticky=tk.NSEW, pady=5, padx=5)

        self.data_entrada = Textcustomizado(self.frame_caixa)
        self.data_entrada.grid(row=8, column=1, sticky=tk.NSEW, pady=5, padx=5)

        self.data_dicas = Labelcustomizada(self.frame_caixa)
        self.data_dicas.grid(row=9, column=0, sticky=tk.NSEW, pady=5, padx=5)
    
    def nome_get(self):
        return self.nome_entrada.get(1.0, tk.END).strip()
    
    def senha_get(self):
        return self.senha_entrada.get().strip()
    
    def data_get(self):
        return self.data_entrada.get(1.0, tk.END).strip()

 

class Registro(BaseCadastro):
    def __init__(self, root):
        super().__init__(root)
        self.root.title('Registro de usuário')
        self.window = None
        self.button_enviar = Buttoncustomizado(self.frame_caixa, text='Enviar cadastro', bg='black', fg='white')
        self.button_enviar.grid(row=12, column=0, pady=5, padx=5)
        
        
    


class Login(BaseCadastro):
    def __init__(self, root):
        super().__init__(root)
        self.root.title('Login de usuário')
        self.button_login = Buttoncustomizado(self.frame_caixa, text='Enviar login', bg='black', fg='white')
        self.button_login.grid(row=12, column=0, pady=5, padx=5)

        self.button_senha = Buttoncustomizado(self.frame_caixa, text='Esqueci senha', bg='black', fg='white')
        self.button_senha.grid(row=16, column=0, pady=5, padx=5)
        
        self.label_reg = Labelcustomizada(self.frame_caixa, text='Não tem cadastro ? Clique no botão abaixo para fazer cadastro.',  wraplength=150)
        self.label_reg.grid(row=19, column=0, pady=5, padx=5)

        self.button_reg = Buttoncustomizado(self.frame_caixa, text='Fazer cadastro', bg='black', fg='white')
        self.button_reg.grid(row=20, column=0, pady=5, padx=5)
    
    def entrada_data(self):
        pass

    def config_eventos(self):
        self.nome_entrada.bind('<KeyRelease>', self.dicas_nome)
        self.senha_entrada.bind('<KeyRelease>', self.dicas_senha)


