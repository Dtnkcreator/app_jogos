import tkinter as tk
import pygame
from tkinter import messagebox
from imagens.imagens import load_images

# Inicialize o pygame e o mixer
pygame.mixer.init()

# Carregue o som
click_som = pygame.mixer.Sound(r"C:\Users\182400280\Downloads\Python\database\SQLite\jogos\antigo\app_jogos\click.wav")

def toca_som():
    click_som.play()

def criar_button(parent_frame, text, row, column, command):
    # Use lambda para chamar `toca_som` e depois `command`
    button = tk.Button(parent_frame, text=text, background='#cdcfb7', command=lambda: [toca_som(), command()])
    button.grid(row=row, column=column, columnspan=2, padx=10, pady=(10, 20), sticky="n")
    button.bind("<Enter>", lambda e: entrada_do_mouse(e, button))
    button.bind("<Leave>", lambda e: saida_do_mouse(e, button))

info_jogo_window = None

def mostra_informacoes_jogo(jogo):
    global info_jogo_window
    
    # Se uma janela de informações já estiver aberta, feche-a
    if info_jogo_window is not None and info_jogo_window.winfo_exists():
        info_jogo_window.destroy()
    
    # Cria uma nova janela
    info_jogo_window = tk.Toplevel()
    info_jogo_window.title("Informações do Jogo")
    
    # Configura o layout da nova janela
    info_jogo_window.geometry("470x300")
    info_jogo_window.resizable(False,False)
    info_jogo_window.configure(bg="#f0f0f0")
    info_label_principal = tk.Label(info_jogo_window, background="#607848")
    info_label_principal.pack(expand="yes", fill="both")
    info_label = tk.Label(info_label_principal, text=f"{jogo}", font=("Arial Black", 16), background="#cdcfb7")
    info_label.grid(row=0, column=0, columnspan=2,  pady=(20, 10), padx=20, sticky="n")
    info_label.bind("<Enter>", lambda e: entrada_do_mouse(e, info_label))
    info_label.bind("<Leave>", lambda e: saida_do_mouse(e, info_label))

    detalhes_jogo = f"Detalhes do jogo {jogo}.\nEste é um jogo incrível com várias características fantásticas!"
    detalhes_label = tk.Label(info_label_principal, text=detalhes_jogo, font=("Arial", 12), bg="#789048", wraplength=550, justify="center")
    detalhes_label.grid(row=1, column=0, columnspan=2, pady=(0, 20), padx=20, sticky="n")

    # Adiciona um botão para fechar a janela, centralizado
    close_button = tk.Button(info_label_principal, text="Fechar", font=("Arial", 15), command=info_jogo_window.destroy, bg="#cdcfb7")
    close_button.grid(row=2, column=0, columnspan=2, pady=(10, 20), padx=20, sticky="n")

    close_button.bind("<Enter>", lambda e: entrada_do_mouse(e, close_button))
    close_button.bind("<Leave>", lambda e: saida_do_mouse(e, close_button))

def cria_label_jogo(parent, text, image, row, column, padx, pady, jogo):
    # Cria um botão ao invés de um label para permitir a interação
    label = tk.Button(parent, text=text, image=image, compound="top", font=("Arial", 8), background="#cdcfb7", command=lambda: mostra_informacoes_jogo(jogo))
    label.grid(row=row, column=column, padx=padx, pady=pady)
    label.bind("<Enter>", lambda e: entrada_do_mouse(e, label))
    label.bind("<Leave>", lambda e: saida_do_mouse(e, label))

def cria_label_subtitulo(parent, text, row, column, padx, pady):
    label_subtitulo = tk.Label(parent, text=text, compound="top", background="#cdcfb7", font=("Arial Black", 9))
    label_subtitulo.grid(row=row, column=column, padx=padx, pady=pady, columnspan=5, sticky="nw")
    label_subtitulo.bind("<Enter>", lambda e: entrada_do_mouse(e, label_subtitulo))
    label_subtitulo.bind("<Leave>", lambda e: saida_do_mouse(e, label_subtitulo))

def cria_label(parent, text, row, column, padx, pady, sticky):
    label_subtitulo = tk.Label(parent, text=text, compound="top", background="#cdcfb7", font=("Arial Black", 8))
    label_subtitulo.grid(row=row, column=column, padx=padx, pady=pady, columnspan=5, sticky=sticky)
    label_subtitulo.bind("<Enter>", lambda e: entrada_do_mouse(e, label_subtitulo))
    label_subtitulo.bind("<Leave>", lambda e: saida_do_mouse(e, label_subtitulo))

def cria_label_titulo(parent, text, row, column, columnspan):
    label_titulo = tk.Label(parent, text=text, font=("Arial Black", 16), background="#cdcfb7")
    label_titulo.grid(row=row, column=column, columnspan=columnspan, pady=(10, 5), sticky="n")
    label_titulo.bind("<Enter>", lambda e: entrada_do_mouse(e, label_titulo))
    label_titulo.bind("<Leave>", lambda e: saida_do_mouse(e, label_titulo))

def cria_frame(parent, background, columnspan, row, column, padx, pady):
    frame = tk.Frame(parent, background=background)
    frame.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky="nw")
    frame.bind("<Enter>", entrada_do_mouse)
    frame.bind("<Leave>", saida_do_mouse)

def entrada_do_mouse(event, item):
    event.widget.config(bg='#d9f4ff')
    item.config(foreground='#316f98')

def saida_do_mouse(event, item):
    event.widget.config(bg='#cdcfb7')
    item.config(foreground='black')

def entrada_do_mouse_inicio(event, item):
    event.widget.config(bg='#d9f4ff')
    item.config(foreground='#000042')

def saida_do_mouse_inicio(event, item):
    event.widget.config(bg='#000042')
    item.config(foreground='white')
