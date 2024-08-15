import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from imagens.imagens import load_images
from botoes_e_labels import entrada_do_mouse, saida_do_mouse, cria_label_jogo, cria_label_subtitulo, cria_label_titulo,criar_button,cria_label,saida_do_mouse_inicio, entrada_do_mouse_inicio, toca_som
from model.model import UsuarioModel
import pygame
from tkcalendar import DateEntry

pygame.mixer.init()

# Carregue o som
click_som = pygame.mixer.Sound(r"C:\Users\182400280\Downloads\Python\database\SQLite\jogos\antigo\app_jogos\click.wav")
mensagem_som = pygame.mixer.Sound(r"C:\Users\182400280\Downloads\Python\database\SQLite\jogos\antigo\app_jogos\mensagem.wav")
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Jogos")
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        self.usuario_model = UsuarioModel()
        self.setup()
        self.create_widgets()
        self.create_menu()
    
        self.login_window = None
        self.favorito_window = None
        self.info_window = None
        self.cadastro_window = None
        self.usuario_logado = None

        self.root.protocol("WM_DELETE_WINDOW", self.fechar_app)
    
    def setup(self):
        self.root.bind("<F11>", self.tela_cheia)
        self.root.bind("<Escape>", self.desativ_tela_cheia)
        self.images = load_images()

    def create_menu(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.menu_configuracoes = tk.Menu(self.menubar, tearoff=0)
        self.submenu_opc_AlterarCor()
        self.menu_configuracoes.add_cascade(label="Cor do fundo", menu=self.corfundo)
        self.menu_configuracoes.add_command(label="Tela Cheia <F11>", command=self.tela_cheia)
        self.menu_configuracoes.add_command(label="Tamanho de Tela Normal <ESC>", command=self.desativ_tela_cheia)
        self.menu_configuracoes.add_command(label="Sair", command=self.fechar_app)
        self.menubar.add_cascade(label="Configurações", menu=self.menu_configuracoes)
        menu_conta = tk.Menu(self.menubar, tearoff=0)
        menu_conta.add_command(label="Favoritos", command=self.abrir_janela_favoritos)
        menu_conta.add_command(label="Login", command=self.abrir_janela_login)
        self.menubar.add_cascade(label="Conta", menu=menu_conta)
        self.menu_usuario = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Usuário", menu=self.menu_usuario)
        self.menu_usuario.add_command(label="Usuário: Não Logado", state=tk.DISABLED)

    def sair_usuario(self):
        # Função para sair do usuário
        if self.usuario_logado:
            mensagem_som.play()
            resposta = messagebox.askyesno("Confirmação", "Deseja realmente sair?")
            if resposta:
                self.usuario_logado = None
                mensagem_som.play()
                messagebox.showinfo("Sair", "Você foi desconectado com sucesso.")
                self.menu_usuario.delete(0, tk.END)
                self.menu_usuario.add_command(label="Usuário: Não Logado", state=tk.DISABLED)
        else:
            pass

    def submenu_opc_AlterarCor(self):
        cores = {
            'Verde Escuro (Default)': '#607848',
            'Amarelo': '#aa9e29',
            'Laranja': '#b25f26',
            'Vermelho': '#6f150b',
            'Rosa': '#f4d2d9',
            'Roxo': '#6b5197',
            'Azul': '#538bcc',
            'Branco': 'white',
            'Verde Invertido': '#789048'
        }

        self.corfundo = tk.Menu(self.menu_configuracoes, tearoff=0)
        for label, cor in cores.items():
            self.corfundo.add_command(label=label, command=lambda cor=cor: self.Backgrounds(cor))

    def Backgrounds(self, cor):
        cores_fundo = {
            "#607848": ('#607848', '#789048', '#789048', '#789048'),
            "#aa9e29": ('#aa9e29', '#d0c152', '#d0c152', '#d0c152'),
            "#538bcc": ('#538bcc', '#88bce6', '#88bce6', '#88bce6'),
            "#b25f26": ('#b25f26', '#c5773d', '#c5773d', '#c5773d'),
            "white": ('white', '#deede0', '#deede0', '#deede0'),
            "#6b5197": ('#6b5197', '#8f73bc', '#8f73bc', '#8f73bc'),
            "#f4d2d9": ('#f4d2d9', '#e9a5b2', '#e9a5b2', '#e9a5b2'),
            "#6f150b": ('#6f150b', '#801c0f', '#801c0f', '#801c0f'),
            "#789048": ('#789048', '#607848', '#607848', '#607848')
        }

        fundo = cores_fundo.get(cor, ('#ffffff', '#ffffff', '#ffffff', '#ffffff'))
        self.frame_principal.configure(bg=fundo[0])
        self.frame_destaques.configure(bg=fundo[1])
        self.frame_retro.configure(bg=fundo[2])
        self.frame_fps.configure(bg=fundo[3])
                


    def create_widgets(self):

        self.frame = tk.Frame(self.root, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame, background="#607848")
        self.scroll_x = tk.Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        

        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scroll_x.grid(row=1, column=0, sticky="ew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        self.frame_principal = tk.Frame(self.canvas, background="#607848")
        self.canvas.create_window((0, 0), window=self.frame_principal, anchor="nw")

        self.frame_principal.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.create_header()
        self.create_game_sections()

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def create_header(self):
        self.label_titulo1 = cria_label_titulo(self.frame_principal, "Aplicativo de Jogos", 0, 0, 5)
        self.time_label = tk.Label(self.frame_principal, font=("Arial", 10), background="#cdcfb7")
        self.time_label.grid(row=0, column=4, padx=10, pady=10, sticky="e")
        self.time_label.bind("<Enter>", lambda e: entrada_do_mouse(e, self.time_label))
        self.time_label.bind("<Leave>", lambda e: saida_do_mouse(e, self.time_label))
        self.update_time()

    def update_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%A, %d %B %Y")
        self.time_label.config(text=f"{current_date}\n{current_time}")
        self.root.after(1000, self.update_time)

    def create_game_sections(self):
        # Jogos em Destaque
        label_subtitulo_destaques = cria_label_subtitulo(self.frame_principal, "Jogos em Destaque", 0, 0, 5, 5)

        self.frame_destaques = tk.Frame(self.frame_principal, background="#789048")
        self.frame_destaques.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # Super Mario Bros.
        label1 = cria_label_jogo(self.frame_destaques, "Super Mario World", self.images[0], 0, 0, 5, 5,"Super Mario World")
        self.criar_button_favoritos(self.frame_destaques, "Super Mario World", 1, 0)
        button_download1 = self.cria_button_download(self.frame_destaques, 2, 0, 5, 5)

        # Kingdom Rush
        label2 = cria_label_jogo(self.frame_destaques, "Kingdom Rush", self.images[1], 0, 1, 5, 5,"Kingdom Rush")
        self.criar_button_favoritos(self.frame_destaques, "Kingdom Rush", 1, 1)
        button_download2 = self.cria_button_download(self.frame_destaques, 2, 1, 5, 5)

        # CS:GO
        label3 = cria_label_jogo(self.frame_destaques, "CS:GO", self.images[2], 0, 2, 5, 5,"CS:GO")
        self.criar_button_favoritos(self.frame_destaques, "CS:GO", 1, 2)
        button_download3 = self.cria_button_download(self.frame_destaques, 2, 2, 5, 5)

        # Bloons TD 6
        label4 = cria_label_jogo(self.frame_destaques, "Bloons TD 6", self.images[3], 0, 3, 5, 5,"Bloons TD 6")
        self.criar_button_favoritos(self.frame_destaques, "Bloons TD 6", 1, 3)
        button_download4 = self.cria_button_download(self.frame_destaques, 2, 3, 5, 5)

        # Metal Slug 3
        label10 = cria_label_jogo(self.frame_destaques, "Metal Slug 3", self.images[9], 0, 4, 5, 5,"Metal Slug 3")
        self.criar_button_favoritos(self.frame_destaques, "Metal Slug 3", 1, 4)
        button_download10 = self.cria_button_download(self.frame_destaques, 2, 4, 5, 5)

        # Jogos Retrô
        label_subtitulo_plataforma = cria_label_subtitulo(self.frame_principal, "Jogos Retrô", 2, 0, 5, 5)

        self.frame_retro = tk.Frame(self.frame_principal, background="#789048")
        self.frame_retro.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # Pacman
        label5 = cria_label_jogo(self.frame_retro, "Pacman", self.images[4], 0, 0, 5, 5,"Pacman")
        self.criar_button_favoritos(self.frame_retro, "Pacman", 1, 0)
        button_download5 = self.cria_button_download(self.frame_retro, 2, 0, 5, 5)

        # Donkey Kong
        label6 = cria_label_jogo(self.frame_retro, "Donkey Kong Country", self.images[5], 0, 1, 5, 5,"Donkey Kong Country")
        self.criar_button_favoritos(self.frame_retro, "Donkey Kong Country", 1, 1)
        button_download6 = self.cria_button_download(self.frame_retro, 2, 1, 5, 5)

        # Tetris
        label7 = cria_label_jogo(self.frame_retro, "Tetris", self.images[6], 0, 2, 5, 5,"Tetris")
        self.criar_button_favoritos(self.frame_retro, "Tetris", 1, 2)
        button_download7 = self.cria_button_download(self.frame_retro, 2, 2, 5, 5)

        # Contra
        label8 = cria_label_jogo(self.frame_retro, "Contra", self.images[7], 0, 3, 5, 5,"Contra")
        self.criar_button_favoritos(self.frame_retro, "Contra", 1, 3)
        button_download8 = self.cria_button_download(self.frame_retro, 2, 3, 5, 5)

        # Sonic
        label9 = cria_label_jogo(self.frame_retro, "Sonic", self.images[8], 0, 4, 5, 5,"Sonic")
        self.criar_button_favoritos(self.frame_retro, "Sonic", 1, 4)
        button_download9 = self.cria_button_download(self.frame_retro, 2, 4, 5, 5)

        # Jogos FPS
        label_subtitulo_fps = cria_label_subtitulo(self.frame_principal, "Jogos FPS", 4, 0, 5, 5)

        self.frame_fps = tk.Frame(self.frame_principal, background="#789048")
        self.frame_fps.grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")


        # ARK
        label11 = cria_label_jogo(self.frame_fps, "ARK: Survival Ascended", self.images[10], 0, 0, 5, 5,"ARK: Survival Ascended")
        self.criar_button_favoritos(self.frame_fps,"ARK: Survival Ascended", 1, 0)
        button_download11 = self.cria_button_download(self.frame_fps, 2, 0, 5, 5)

        # Apex Legends
        label12 = cria_label_jogo(self.frame_fps, "Apex Legends", self.images[11], 0, 1, 5, 5,"Apex Legends")
        self.criar_button_favoritos(self.frame_fps,"Apex Legends", 1, 1)
        button_download12 = self.cria_button_download(self.frame_fps, 2, 1, 5, 5)

        # DayZ
        label13 = cria_label_jogo(self.frame_fps, "DayZ", self.images[12], 0, 2, 5, 5,"DayZ")
        self.criar_button_favoritos(self.frame_fps,"DayZ", 1, 2)
        button_download13 = self.cria_button_download(self.frame_fps, 2, 2, 5, 5)

        # Team Fortress 2
        label14 = cria_label_jogo(self.frame_fps, "Team Fortress 2", self.images[13], 0, 3, 5, 5,"Team Fortress 2")
        self.criar_button_favoritos(self.frame_fps,"Team Fortress 2", 1, 3)
        button_download14 = self.cria_button_download(self.frame_fps, 2, 3, 5, 5)

        # PUBG
        label15 = cria_label_jogo(self.frame_fps, "PUBG", self.images[14], 0, 4, 5, 5,"PUBG")
        self.criar_button_favoritos(self.frame_fps,"PUBG", 1, 4)
        button_download15 = self.cria_button_download(self.frame_fps, 2, 4, 5, 5)

    def criar_button_favoritos(self,parent_frame, jogo, row, column):
        button = tk.Button(parent_frame, text="Favoritar",font=("Arial",9), background="#cdcfb7", command=lambda:[toca_som(),self.adicionar_favorito(jogo)])
        button.grid(row=row, column=column, padx=5, pady=5)
        button.bind("<Enter>", lambda e: entrada_do_mouse(e, button))
        button.bind("<Leave>", lambda e: saida_do_mouse(e, button))
    
    def adicionar_favorito(self, jogo):
        if not self.usuario_logado:
            mensagem_som.play()
            messagebox.showwarning("Erro", "Você precisa realizar o login primeiro.")
            return
        
        if self.usuario_model.adicionar_favorito(self.usuario_logado, jogo):
            mensagem_som.play()
            messagebox.showinfo("Favorito", f"{jogo} adicionado aos favoritos.")
            self.atualizar_favoritos()
        else:
            mensagem_som.play()
            messagebox.showinfo("Favorito", "O jogo já está na lista de favoritos.")
    def abrir_janela_favoritos(self):
        if hasattr(self, 'favorito_window') and self.info_window and self.info_window.winfo_exists():
            self.info_window.destroy
        if not self.usuario_logado:
            mensagem_som.play()
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

        self.frame_favorito = tk.Label(self.favorito_window, image=self.images[15])
        self.frame_favorito.pack(fill="both", expand=True)

        favorito_label = tk.Label(self.frame_favorito, text="Meus Favoritos", font=("Arial", 12), background="#cdcfb7")
        favorito_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="n")

        self.frame_lista_botao = tk.Label(self.frame_favorito, image=self.images[15])
        self.frame_lista_botao.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.listbox_favoritos = tk.Listbox(self.frame_lista_botao, background="#cdcfb7", selectmode=tk.SINGLE)
        self.listbox_favoritos.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.botao_remover_favorito = tk.Button(self.frame_lista_botao, text="Remover Favorito", command=self.remover_favorito)
        self.botao_remover_favorito.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="n")

        self.frame_favorito.grid_rowconfigure(1, weight=1)
        self.frame_favorito.grid_columnconfigure(0, weight=1)
        self.frame_lista_botao.grid_rowconfigure(0, weight=1)
        self.frame_lista_botao.grid_columnconfigure(0, weight=1)

        self.atualizar_favoritos()

        self.favorito_window.protocol("WM_DELETE_WINDOW", self.favorito_window.destroy)

    
    def atualizar_favoritos(self):
        if hasattr(self, 'favorito_window') and self.favorito_window and self.favorito_window.winfo_exists():
            if hasattr(self, 'listbox_favoritos') and self.listbox_favoritos.winfo_exists():
                self.listbox_favoritos.delete(0, tk.END)
                favoritos = self.usuario_model.obter_favoritos(self.usuario_logado)
                for fav in favoritos:
                    self.listbox_favoritos.insert(tk.END, fav)

    def abrir_janela_login(self):
        if self.usuario_logado:
            mensagem_som.play()
            messagebox.showinfo("Já Logado", "O Login já foi realizado.")
            return

        if self.login_window is None or not self.login_window.winfo_exists():
            self.login_window = tk.Toplevel(self.root)
            self.login_window.title("Login")
            self.login_window.geometry("320x200")
            self.login_window.resizable(False, False)

            self.frame_login = tk.Label(self.login_window, image=self.images[15])
            self.frame_login.pack(fill="both", expand=True)

            login_titulo = tk.Label(self.frame_login, text="Login", font=("Arial Black", 12), background="#cdcfb7")
            login_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 20), sticky="n")

            login_titulo.bind("<Enter>", lambda e: entrada_do_mouse(e, login_titulo))
            login_titulo.bind("<Leave>", lambda e: saida_do_mouse(e, login_titulo))

            label_nome = tk.Label(self.frame_login, text="Nome de Usuário:", font=("Arial Black", 8), background="#cdcfb7")
            label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="e")

            label_nome.bind("<Enter>", lambda e: entrada_do_mouse(e, label_nome))
            label_nome.bind("<Leave>", lambda e: saida_do_mouse(e, label_nome))

            entry_nome = tk.Entry(self.frame_login)
            entry_nome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

            label_senha = tk.Label(self.frame_login, text="Senha:", font=("Arial Black", 8), background="#cdcfb7")
            label_senha.grid(row=2, column=0, padx=10, pady=10, sticky="e")

            label_senha.bind("<Enter>", lambda e: entrada_do_mouse(e, label_senha))
            label_senha.bind("<Leave>", lambda e: saida_do_mouse(e, label_senha))

            self.entry_senha = tk.Entry(self.frame_login, show="•")
            self.entry_senha.grid(row=2, column=1, padx=10, pady=10, sticky="w")

            self.botao_mostra_senha = tk.Button(self.frame_login, image=self.images[16], command= self.esconde_senha)
            self.botao_mostra_senha.grid(row=2, column=2, padx=5, pady=10, sticky="w")



            def login():
                usuario = entry_nome.get()
                senha = self.entry_senha.get()
                data_de_nascimento = self.usuario_model.obter_data_nascimento(usuario)
                if self.usuario_model.validar_usuario(usuario, senha):
                    self.usuario_logado = usuario
                    if self.login_window:
                        self.login_window.destroy()
                        self.login_window = None
                    mensagem_som.play()
                    messagebox.showinfo("Login", f"Bem-vindo, {usuario}!")
                    self.menu_usuario.delete(0, tk.END)
                    self.menu_usuario.add_command(label=f"Usuário: {usuario}", state=tk.DISABLED)
                    self.menu_usuario.add_command(label=f"Data de Nascimento: {data_de_nascimento}", state=tk.DISABLED)
                    self.menu_usuario.add_command(label="Sair", command=self.sair_usuario)
                elif usuario == '' or senha == '':
                    mensagem_som.play()
                    messagebox.showwarning("Aviso", "Preencha todos os campos!")
                else:
                    mensagem_som.play()
                    messagebox.showerror("Login", "Usuário ou senha incorretos.")

            login_button = criar_button(self.frame_login,"Entrar",3,0,login)

            cadastro_button = criar_button(self.frame_login,"Cadastrar",3,1,self.abrir_janela_cadastro)
        
            self.login_window.protocol("WM_DELETE_WINDOW", self.login_window.destroy)

        else:
            self.login_window.lift()

    def abrir_janela_cadastro(self):
        # Fechar a janela de login se estiver aberta
        if self.login_window:
            self.login_window.destroy()
            self.login_window = None  # Opcional: limpar a referência à janela de login

        # Verificar se a janela de cadastro já está aberta
        if not self.cadastro_window or not tk.Toplevel.winfo_exists(self.cadastro_window):
            self.cadastro_window = tk.Toplevel(self.root)
            self.cadastro_window.title("Cadastro")
            self.cadastro_window.geometry("300x200")  # Ajustado para acomodar o novo layout
            self.cadastro_window.resizable(False, False)

            frame_cadastro = tk.Label(self.cadastro_window, image=self.images[15])  # Alterado de Label para Frame para melhor controle
            frame_cadastro.pack(fill='both', expand=True)

            for i in range(5):  # Ajustado para suportar uma linha extra
                frame_cadastro.grid_rowconfigure(i, weight=0)

            for i in range(2):
                frame_cadastro.grid_columnconfigure(i, weight=1)

            cadastro_titulo = cria_label_titulo(frame_cadastro, "Cadastro", 0, 0, 2)

            label_novo_nome = cria_label(frame_cadastro, "Novo usuário:", 1, 0, 10, 5, "w")

            self.entrada_usuario_cadastro = tk.Entry(frame_cadastro, width=20)  # Ajusta a largura da entrada
            self.entrada_usuario_cadastro.grid(row=1, column=1, padx=5, pady=5, sticky="e")

            label_nova_senha = cria_label(frame_cadastro, "Nova senha:", 2, 0, 10, 5, "w")
            self.entrada_senha_cadastro = tk.Entry(frame_cadastro, width=20)  # Ajusta a largura da entrada
            self.entrada_senha_cadastro.grid(row=2, column=1, padx=5, pady=5, sticky="e")

            label_aniversario = cria_label(frame_cadastro, "Sua data de nascimento:", 3, 0, 10, 5, "w")
            self.entrada_aniversario = DateEntry(frame_cadastro, width=10, background='darkblue', foreground='white', borderwidth=2)
            self.entrada_aniversario.grid(row=3, column=1, padx=5, pady=5, sticky="e")

            button_cadastro = criar_button(frame_cadastro, "Cadastrar", 4, 0, self.cadastrar_usuario)

        else:
            self.cadastro_window.lift()

        self.cadastro_window.protocol("WM_DELETE_WINDOW", self.cadastro_window.destroy)



    def cadastrar_usuario(self):
        usuario = self.entrada_usuario_cadastro.get()
        senha = self.entrada_senha_cadastro.get()
        data_de_nascimento = self.entrada_aniversario.get()

        if not usuario or not senha or not data_de_nascimento:
            mensagem_som.play()
            messagebox.showwarning("Erro", "Os campos não foram preenchidos corretamente.")
            return

        if self.usuario_model.criar_usuario(usuario, senha,data_de_nascimento):
            mensagem_som.play()
            messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
            self.cadastro_window.destroy
        else:
            mensagem_som.play()
            messagebox.showerror("Erro", "Não foi possível realizar o cadastro. Usuário pode já existir.")

    def remover_favorito(self):
        if not self.usuario_logado:
            mensagem_som.play()
            messagebox.showwarning("Erro", "Você precisa realizar o login primeiro.")
            return

        selecionado = self.listbox_favoritos.curselection()
        if not selecionado:
            mensagem_som.play()
            messagebox.showwarning("Erro", "Você não tem nenhum jogo para remover.")
            return

        jogo = self.listbox_favoritos.get(selecionado)
        if self.usuario_model.remover_favorito(self.usuario_logado, jogo):
            mensagem_som.play()
            messagebox.showinfo("Remover Favorito", f"{jogo} removido dos favoritos.")
            self.atualizar_favoritos()
        else:
            mensagem_som.play()
            messagebox.showerror("Erro", "Erro ao remover o jogo dos favoritos.")

    def cria_button_download(self, parent_frame, row, column, padx, pady):

            button = tk.Button(parent_frame, text="Baixar", background="#cdcfb7",font=("Arial", 9), command=lambda:[toca_som(), self.iniciar_download(button)])
            button.grid(row=row, column=column, padx=padx, pady=pady)
            button.bind("<Enter>", lambda e: entrada_do_mouse(e, button))
            button.bind("<Leave>", lambda e: saida_do_mouse(e, button))
            return button

    def iniciar_download(self, button):
        if self.usuario_logado:
            button.config(text="Baixando...", state="disabled")

            button.after(3000, lambda: self.download_concluido(button))
        else:
            mensagem_som.play()
            messagebox.showwarning("Erro", "Você precisa fazer o Login primeiro.")

    def download_concluido(self, button):
        mensagem_som.play()
        messagebox.showinfo("Informação", "O download foi concluído.")
        button.config(text="Download Completo", state="normal")
        button.config(command=lambda: self.mensagem_download_completo(button))

    def mensagem_download_completo(self, button):
        mensagem_som.play()
        messagebox.showinfo("Informação", "O download já foi feito.")

    def login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        if self.usuario_model.validar_usuario(usuario, senha):
            mensagem_som.play()
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.usuario_logado = usuario
            self.fechar_janela_login()
        else:
            mensagem_som.play()
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def esta_logado(self):
        return self.usuario_logado is not None

    def fechar_janela_login(self):
        if self.login_window:
            self.login_window.destroy
            self.login_window = None
            
    def tela_cheia(self, event=None):
        self.root.geometry("720x850")
        # Esconde as barras de rolagem em tela cheia
        self.scroll_x.grid_forget()
        self.scroll_y.grid_forget()

    def desativ_tela_cheia(self, event=None):
        self.root.geometry("700x700")
        self.scroll_x = tk.Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_y = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.grid(row=1, column=0, sticky="ew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")


        
    def esconde_senha(self):
        if self.entry_senha.cget('show') == '•':
            self.entry_senha.config(show='')
            self.botao_mostra_senha.config(image=self.images[17])
        else:
            self.entry_senha.config(show='•')
            self.botao_mostra_senha.config(image=self.images[16], command=self.esconde_senha)



    def fechar_app(self):
        mensagem_som.play()
        resposta = messagebox.askyesno("Confirmar Saída", "Quer realmente sair?")
        if resposta:
            self.usuario_model.fechar_conexao()
            self.root.destroy()

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Inicial")
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        self.images = load_images()

        self.frame_inicio = tk.Frame(self.root, bg="#000042")
        self.frame_inicio.pack(fill=tk.BOTH, expand=True)

        self.canvas_inicio = tk.Label(self.frame_inicio, image=self.images[18])
        self.canvas_inicio.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.canvas_inicio.grid_rowconfigure(0, weight=1)
        self.canvas_inicio.grid_rowconfigure(1, weight=1)
        self.canvas_inicio.grid_rowconfigure(2, weight=1)
        self.canvas_inicio.grid_rowconfigure(3, weight=1)
        self.canvas_inicio.grid_columnconfigure(0, weight=1)

        # Adicionando widgets ao frame usando grid
        self.label_inicio = tk.Label(self.canvas_inicio, text="Bem-vindo ao Aplicativo de Jogos!",background="#000042",foreground="white",font=("Arial Black",20))
        self.label_inicio.grid(row=0, column=0, pady=20, padx=10)
        self.label_inicio2 = tk.Label(self.canvas_inicio, text="Aperte iniciar para ir para a tela principal!",background="#000042",foreground="white", font=("Arial Black",15))
        self.label_inicio2.grid(row=1, column=0, pady=20, padx=10)
        self.button_start = tk.Button(self.canvas_inicio, text="Iniciar",background="#000042",foreground="white", font=("Arial Black",20), command=self.abrir_app)
        self.button_start.grid(row=2, column=0, pady=10)

        self.label_inicio.bind("<Enter>", lambda e: entrada_do_mouse_inicio(e, self.label_inicio))
        self.label_inicio.bind("<Leave>", lambda e: saida_do_mouse_inicio(e, self.label_inicio))
        self.label_inicio2.bind("<Enter>", lambda e: entrada_do_mouse_inicio(e, self.label_inicio2))
        self.label_inicio2.bind("<Leave>", lambda e: saida_do_mouse_inicio(e, self.label_inicio2))
        self.button_start.bind("<Enter>", lambda e: entrada_do_mouse_inicio(e, self.button_start))
        self.button_start.bind("<Leave>", lambda e: saida_do_mouse_inicio(e, self.button_start))

    def abrir_app(self):
        self.root.destroy()
        root = tk.Tk()
        app = App(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()
