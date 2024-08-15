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
    info_jogo_window.geometry("600x330")
    info_jogo_window.resizable(False,False)
    info_jogo_window.configure(bg="#607848")
    info_label_principal = tk.Label(info_jogo_window, background="#607848")
    info_label_principal.pack(expand="yes", fill="both")
    info_label = tk.Label(info_label_principal, text=f"{jogo}", font=("Arial Black", 16), background="#cdcfb7")
    info_label.grid(row=0, column=0, columnspan=2,  pady=(20, 10), padx=20, sticky="n")
    info_label.bind("<Enter>", lambda e: entrada_do_mouse(e, info_label))
    info_label.bind("<Leave>", lambda e: saida_do_mouse(e, info_label))

    if jogo=="Super Mario World":
        detalhes_jogo = f"Super Mario World também conhecido como Super Mario Bros. 4 é um jogo de plataforma para o Super Nintendo Entertainment System. Foi lançado em 1990 e foi um dos jogos mais populares para o SNES (devido ao fato de ser uma versão livre junto com o sistema). Um remake do jogo foi lançado intitulado Super Mario Advance 2: Super Mario World, e também incluiu Mario Bros. Mario montou e utilizou Yoshi pela primeira vez neste jogo."
    if jogo=="Kingdom Rush":
        detalhes_jogo = f"Kingdom Rush é um jogo de fantasia de defesa de torre criado pela Ironhide Game Studio e patrocinado pela Armor Games. Lançado pela primeira vez em 28 de julho de 2011, tornou-se imensamente popular e acumulou um total de mais de 70 milhões de jogos apenas na Armor Games."
    if jogo=="CS:GO":
        detalhes_jogo = f"Counter-Strike: Global Offensive (CS:GO) é um videogame de tiro em primeira pessoa que faz parte da série Counter-Strike. Foi anunciado ao público em 12 de agosto de 2011 e é desenvolvido pela Valve Corporation e seu parceiro, Hidden Path Entertainment. O jogo foi lançado posteriormente em 21 de agosto de 2012 para Playstation 3, Xbox 360, Microsoft Windows, macOS e posteriormente Linux como um título para download."
    if jogo=="Bloons TD 6":
        detalhes_jogo = f"Bloons TD 6 é desenvolvido e publicado pela Ninja Kiwi, o jogo foi lançado em 13 de junho de 2018 para Android e iOS, e posteriormente levado para Steam, Windows e Macintosh, e para consoles. Assim como os outros jogos de defesa de torre da série BTD, o objetivo do Bloons TD 6 é evitar que balões inimigos, chamados de Bloons, atravessem uma pista e ceifem vidas, o que é cumprido pelo jogador colocando uma combinação de macaco- torres baseadas para estourar os Bloons antes que escapem. Bloons TD 6 apresenta gráficos 3D, mecânica de linha de visão, tipos adicionais de Bloons, Heróis, 5º atualizações de nível, um terceiro caminho de atualização, cosméticos expandidos e muito mais."
    if jogo=="Metal Slug 3":
        detalhes_jogo = f"Metal Slug 3 (メタルスラッグ 3- Metaru Suraggu Surī) é um videogame run and gun para o console/plataforma arcade Neo-Geo criado pela SNK que foi lançado em 2000 e é a sequência de Metal Slug 2. Sendo o último Metal Slug na série em que a SNK estava trabalhando até a falência, ela recebeu muitos recursos, melhorias e melhorias. A música do jogo foi desenvolvida pela Noise Factory. O jogo foi portado para PlayStation 2 e Xbox. O jogo também foi relançado para Wii, PSP, PS2 e PS4 (PS2 Classic Download) como parte da coleção Metal Slug Anthology."
    if jogo=="Pacman":
        detalhes_jogo = f"Pac-Man (conhecido em japonês com o nome de Puckman ou パックマン) é um jogo eletrônico criado por Tōru Iwatani para a empresa Namco, e sendo distribuído para o mercado americano pela Midway Games. Produzido originalmente para Arcade no início dos anos 1980, tornou-se um dos jogos mais jogados e populares no momento, tendo versões modernas para diversos consoles e continuações. A mecânica do jogo é simples: o jogador era uma cabeça redonda com uma boca que se abre e fecha, posicionado em um labirinto simples repleto de pastilhas e 4 fantasmas que o perseguiam. O objetivo era comer todas as pastilhas sem ser alcançado pelos fantasmas, em ritmo progressivo de dificuldade."
    if jogo=="Donkey Kong Country":
        detalhes_jogo = f"Donkey Kong Country (スーパードンキーコング, Sūpā Donkī Kongu no Japão) é um jogo de plataforma desenvolvido pela Rareware e foi lançado pela primeira vez para o Super Family Computer/Super Nintendo Entertainment System pela Nintendo em 1994. O popular jogo é creditado por seu spin- a estreia do primeiro antagonista de jogo da Nintendo, Donkey Kong, uma década antes do lançamento do jogo, bem como o início de uma nova franquia inteiramente baseada em novos personagens e jogabilidade. Embora a Rare tenha feito alguns jogos populares no passado, como Battletoads para Famicom/NES, Donkey Kong Country é creditado por torná-los bem conhecidos na indústria."
    if jogo=="Tetris":
        detalhes_jogo = f"Tetris (em russo: Тетрис) é um jogo eletrônico de quebra-cabeça criado por Alexey Pajitnov, lançado em 1985. Foi publicado por várias empresas para diversas plataformas, mais proeminentemente durante uma disputa sobre a apropriação dos direitos no final da década de 1980. Após um período significativo de publicação pela Nintendo, em 1996 os direitos foram revertidos para Pajitnov, que co-fundou a Tetris Company com Henk Rogers para gerenciamento do licenciamento da série."
    if jogo=="Contra":
        detalhes_jogo = f"Contra (魂斗羅 Kontora?) é uma série de jogos eletrônicos de plataforma (Shoot 'em up) criados pela Konami em 1987. Enquanto que os primeiros jogos da série foi lançada para arcade, a série ganhou maior popularidade devido aos lançamentos de seus jogos para consoles, especialmente os títulos criados para o Nintendo Entertainment System (NES). As fases são variadas, alternando scroll horizontal e vertical e até fases em pseudo 3D. A principio parece uma guerra normal, mas nas fases mais adiantadas o cenário vai se tornando bizarro e alienígena."
    if jogo=="Sonic":
        detalhes_jogo = f"Sonic the Hedgehog 3 é um jogo de plataforma de 1994 desenvolvido e publicado pela Sega para o Sega Genesis. Como nos jogos anteriores do Sonic, os jogadores atravessam níveis de rolagem lateral enquanto coletam anéis e derrotam inimigos. Eles controlam Sonic e Tails, que tentam recuperar as Esmeraldas do Caos para impedir o Doutor Robotnik de relançar sua estação espacial, o Death Egg, após ele pousar em uma misteriosa ilha flutuante. Sonic 3 apresenta Knuckles the Echidna, o guardião da ilha, que prepara armadilhas para Sonic e Tails."
    if jogo==f"ARK: Survival Ascended":
        detalhes_jogo = f"Ark: Survival Ascended é um videogame de sobrevivência de ação e aventura desenvolvido pelo Studio Wildcard. É uma remasterização do jogo Ark: Survival Evolved de 2017. Foi lançado em acesso antecipado para Windows em 25 de outubro de 2023, Xbox Series X/S em 21 de novembro de 2023 e PlayStation 5 em 30 de novembro de 2023."    
    if jogo=="Apex Legends":
        detalhes_jogo = f"Apex Legends é um jogo eletrônico free-to-play do gênero battle royale desenvolvido pela Respawn Entertainment e publicado pela Electronic Arts. Foi lançado para Microsoft Windows, PlayStation 4 e Xbox One em fevereiro de 2019, para Nintendo Switch em março de 2021 e para Android e iOS em maio de 2022, tendo sido cancelado em janeiro de 2023, com o desligamento de seus servidores planejado para 1º de maio do mesmo ano. O jogo oferece suporte a jogabilidade multiplataforma."
    if jogo=="DayZ":
        detalhes_jogo = f"DayZ, originalmente DayZ Standalone, é um jogo eletrônico multijogador em mundo aberto desenvolvido pelo estúdio checo Bohemia Interactive Studio. DayZ Standalone é uma adaptação e sucessor do DayZ mod de 2012 que foi originalmente criado para o jogo ARMA 2, também desenvolvido pela Bohemia Interactive. O jogo DayZ tem como objetivo principal a sobrevivência em um contexto de infecção global, onde aqueles infectados pelo vírus se tornam extremamente agressivos. Diferentemente dos zumbis tradicionais, os infectados em DayZ são seres vivos e podem ser mortos por tiros em qualquer parte do corpo. Neste cenário desafiador, os jogadores precisam lutar pela sua própria sobrevivência, competindo também com outros jogadores por recursos escassos, como água, comida, armas e medicamentos."
    if jogo=="Team Fortress 2":
        detalhes_jogo = f"Team Fortress 2 é um jogo de tiro em primeira e terceira pessoa baseado em classes desenvolvido pela Valve e a sequência de Team Fortress Classic. Existem duas equipes jogáveis, RED e BLU, nas quais os jogadores podem entrar e completar objetivos em diferentes modos de jogo. Os jogadores podem escolher nove classes: Scout, Soldier, Pyro, Demoman, Heavy, Engineer, Medic, Sniper e Spy."
    if jogo=="PUBG":
        detalhes_jogo = f"PUBG: Battlegrounds (anteriormente conhecido como Player Unknown's Battlegrounds) é um jogo Battle Royale de 2017 desenvolvido pela PUBG Studios e publicado pela Krafton. O jogo, inspirado no filme japonês Battle Royale de 2000, é baseado em mods anteriores criados por Brendan 'PlayerUnknown' Greene para outros jogos e expandido para um jogo independente sob a direção criativa de Greene. É o primeiro jogo da série PUBG Universe."

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
