from PIL import Image, ImageTk
def load_images():
    image1 = Image.open("imagens/mario.jpg").resize((120, 120))
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("imagens/kingdomrush.jpg").resize((120, 120))
    photo2 = ImageTk.PhotoImage(image2)

    image3 = Image.open("imagens/csgo.jpg").resize((120, 120))
    photo3 = ImageTk.PhotoImage(image3)

    image4 = Image.open("imagens/bloons.jpg").resize((120, 120))
    photo4 = ImageTk.PhotoImage(image4)

    image5 = Image.open("imagens/pacman.jpg").resize((120, 120))
    photo5 = ImageTk.PhotoImage(image5)

    image6 = Image.open("imagens/donkeykong.jpg").resize((120, 120))
    photo6 = ImageTk.PhotoImage(image6)

    image7 = Image.open("imagens/tetris.jpg").resize((120, 120))
    photo7 = ImageTk.PhotoImage(image7)

    image8 = Image.open("imagens/contra.jpg").resize((120, 120))
    photo8 = ImageTk.PhotoImage(image8)

    image9 = Image.open("imagens/sonic.jpg").resize((120, 120))
    photo9 = ImageTk.PhotoImage(image9)

    image10 = Image.open("imagens/metalslug3.jpg").resize((120, 120))
    photo10 = ImageTk.PhotoImage(image10)

    # Corrigir a atribuição das imagens FPS
    image11 = Image.open("imagens/ark.jpg").resize((120, 120))
    photo11 = ImageTk.PhotoImage(image11)

    image12 = Image.open("imagens/apexlegends.jpg").resize((120, 120))
    photo12 = ImageTk.PhotoImage(image12)

    image13 = Image.open("imagens/dayz.jpg").resize((120, 120))
    photo13 = ImageTk.PhotoImage(image13)

    image14 = Image.open("imagens/teamfortress2.jpg").resize((120, 120))
    photo14 = ImageTk.PhotoImage(image14)

    image15 = Image.open("imagens/pubg.jpg").resize((120, 120))
    photo15 = ImageTk.PhotoImage(image15)

    image16 = Image.open("imagens/fundo.jpg").resize((500, 500))
    photo16 = ImageTk.PhotoImage(image16)

    image17 = Image.open("imagens/mostrar.jpg").resize((15, 15))
    photo17 = ImageTk.PhotoImage(image17)

    image18 = Image.open("imagens/esconder.jpg").resize((15, 15))
    photo18 = ImageTk.PhotoImage(image18)

    image19 = Image.open("imagens/wallpaper.jpg").resize((700, 700))
    photo19 = ImageTk.PhotoImage(image19)

    return photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, photo11, photo12, photo13, photo14, photo15, photo16, photo17, photo18, photo19
