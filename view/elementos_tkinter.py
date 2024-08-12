import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from imagens.imagens import load_images
class Mensagens:
  @staticmethod
  def msgAtencao(msg):
    messagebox.showwarning('Atenção', msg)
    
  @staticmethod
  def msgInfo(msg):
    messagebox.showinfo('Informação', msg)
  
  @staticmethod
  def msgQuestao(msg):
    messagebox.askyesno('Questão', msg)
  
  @staticmethod
  def msgErro(msg):
    messagebox.showerror('Erro', msg)




def titulo(titulo, master,linha,  **args,):
  label = tk.Label(master, **args)
  label.grid(row=linha, column=0, sticky=tk.NSEW)

def entrada_do_mouse(event, item):
    event.widget.config(bg='#d9f4ff')
    item.config(foreground='#316f98')

def saida_do_mouse(event, item):
    event.widget.config(bg='#cdcfb7')
    item.config(foreground='black')
    
#label para textos etc.
def Labelcustomizada(master, **args):
  args.setdefault('bg', '#cdcfb7')
  args.setdefault('font', ('Arial', 10))
  return tk.Label(master, **args)

#label dedicada a titulos
def LabelcustomizadaTitulo(master, **args):
  args.setdefault('bg', '#cdcfb7')
  args.setdefault('font', ('Arial Black', 12, 'bold'))
  return tk.Label(master, **args)


#label dedicada a titulos
def Buttoncustomizado(master, **args):
  args.setdefault('font', ('Arial', 9))
  return tk.Button(master, **args)

def CheckButtoncustomizado(master, **args):
  args.setdefault('font', ('Arial', 9))
  return tk.Checkbutton(master, **args)

def Framecustomizado(master, **args):
  args.setdefault('bg', '#dceeb1')
  return tk.Label(master,  **args)

def Textcustomizado(master, **args):
  args.setdefault('font', ('Arial', 9))
  args.setdefault('width', '12')
  args.setdefault('height', '0')
  return tk.Text(master, borderwidth=1, relief=tk.SOLID,**args)


def Entrycustomizado(master, **args):
  return tk.Entry(master, borderwidth=1, relief=tk.SOLID,**args)
                    
                    

