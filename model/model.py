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
                senha VARCHAR(100),
                data_de_nascimento DATE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS favoritos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_jogo VARCHAR(255) NOT NULL,
                id_usuario INT NOT NULL,
                favoritado BOOLEAN NOT NULL DEFAULT FALSE,
                FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
            )
        ''')
        self.conn.commit()

    def criar_usuario(self, nome, senha, data_de_nascimento):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO usuario (nome, senha, data_de_nascimento) VALUES (%s, %s, %s)', 
                (nome, senha, data_de_nascimento)
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
    
    def obter_data_nascimento(self, nome):
        cursor = self.conn.cursor()
        cursor.execute('SELECT data_de_nascimento FROM usuario WHERE nome = %s', (nome,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else None


    def adicionar_favorito(self, usuario_nome, jogo_nome):
        try:
            cursor = self.conn.cursor()
            
            # Obter o ID do usuário
            cursor.execute('SELECT id FROM usuario WHERE nome = %s', (usuario_nome,))
            user = cursor.fetchone()
            if not user:
                cursor.close()
                return False
            
            id_usuario = user[0]

            # Verificar se o jogo já está favoritado pelo usuário
            cursor.execute(
                'SELECT * FROM favoritos WHERE id_usuario = %s AND nome_jogo = %s',
                (id_usuario, jogo_nome)
            )
            if cursor.fetchone():
                cursor.close()
                return False

            # Adicionar o jogo aos favoritos
            cursor.execute(
                'INSERT INTO favoritos (nome_jogo, id_usuario, favoritado) VALUES (%s, %s, TRUE)',
                (jogo_nome, id_usuario)
            )
            self.conn.commit()
            cursor.close()
            return True
        except mariadb.Error as e:
            print(f"Erro ao adicionar favorito: {e}")
            return False

    def obter_favoritos(self, usuario_nome):
        cursor = self.conn.cursor()
        
        # Obter o ID do usuário
        cursor.execute('SELECT id FROM usuario WHERE nome = %s', (usuario_nome,))
        user = cursor.fetchone()
        if not user:
            cursor.close()
            return []

        id_usuario = user[0]

        # Obter todos os jogos favoritados pelo usuário
        cursor.execute(
            'SELECT nome_jogo FROM favoritos WHERE id_usuario = %s AND favoritado = TRUE',
            (id_usuario,)
        )
        favoritos = cursor.fetchall()
        cursor.close()
        return [fav[0] for fav in favoritos]
    
    def remover_favorito(self, usuario_nome, jogo_nome):
        try:
            cursor = self.conn.cursor()
            
            # Obter o ID do usuário
            cursor.execute('SELECT id FROM usuario WHERE nome = %s', (usuario_nome,))
            resultado = cursor.fetchone()
            if not resultado:
                cursor.close()
                return False

            id_usuario = resultado[0]

            # Remover o jogo dos favoritos
            cursor.execute(
                "DELETE FROM favoritos WHERE id_usuario = %s AND nome_jogo = %s",
                (id_usuario, jogo_nome)
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
