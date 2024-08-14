import tkinter as tk
from tkinter import messagebox
from view.elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from view.sistema_login import Registro, BaseCadastro, Login
from model.modelo import UsuarioModel
from datetime import datetime
from imagens.imagens import load_images
from model.user import User

class Controle:
    def __init__(self, root):
        self.root = root
        self.current_user = None  # Para armazenar o usuário atual após login
        self.usuario_model = UsuarioModel()  # Instancia o modelo de usuário
        self.images = load_images()

    def obter_usuario_logado(self):
        return self.current_user

    def abrir_janela_registro(self):
        if self.current_user is None:
            self.root.withdraw()
            try:
                self.window_log.destroy()
            except AttributeError:
                pass
            self.window_reg = tk.Toplevel(self.root)
            self.registro = Registro(self.window_reg)
            self.config_button_enviar()
            self.config_eventos()
            self.registro.button_voltar.config(command=self.retornar_app_principal_reg)
        else:
            Mensagens.msgAtencao('Saia da conta logada para criar uma nova conta!')

    def abrir_janela_login(self):
        if self.current_user is None:  # Só abrir a janela de login se não estiver logado
            self.root.withdraw()
            self.window_log = tk.Toplevel(self.root)
            self.login = Login(self.window_log)

            def check_user_janela_login():
                nome_procurado = self.login.nome_get()
                senha_procurada = self.login.senha_get()
                if self.usuario_model.validar_usuario(nome_procurado, senha_procurada):
                    self.current_user = nome_procurado  # Armazena a instância do usuário logado
                    Mensagens.msgInfo(f'Login bem-sucedido! \nBem-vindo {self.current_user}!')
                    self.abrir_janela_principal()
                    self.window_log.destroy()
                else:
                    Mensagens.msgAtencao('Nome de usuário ou senha incorretos!')

            self.login.button_login.config(command=check_user_janela_login)
            self.login.button_reg.config(command=self.abrir_janela_registro)
            self.login.button_voltar2.config(command=self.retornar_app_principal_log)
            self.login.mostrar_senha.config(command=self.ocultar_senha)
            self.ocultar_senha_visible = False
        else:
            Mensagens.msgAtencao('Você já está logado!')

    def abrir_janela_principal(self):
        if hasattr(self, 'window_log'):
            self.window_log.destroy()
        self.root.deiconify()  # Exibir favoritos ou outras informações relacionadas ao usuário

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
        except AttributeError:
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
            self.registro.nome_dicas.config(text='Aviso: Entrada resetada', fg='red')
        else:
            self.registro.nome_dicas.config(text=f'Aviso: Seu nome de usuário não chegou ao número mínimo de caracteres, pois tem {ler_nome}!', fg='red', wraplength=200)
            if ler_nome <= 1:
                self.registro.nome_dicas.config(text=f'Aviso: Seu nome de usuário é insuficiente, pois tem {ler_nome} caractere!', fg='red', wraplength=200)

    def dicas_senha(self, event):
        ler_senha = len(self.registro.senha_get())

        if 1 <= ler_senha <= 4:
            self.registro.nome_dicas.config(text=f'Aviso: Sua senha é fraca!', fg='red', wraplength=200)
        elif 5 <= ler_senha <= 10:
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

    def abrir_janela_favoritos(self):
        if not self.current_user:
            messagebox.showwarning("Erro", "Você precisa realizar o login primeiro.")
            return

        if hasattr(self, 'favorito_window') and self.favorito_window and self.favorito_window.winfo_exists():
            self.favorito_window.lift()
            self.favorito_window.focus()
            return

        self.favorito_window = tk.Toplevel(self.root)
        self.favorito_window.title("Favoritos")
        self.favorito_window.geometry("300x400")
        self.favorito_window.resizable(False, False)

        frame_favorito = tk.Label(self.favorito_window, image=self.images[15])
        frame_favorito.pack(fill="both", expand=True)

        favorito_label = tk.Label(frame_favorito, text="Meus Favoritos", font=("Arial", 12), background="#cdcfb7")
        favorito_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

        frame_lista_botao = tk.Label(frame_favorito, image=self.images[15])
        frame_lista_botao.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        listbox_favoritos = tk.Listbox(frame_lista_botao, background="#cdcfb7", selectmode=tk.SINGLE)
        listbox_favoritos.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        botao_remover_favorito = tk.Button(frame_lista_botao, text="Remover Favorito", command=lambda: self.remover_favorito(listbox_favoritos))
        botao_remover_favorito.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="n")

        frame_favorito.grid_rowconfigure(1, weight=1)
        frame_favorito.grid_columnconfigure(0, weight=1)
        frame_lista_botao.grid_rowconfigure(0, weight=1)
        frame_lista_botao.grid_columnconfigure(0, weight=1)

        self.atualizar_favoritos(listbox_favoritos)

        self.favorito_window.protocol("WM_DELETE_WINDOW", self.favorito_window.destroy)

    def atualizar_favoritos(self, listbox_favoritos):
        listbox_favoritos.delete(0, tk.END)
        favoritos = self.usuario_model.obter_favoritos(self.current_user)
        for fav in favoritos:
            listbox_favoritos.insert(tk.END, fav)

    def remover_favorito(self, listbox_favoritos):
        if not self.current_user:
            messagebox.showwarning("Erro", "Você precisa realizar o login primeiro.")
            return

        selecionado = listbox_favoritos.curselection()
        if not selecionado:
            messagebox.showwarning("Erro", "Você não tem nenhum jogo para remover.")
            return

        jogo = listbox_favoritos.get(selecionado)
        if self.usuario_model.remover_favorito(self.current_user, jogo):
            messagebox.showinfo("Remover Favorito", f"{jogo} removido dos favoritos.")
            self.atualizar_favoritos(listbox_favoritos)
        else:
            messagebox.showerror("Erro", "Erro ao remover o jogo dos favoritos.")

if __name__ == '__main__':
    root = tk.Tk()
    controle = Controle(root)
    menu = tk.Menu(root)
    root.config(menu=menu)
    root.mainloop()
