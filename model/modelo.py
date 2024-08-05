import mysql.connector
from datetime import datetime
from view.elementos_tkinter import Mensagens

class SalvarUsuario:
    def __init__(self, nome_usuario: str, data_usuario: datetime, senha_usuario: str):
        self.nome_usuario = nome_usuario
        self.data_usuario = data_usuario
        self.senha_usuario = senha_usuario
        
        try:
            self.conexao = mysql.connector.connect(
                host="localhost",
                user="app",
                password="oi",
                database="app_jogos"
            )
            self.cursor = self.conexao.cursor()
            self.criar_tabela_dados_usuarios()
            self.inserir_usuario_nas_tabelas()

        except mysql.connector.Error as err:
            print(f"Erro de conexão: {err}")
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conexao:
                self.conexao.commit()
                self.conexao.close()

    def criar_tabela_dados_usuarios(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dados_usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_usuario VARCHAR(255) NOT NULL,
                data_de_nascimento DATE,
                senha_usuario VARCHAR(255) NOT NULL
            );
            """)
            print('Tabela criada com sucesso!')
        except mysql.connector.Error as err:
            print(f'Erro ao criar tabela: {err}')

    def inserir_usuario_nas_tabelas(self):
        try:
            # Verifica se um usuário existe com este nome ou não
            self.cursor.execute("SELECT * FROM dados_usuarios WHERE nome_usuario = %s OR data_de_nascimento = %s OR senha_usuario = %s;", 
                                (self.nome_usuario, self.data_usuario, self.senha_usuario,))
            usuarios_existentes = self.cursor.fetchall()

            for usuario in usuarios_existentes:
                if usuario[1] == self.nome_usuario and usuario[2] == self.data_usuario and usuario[3] == self.senha_usuario:
                    Mensagens.msgAtencao('Você já foi cadastrado!')
                    return
                
                elif usuario[1] == self.nome_usuario:
                    Mensagens.msgAtencao('Já existe um usuário com este nome! Mude para outro nome!')
                    return

                elif usuario[3] == self.senha_usuario:
                    Mensagens.msgAtencao('Já existe um usuário com esta senha! Mude para outra senha!')
                    return
                
                try:
                    # Inserir o usuário se ele não existir
                    self.cursor.execute("""
                    INSERT INTO dados_usuarios (nome_usuario, data_de_nascimento, senha_usuario)
                    VALUES (%s, %s, %s);
                    """, (self.nome_usuario, self.data_usuario, self.senha_usuario))
                    print('Usuario  inserido com sucesso na tabela !')
                    
                    print('Usuario inserido com sucesso na tabela !')
            
                    Mensagens.msgInfo('Seu cadastro foi realizado com sucesso!')
                except ValueError:
                    print('Usuario não foi inserido com sucesso na tabela !')
     
    
        except mysql.connector.Error as err:
            print(f'Erro ao inserir o usuário {self.nome_usuario}: {err}')
        
       

#classe dedica ao modulo login e verifica se o usuario existe ou não
class CarregarUsuario:
    def __init__(self, nome_procurado: str, senha_procurada: str):
        self.nome_procurado = nome_procurado
        self.senha_procurada = senha_procurada
        
        try:
            self.conexao = mysql.connector.connect(
                host="localhost",
                user="app",
                password="oi",
                database="app_jogos"
            )
            self.cursor = self.conexao.cursor()
            self.show_users()
        except mysql.connector.Error as err:
            print(f"Erro de conexão: {err}")
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conexao:
                self.conexao.close()

    

    def show_users(self):

        try:
            self.cursor.execute("SELECT * FROM dados_usuarios WHERE nome_usuario = %s;", (self.nome_procurado,))
            self.mostrar_usuarios = self.cursor.fetchall()
            self.dicio_pessoa = {}
            usuario_encontrado = False
            for usuario in self.mostrar_usuarios:
                self.dicio_pessoa[f'usuário {usuario[0]}'] = {
                    'ID': usuario[0],
                    'Nome': usuario[1],
                    'Data de nascimento': usuario[2],
                    'Senha': usuario[3]
                }
                if usuario[1] == self.nome_procurado:
                    if usuario[3] == self.senha_procurada:
                        Mensagens.msgInfo(f'{self.nome_procurado} encontrado !')
                    else:
                        Mensagens.msgAtencao(f'Usuário {self.nome_procurado} encontrado, mas a senha está errada!')
                    usuario_encontrado = True
                    break

            if not usuario_encontrado:
                Mensagens.msgAtencao(f'Não foi encontrado {self.nome_procurado}!')
                
        except mysql.connector.Error as err:
            print(f'Erro ao mostrar usuários: {err}')
