import mariadb
import sys

class UsuarioModel:
    def __init__(self, db_name='app_jogos', user='root', password='', host='localhost', port=3306):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db_name
            )
        except mariadb.Error as e:
            print(f"Erro de conexão ao MariaDB: {e}")
            sys.exit(1)
        
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) UNIQUE,
                senha VARCHAR(100)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS favoritos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario_nome VARCHAR(100),
                jogo_nome VARCHAR(100),
                FOREIGN KEY (usuario_nome) REFERENCES usuario(nome)
            )
        ''')
        self.conn.commit()

    def criar_usuario(self, nome, senha):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO usuario (nome, senha) VALUES (%s, %s)', 
                (nome, senha)
            )
            self.conn.commit()
            cursor.close()
            return True
        except mariadb.Error as e:
            print(f"Erro ao criar usuário: {e}")
            return False

    def validar_usuario(self, nome, senha):
        cursor = self.conn.cursor()
        cursor.execute('SELECT senha FROM usuario WHERE nome = %s', (nome,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            stored_password = user[0]
            return senha == stored_password
        return False

    def adicionar_favorito(self, usuario_nome, jogo_nome):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'SELECT * FROM favoritos WHERE usuario_nome = %s AND jogo_nome = %s', 
                (usuario_nome, jogo_nome)
            )
            if cursor.fetchone():
                cursor.close()
                return False

            cursor.execute(
                'INSERT INTO favoritos (usuario_nome, jogo_nome) VALUES (%s, %s)', 
                (usuario_nome, jogo_nome)
            )
            self.conn.commit()
            cursor.close()
            return True
        except mariadb.Error as e:
            print(f"Erro ao adicionar favorito: {e}")
            return False

    def obter_favoritos(self, usuario_nome):
        cursor = self.conn.cursor()
        cursor.execute(
            'SELECT jogo_nome FROM favoritos WHERE usuario_nome = %s', 
            (usuario_nome,)
        )
        favoritos = cursor.fetchall()
        cursor.close()
        return [fav[0] for fav in favoritos]
    
    def remover_favorito(self, usuario, jogo):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM favoritos WHERE usuario_nome = %s AND jogo_nome = %s", 
                (usuario, jogo)
            )
            self.conn.commit()
            rows_affected = cursor.rowcount
            cursor.close()
            return rows_affected > 0
        except mariadb.Error as e:
            print(f"Erro ao remover favorito: {e}")
            return False

    def fechar_conexao(self):
        self.conn.close()
