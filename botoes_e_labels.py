import tkinter as tk

def criar_button(parent_frame,text, row, column,command):
        button = tk.Button(parent_frame, text=text,background='#cdcfb7', command=command)
        button.grid(row=row, column=column, columnspan=2, padx=10, pady=(10, 20), sticky="n")
        button.bind("<Enter>", lambda e: entrada_do_mouse(e, button))
        button.bind("<Leave>", lambda e: saida_do_mouse(e, button))

def cria_label_jogo(parent, text, image, row, column, padx, pady):
    label = tk.Button(parent, text=text, image=image, compound="top", font=("Arial", 8), background="#cdcfb7")
    label.grid(row=row, column=column, padx=padx, pady=pady)
    label.bind("<Enter>", lambda e: entrada_do_mouse(e, label))
    label.bind("<Leave>", lambda e: saida_do_mouse(e, label))

def cria_label_subtitulo(parent, text, row, column, padx, pady):
    label_subtitulo = tk.Label(parent, text=text, compound="top", background="#cdcfb7", font=("Arial Black", 9))
    label_subtitulo.grid(row=row, column=column, padx=padx, pady=pady, columnspan=5, sticky="nw")
    label_subtitulo.bind("<Enter>", lambda e: entrada_do_mouse(e, label_subtitulo))
    label_subtitulo.bind("<Leave>", lambda e: saida_do_mouse(e, label_subtitulo))

def cria_label(parent, text, row, column, padx, pady,sticky):
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
