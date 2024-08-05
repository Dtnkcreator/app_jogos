import tkinter as tk
from view.elementos_tkinter import Buttoncustomizado, Labelcustomizada, LabelcustomizadaTitulo, Mensagens, Textcustomizado
from view.sistema_login import Registro, BaseCadastro, Login
from model.modelo import SalvarUsuario, CarregarUsuario
from datetime import datetime

class Controle:
    def __init__(self, root):
        self.root= root
        self.contar_click = 0
       
  
    #só iremos chamar se o usuario se registrar pelo login
    def abrir_janela_registro(self):
           self.root.withdraw()
           self.window_reg = tk.Toplevel(self.root)
           self.registro = Registro(self.window_reg)
           self.config_button_enviar()
           self.config_check()
           self.config_eventos()
    

    def abrir_janela_login(self):
        self.root.withdraw()
        self.window_log = tk.Toplevel(self.root)
        self.login = Login(self.window_log)
        
        def check_user_janela_login():
            #usuario insere o nome e a senha
            self.nome_procurado = self.login.nome_get()
            self.senha_procurado = self.login.senha_get()
            self.carrega_user = CarregarUsuario(self.nome_procurado, self.senha_procurado)

        self.login.button_login.config(command=check_user_janela_login)
        self.login.button_reg.config(command=self.abrir_janela_registro)
        

         
    
    
    def config_check(self):
        self.mostre_senha = tk.IntVar()
        self.registro.mostrar_senha.config(variable=self.mostre_senha,command=self.ocultar_senha)

    def config_button_enviar(self):
          self.registro.button_enviar.config(command=self.salvar_usuario)

    def ocultar_senha(self):
        #no contexto checkbutton quando marco a caixa o valor é igual a 1
        if self.mostre_senha.get()==1:
            self.registro.senha_entrada.config(show='')
            self.registro.mostrar_senha.config(text='Ocultar senha')
        else:
            self.registro.senha_entrada.config(show='*')
            self.registro.mostrar_senha.config(text='Mostrar senha')

       
    
    def config_eventos(self):
        self.registro.nome_entrada.bind('<KeyRelease>', self.dicas_nome)
        self.registro.senha_entrada.bind('<KeyRelease>', self.dicas_senha)
        self.registro.data_entrada.bind('<KeyRelease>', self.dicas_data)
       
    def dicas_nome(self, event):
        
        self.ler_nome = len(self.registro.nome_get())

        if self.ler_nome>=5 and self.ler_nome<=9:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário está no números de caracteres mínimo, pois tem {self.ler_nome} !',fg='green', wraplength=200)
            
        elif self.ler_nome==10:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário chegou ao número de caractere máximo, pois tem {self.ler_nome} !',fg='green', wraplength=200)
        
        elif self.ler_nome>=11:
            Mensagens.msgAtencao(f'Seu nome de usuário chegou número de caractere máximo, pois tem {self.ler_nome} !')
            self.registro.nome_entrada.delete(1.0, tk.END)
            self.registro.nome_dicas.config(text='Entrada resetada')
        
        else:
            self.registro.nome_dicas.config(text=f'Seu nome de usuário não chegou ao  número de caractere mínimo, pois tem {self.ler_nome} !',fg='red', wraplength=200)
            if self.ler_nome<=1:
                self.registro.nome_dicas.config(text=f'Seu nome de usuário é insuficente, pois tem {self.ler_nome}  caractere !',fg='red', wraplength=200)
        
    def dicas_senha(self, event):
            self.ler_senha = len(self.registro.senha_get())

            if self.ler_senha>=5 and self.ler_senha<=9:
                self.registro.senha_dicas.config(text=f'Sua senha de usuário está no números de caracteres mínimo, pois tem {self.ler_senha} !',fg='green', wraplength=200)
                
            elif self.ler_senha==10:
                self.registro.senha_dicas.config(text=f'Sua senha de usuário chegou ao número de caractere máximo, pois tem {self.ler_senha} !',fg='green', wraplength=200)
            
            elif self.ler_senha>=11:
                Mensagens.msgAtencao(f'Sua senha de usuário chegou número de caractere máximo, pois tem {self.ler_senha} !')
                self.registro.senha_entrada.delete(0, tk.END)
                self.registro.senha_dicas.config(text='Entrada resetada')
            
            else:
                self.registro.senha_dicas.config(text=f'Sua senha de usuário não chegou ao  número de caractere mínimo, pois tem {self.ler_senha} !',fg='red', wraplength=200)
                if self.ler_senha<=1:
                    self.registro.senha_dicas.config(text=f'Sua senha de usuário é insuficente, pois tem {self.ler_senha}  caractere !',fg='red', wraplength=200)

    def dicas_data(self, event):
        try:
            self.data_formatada = datetime.strptime(self.registro.data_get(), '%d-%m-%Y')
            self.data_padrao =  self.data_formatada.strftime('%d-%m-%Y')
            self.registro.data_dicas.config(text=f'Sua  data de nascimento ficou : {self.data_padrao}', fg='green')

        except ValueError:
            self.registro.data_dicas.config(text='Inválido', fg='red')
    
    def salvar_usuario(self):
        self.nome = self.registro.nome_get()
        self.senha = self.registro.senha_get()
        self.data = self.registro.data_get()

        def verificar_campo_vazio():
            nome_status = self.registro.nome_dicas
            senha_status = self.registro.senha_dicas
            data_status = self.registro.data_dicas

            
            if self.nome == '' and self.senha == '' and self.data == '':
                Mensagens.msgAtencao('Os três campos estão vazios, preencha por favor!')
            

            elif nome_status.cget('fg')=='red' and data_status.cget('fg')=='red' and senha_status.cget('fg')=='red':
                Mensagens.msgAtencao('Os três campos não seguem os requisitos ! Preencha por favor!')

            elif nome_status.cget('fg')!='red' and data_status.cget('fg')=='red' and senha_status.cget('fg')=='red':
                Mensagens.msgAtencao('Os campos data  e senha   não seguem os requisitos ! Preencha por favor!')
            
            elif nome_status.cget('fg')=='red' and data_status.cget('fg')!='red' and senha_status.cget('fg')=='red':
                Mensagens.msgAtencao('Os campos nome  e senha  não seguem os requisitos ! Preencha por favor!')
            
            elif nome_status.cget('fg')=='red' and data_status.cget('fg')=='red' and senha_status.cget('fg')!='red':
                Mensagens.msgAtencao('Os campos nome  e data  não seguem os requisitos ! Preencha por favor!')
            
            elif senha_status.cget('fg')=='red':
                Mensagens.msgAtencao('O campo senha não segue requisitos ! Preencha por favor!')
            
            elif nome_status.cget('fg')=='red':
                Mensagens.msgAtencao('O campo nome não segue requisitos ! Preencha por favor!')
            
            elif data_status.cget('fg')=='red':
                Mensagens.msgAtencao('O campo data não segue requisitos ! Preencha por favor!')
            
            elif self.nome != '' and self.senha == '' and self.data == '':
                Mensagens.msgAtencao('Os  campos data e senha estão vazios, preencha por favor!')
            
            elif self.nome == '' and self.senha != '' and self.data == '':
                Mensagens.msgAtencao('Os campos data e nome estão vazios, preencha por favor!')
            
            elif self.nome == '' and self.senha == '' and self.data != '':
                Mensagens.msgAtencao('Os  campos nome e senha estão vazios, preencha por favor!')

            elif self.nome == '':
                Mensagens.msgAtencao('O campo nome está vazio, preencha por favor!')
            elif self.senha == '':
                Mensagens.msgAtencao('O campo senha está vazio, preencha por favor!')
            elif self.data == '':
                Mensagens.msgAtencao('O campo data está vazio, preencha por favor!')
            
            elif  nome_status.cget('fg')=='red' and self.data == '' and self.senha == '' :
                Mensagens.msgAtencao('O campo nome não seguiu os requsitos e ademais, os campos data e senha estão vazios, preencha por favor!')
            else:
                self.contar_click+=1
                if self.contar_click>=2:
                    Mensagens.msgAtencao('Seu cadastro já foi enviado !')
                else:
                    self.registro.nome_entrada.config(state=tk.DISABLED)
                    self.registro.data_entrada.config(state=tk.DISABLED)
                    self.registro.senha_entrada.config(state=tk.DISABLED)
                    self.salva_user_no_banco = SalvarUsuario(self.nome, self.data_formatada, self.senha)

                    return self.abrir_janela_login()
        verificar_campo_vazio()

     
if __name__=='__main__':
    root = tk.Tk()
    Controle(root)
    root.mainloop()



        