import tkinter as tk
from tkinter import messagebox
# Funções de botão
def criar_button(parent_frame,text, row, column,command):
        button = tk.Button(parent_frame, text=text,background="#cdcfb7", command=command)
        button.grid(row=row, column=column, columnspan=2, padx=10, pady=(10, 20), sticky="n")
        button.bind("<Enter>", entrada_do_mouse)
        button.bind("<Leave>", saida_do_mouse)

def cria_label_jogo(parent, text, image, row, column, padx, pady):
    # Define a cor de fundo igual ao botão de download
    label = tk.Button(parent, text=text, image=image, compound="top", font=("Arial", 8), background="#cdcfb7")
    label.grid(row=row, column=column, padx=padx, pady=pady)
    label.bind("<Enter>", entrada_do_mouse)
    label.bind("<Leave>", saida_do_mouse)

def cria_label_subtitulo(parent, text, row, column, padx, pady):
    # Define a cor de fundo igual ao botão de download
    label_subtitulo = tk.Label(parent, text=text, compound="top", background="#cdcfb7", font=("Arial Black", 9))
    label_subtitulo.grid(row=row, column=column, padx=padx, pady=pady, columnspan=5, sticky="nw")
    label_subtitulo.bind("<Enter>", entrada_do_mouse)
    label_subtitulo.bind("<Leave>", saida_do_mouse)

def cria_label(parent, text, row, column, padx, pady,sticky):
    # Define a cor de fundo igual ao botão de download
    label_subtitulo = tk.Label(parent, text=text, compound="top", background="#cdcfb7", font=("Arial Black", 9))
    label_subtitulo.grid(row=row, column=column, padx=padx, pady=pady, columnspan=5, sticky=sticky)
    label_subtitulo.bind("<Enter>", entrada_do_mouse)
    label_subtitulo.bind("<Leave>", saida_do_mouse)
def cria_label_titulo(parent, text, row, column, columnspan):
    # Define a cor de fundo igual ao botão de download
    label_titulo = tk.Label(parent, text=text, font=("Arial Black", 16), background="#cdcfb7")
    label_titulo.grid(row=row, column=column, columnspan=columnspan, pady=(10, 5), sticky="n")
    label_titulo.bind("<Enter>", entrada_do_mouse)
    label_titulo.bind("<Leave>", saida_do_mouse)

def cria_frame(parent, background, columnspan, row, column, padx, pady):
    frame = tk.Frame(parent, background=background)
    frame.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky="nw")
    frame.bind("<Enter>", entrada_do_mouse)
    frame.bind("<Leave>", saida_do_mouse)

# Funções para mudança de cor
def entrada_do_mouse(event):
    event.widget.config(bg='#d9f4ff')

def saida_do_mouse(event):
    event.widget.config(bg='#cdcfb7')
