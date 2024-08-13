import tkinter as tk
from tkinter import messagebox, ttk
from model.user import User




def adicionar_opcao(menu:tk.Menu, label, font_family, font_size,state_op, font_style="normal"):
    menu.menu_configuracoes.add_command(
        label=label,
        command=menu.exemplo_comando,
        font=(font_family, font_size, font_style),
        state = state_op
    )

def atualizar_opcao(menu:tk.Menu,usuario:User):
    # Limpar todas as opções e re-adicionar com uma atualização
    menu.menu_configuracoes.delete(0, tk.END)  # Remove todas as opções
    
    if(usuario.nome.count>0):
         menu.adicionar_opcao(usuario.nome, "Arial", 12,tk.NORMAL)
    # Re-adiciona as opções com a atualização desejada
    else:
        menu.adicionar_opcao("Usuário: Não Logado", "Arial", 12,tk.DISABLED)

def verificacao_login(usuario:User):
    try:
        if(usuario.nome.count>0):
            return True
        else:
            return False
    except:
        return False