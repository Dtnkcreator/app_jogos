import tkinter as tk
from view.elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from view.sistema_login import Registro, BaseCadastro, Login
from model.modelo import UsuarioModel
from datetime import datetime
from imagens.imagens import load_images

class Controle:
    def __init__(self, root):
        self.root = root
        self.contar_click = 0
        self.current_user = None  # Para armazenar o usuário atual após login
        self.usuario_model = UsuarioModel()  # Instancia o modelo de usuário
        self.images = load_images

    def abrir_janela_registro(self):
        self.root.withdraw()
        try:
            self.window_log.destroy()
        except:
            pass
        self.window_reg = tk.Toplevel(self.root)
        self.registro = Registro(self.window_reg)
        self.config_button_enviar()
        self.config_eventos()
        self.registro.button_voltar.config(command=self.retornar_app_principal_reg)

    def abrir_janela_login(self):
        self.root.withdraw()
        self.window_log = tk.Toplevel(self.root)
        self.login = Login(self.window_log)
        
        def check_user_janela_login():
            nome_procurado = self.login.nome_get()
            senha_procurada = self.login.senha_get()
            if self.usuario_model.validar_usuario(nome_procurado, senha_procurada):
                self.current_user = nome_procurado  # Armazena o nome do usuário logado
                Mensagens.msgInfo(f'Login bem-sucedido para {nome_procurado}!')
                self.abrir_janela_principal()
            else:
                Mensagens.msgAtencao('Nome de usuário ou senha incorretos!')

        self.login.button_login.config(command=check_user_janela_login)
        self.login.button_reg.config(command=self.abrir_janela_registro)
        self.login.button_voltar2.config(command=self.retornar_app_principal_log)
        self.login.mostrar_senha.config(command=self.ocultar_senha)
        self.ocultar_senha_visible = False
    
    def abrir_janela_principal(self):
        self.window_log.destroy()
        self.root = tk.Toplevel(self.root)
        self.exibir_favoritos()

    def exibir_favoritos(self):
        if self.current_user:
            favoritos = self.usuario_model.obter_favoritos(self.current_user)
            label_favoritos = tk.Label(self.window_principal, text=f'Favoritos de {self.current_user}:')
            label_favoritos.pack()
            
            for jogo in favoritos:
                jogo_label = tk.Label(self.window_principal, text=jogo)
                jogo_label.pack()

    def retornar_app(self):
        self.root.deiconify()
        self.window_log.withdraw()

    def config_button_enviar(self):
        self.registro.button_enviar.config(command=self.salvar_usuario)

    def ocultar_senha(self):
        try:
            if hasattr(self, 'login') and hasattr(self.login, 'senha_entrada'):
                if self.login.senha_entrada.cget('show') == '•':
                    self.login.senha_entrada.config(show='')
                else:
                    self.login.senha_entrada.config(show='•')
        except:
            pass


    
    def dicas_nome(self, event):
        ler_nome = len(self.registro.nome_get())

        if 5 <= ler_nome <= 9:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário está no número de caracteres mínimo, pois tem {ler_nome}!', fg='green', wraplength=200)
        elif ler_nome == 10:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário chegou ao número de caracteres máximo, pois tem {ler_nome}!', fg='green', wraplength=200)
        elif ler_nome >= 11:
            Mensagens.msgAtencao(f'Seu nome de usuário chegou ao número máximo de caracteres, pois tem {ler_nome}!')
            self.registro.nome_entrada.delete(1.0, tk.END)
            self.registro.nome_dicas.config(text='Entrada resetada')
        else:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário não chegou ao número mínimo de caracteres, pois tem {ler_nome}!', fg='red', wraplength=200)
            if ler_nome <= 1:
                self.registro.nome_dicas.config(text=f'Seu nome de usuário é insuficiente, pois tem {ler_nome} caractere!', fg='red', wraplength=200)

    def dicas_senha(self, event):
        ler_senha = len(self.registro.senha_get())

        if 5 <= ler_senha <= 9:
            self.registro.nome_dicas.config(text=f'Sua senha está no número mínimo de caracteres, pois tem {ler_senha}!', fg='green', wraplength=200)
        elif ler_senha == 10:
            self.registro.nome_dicas.config(text=f'Sua senha chegou ao número máximo de caracteres, pois tem {ler_senha}!', fg='green', wraplength=200)
        elif ler_senha >= 11:
            Mensagens.msgAtencao(f'Sua senha chegou ao número máximo de caracteres, pois tem {ler_senha}!')
            self.registro.senha_entrada.delete(0, tk.END)
            self.registro.nome_dicas.config(text='Entrada resetada')
        else:
            self.registro.nome_dicas.config(text=f'Sua senha não chegou ao número mínimo de caracteres, pois tem {ler_senha}!', fg='red', wraplength=200)
            if ler_senha <= 1:
                self.registro.nome_dicas.config(text=f'Sua senha é insuficiente, pois tem {ler_senha} caractere!', fg='red', wraplength=200)

    def dicas_data(self, event):
        try:
            data_formatada = datetime.strptime(self.registro.data_get(), '%d-%m-%Y')
            data_padrao = data_formatada.strftime('%d-%m-%Y')
            self.registro.nome_dicas.config(text=f'Sua data de nascimento ficou: {data_padrao}', fg='green')
        except ValueError:
            self.registro.nome_dicas.config(text='Inválido', fg='red')

    def config_eventos(self):
        self.registro.nome_entrada.bind('<KeyRelease>', self.dicas_nome)
        self.registro.senha_entrada.bind('<KeyRelease>', self.dicas_senha)
        self.registro.data_entrada.bind('<KeyRelease>', self.dicas_data)

    def salvar_usuario(self):
        nome = self.registro.nome_get()
        senha = self.registro.senha_get()
        data = self.registro.data_get()

        def verificar_campo_vazio():
            nome_status = self.registro.nome_get()
            senha_status = self.registro.senha_get()
            data_status = self.registro.data_get()

            if nome == '' and senha == '' and data == '':
                Mensagens.msgAtencao('Os três campos estão vazios, preencha por favor!')
            elif nome_status.cget('fg') == 'red' and data_status.cget('fg') == 'red' and senha_status.cget('fg') == 'red':
                Mensagens.msgAtencao('Os três campos não seguem os requisitos! Preencha por favor!')
            elif nome_status.cget('fg') != 'red' and data_status.cget('fg') == 'red' and senha_status.cget('fg') == 'red':
                Mensagens.msgAtencao('Os campos data e senha não seguem os requisitos! Preencha por favor!')
            elif nome_status.cget('fg') == 'red' and data_status.cget('fg') != 'red' and senha_status.cget('fg') == 'red':
                Mensagens.msgAtencao('Os campos nome e senha não seguem os requisitos! Preencha por favor!')
            elif nome_status.cget('fg') == 'red' and data_status.cget('fg') == 'red' and senha_status.cget('fg') != 'red':
                Mensagens.msgAtencao('Os campos nome e data não seguem os requisitos! Preencha por favor!')
            elif senha_status.cget('fg') == 'red':
                Mensagens.msgAtencao('O campo senha não segue requisitos! Preencha por favor!')
            elif nome_status.cget('fg') == 'red':
                Mensagens.msgAtencao('O campo nome não segue requisitos! Preencha por favor!')
            elif data_status.cget('fg') == 'red':
                Mensagens.msgAtencao('O campo data não segue requisitos! Preencha por favor!')
            elif nome != '' and senha == '' and data == '':
                Mensagens.msgAtencao('Os campos data e senha estão vazios, preencha por favor!')
            elif nome == '' and senha != '' and data == '':
                Mensagens.msgAtencao('Os campos data e nome estão vazios, preencha por favor!')
            elif nome == '' and senha == '' and data != '':
                Mensagens.msgAtencao('Os campos nome e senha estão vazios, preencha por favor!')
            elif nome == '':
                Mensagens.msgAtencao('O campo nome está vazio, preencha por favor!')
            elif senha == '':
                Mensagens.msgAtencao('O campo senha está vazio, preencha por favor!')
            elif data == '':
                Mensagens.msgAtencao('O campo data está vazio, preencha por favor!')
            elif nome_status.cget('fg') == 'red' and data == '' and senha == '':
                Mensagens.msgAtencao('O campo nome não seguiu os requisitos e ademais, os campos data e senha estão vazios, preencha por favor!')
            else:
                self.contar_click += 1
                if self.contar_click >= 2:
                    Mensagens.msgAtencao('Seu cadastro já foi enviado!')
                else:
                    self.registro.nome_entrada.config(state=tk.DISABLED)
                    self.registro.data_entrada.config(state=tk.DISABLED)
                    self.registro.senha_entrada.config(state=tk.DISABLED)
                    data_formatada = datetime.strptime(data, '%d-%m-%Y')
                    self.usuario_model.salvar_usuario(nome, data_formatada, senha)
                    Mensagens.msgInfo('Cadastro realizado com sucesso!')
                    return self.abrir_janela_login()
        
        verificar_campo_vazio()

    def retornar_app_principal_log(self):
        self.window_log.destroy()
        self.root.deiconify()

    def retornar_app_principal_reg(self):
        self.window_reg.destroy()
        self.root.deiconify()
     
if __name__ == '__main__':
    root = tk.Tk()
    Controle(root)
    root.mainloop()
