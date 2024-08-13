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
        self.images = load_images()
        self.menu_conta = None  # Armazenar o menu de contas

    def obter_usuario_logado(self):
        return self.current_user

    
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
        if self.current_user is None:  # Só abrir a janela de login se não estiver logado
            self.root.withdraw()
            self.window_log = tk.Toplevel(self.root)
            self.login = Login(self.window_log)

            def check_user_janela_login():
                nome_procurado = self.login.nome_get()
                senha_procurada = self.login.senha_get()
                if self.usuario_model.validar_usuario(nome_procurado, senha_procurada):
                    self.current_user = nome_procurado  # Armazena o nome do usuário logado
                    Mensagens.msgInfo(f'Login bem-sucedido! \nBem-vindo {self.current_user}!')
                    self.abrir_janela_principal()
                    if self.menu_conta:
                        self.menu_conta.entryconfig("Login", state=tk.DISABLED)
                        self.menu_conta.entryconfig("Cadastro", state=tk.DISABLED)
                    self.window_log.destroy()
                else:
                    Mensagens.msgAtencao('Nome de usuário ou senha incorretos!')

            self.login.button_login.config(command=check_user_janela_login)
            self.login.button_reg.config(command=self.abrir_janela_registro)
            self.login.button_voltar2.config(command=self.retornar_app_principal_log)
            self.login.mostrar_senha.config(command=self.ocultar_senha)
            self.ocultar_senha_visible = False

    def abrir_janela_principal(self):
        if hasattr(self, 'window_log'):
            self.window_log.destroy()
        self.root.deiconify()

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

        if 1 <= ler_nome <= 9:
            self.registro.nome_dicas.config(text=f'Aviso: Seu nome de usuário é valido!', fg='green', wraplength=200)
        elif ler_nome == 10:
            self.registro.nome_dicas.config(text=f'Aviso: Seu nome de usuário chegou ao número de caracteres máximo, pois tem {ler_nome}!', fg='red', wraplength=200)
        elif ler_nome >= 20:
            Mensagens.msgAtencao(f'Aviso: Seu nome de usuário chegou ao número máximo de caracteres, pois tem {ler_nome}!')
            self.registro.nome_entrada.delete(1.0, tk.END)
            self.registro.nome_dicas.config(text='Aviso: Entrada resetada',fg='red')
        else:
            self.registro.nome_dicas.config(text=f'Aviso: Seu nome de usuário não chegou ao número mínimo de caracteres, pois tem {ler_nome}!', fg='red', wraplength=200)
            if ler_nome <= 1:
                self.registro.nome_dicas.config(text=f'Aviso: Seu nome de usuário é insuficiente, pois tem {ler_nome} caractere!', fg='red', wraplength=200)

    def dicas_senha(self, event):
        ler_senha = len(self.registro.senha_get())

        if 1 <= ler_senha <= 4:
            self.registro.nome_dicas.config(text=f'Aviso: Sua senha é fraca!', fg='red', wraplength=200)
        elif 5<= ler_senha <=10:
            self.registro.nome_dicas.config(text=f'Aviso: Sua senha é moderada, pois tem {ler_senha}!', fg='green', wraplength=200)
        elif ler_senha >= 20:
            Mensagens.msgAtencao(f'Aviso: Sua senha chegou ao número máximo de caracteres, pois tem {ler_senha}!')
            self.registro.senha_entrada.delete(0, tk.END)
            self.registro.nome_dicas.config(text='Aviso: Entrada resetada')
        else:
            self.registro.nome_dicas.config(text=f'Aviso: Sua senha não chegou ao número mínimo de caracteres, pois tem {ler_senha}!', fg='red', wraplength=200)
            if ler_senha <= 1:
                self.registro.nome_dicas.config(text=f'Aviso: Sua senha é insuficiente, pois tem {ler_senha} caractere!', fg='red', wraplength=200)

    def dicas_data(self, event):
        try:
            data_formatada = datetime.strptime(self.registro.data_get(), '%d-%m-%Y')
            data_padrao = data_formatada.strftime('%d-%m-%Y')
            self.registro.nome_dicas.config(text=f'Aviso: Sua data de nascimento ficou: {data_padrao}', fg='green')
        except ValueError:
            self.registro.nome_dicas.config(text='Aviso: A data de nascimento deve ter o\n formato dd-mm-YYYY!', fg='red')

    def config_eventos(self):
        self.registro.nome_entrada.bind('<KeyRelease>', self.dicas_nome)
        self.registro.senha_entrada.bind('<KeyRelease>', self.dicas_senha)
        self.registro.data_entrada.bind('<KeyRelease>', self.dicas_data)

    def salvar_usuario(self):
        nome = self.registro.nome_get()
        senha = self.registro.senha_get()
        data = self.registro.data_get()

        def verificar_campo_vazio():
            nome = self.registro.nome_get()
            senha = self.registro.senha_get()
            data = self.registro.data_get()

            mensagens = []
            if nome == '':
                mensagens.append('O campo nome está vazio, preencha por favor!')
            if senha == '':
                mensagens.append('O campo senha está vazio, preencha por favor!')
            if data == '':
                mensagens.append('O campo data está vazio, preencha por favor!')

            if nome == 'red':
                mensagens.append('O campo nome não segue requisitos! Preencha por favor!')
            if senha == 'red':
                mensagens.append('O campo senha não segue requisitos! Preencha por favor!')
            if data == 'red':
                mensagens.append('O campo data não segue requisitos! Preencha por favor!')

            if mensagens:
                Mensagens.msgAtencao('\n'.join(mensagens))
                return False
            return True

        if verificar_campo_vazio():
            self.registro.nome_entrada.config(state=tk.DISABLED)
            self.registro.data_entrada.config(state=tk.DISABLED)
            self.registro.senha_entrada.config(state=tk.DISABLED)

            # Verificar se o usuário já existe
            if self.usuario_model.usuario_existe(nome):
                Mensagens.msgAtencao('Nome de usuário já está em uso. Por favor, escolha outro.')
                self.registro.nome_entrada.config(state=tk.NORMAL)
                self.registro.data_entrada.config(state=tk.NORMAL)
                self.registro.senha_entrada.config(state=tk.NORMAL)
                return

            try:
                data_formatada = datetime.strptime(data, '%d-%m-%Y').date()
                if self.usuario_model.criar_usuario(nome, senha, data_formatada):
                    Mensagens.msgInfo('Cadastro realizado com sucesso!')
                    self.window_reg.destroy()
                    self.abrir_janela_login()
                else:
                    Mensagens.msgAtencao('Não foi possível salvar o usuário. Tente novamente.')
            except ValueError:
                Mensagens.msgAtencao('Data inválida, por favor use o formato dd-mm-YYYY!')
                self.registro.nome_entrada.config(state=tk.NORMAL)
                self.registro.data_entrada.config(state=tk.NORMAL)
                self.registro.senha_entrada.config(state=tk.NORMAL)

    def retornar_app_principal_log(self):
        self.window_log.destroy()
        self.root.deiconify()

    def retornar_app_principal_reg(self):
        self.window_reg.destroy()
        self.root.deiconify()
    def obter_nome_usuario(self):
        return self.usuario_logado

if __name__ == '__main__':
    root = tk.Tk()
    controle = Controle(root)
    menu = tk.Menu(root)
    root.mainloop()
