from tkinter import *
import webbrowser
import string
from random import *

def open_insta():
	webbrowser.open_new('https://www.instagram.com/h4ck3rm4n04/?next=%2F')

def generate_password():
	min_pass = 6
	max_pass = 15
	tout_les_caractères =string.ascii_letters + string.digits + string.punctuation
	password = "".join(choice(tout_les_caractères) for x in range(randint(min_pass, max_pass)))
	input_champ.delete(0, END)
	input_champ.insert(0, password)


window = Tk()
window.title('Générateur de Mot de Passe')
window.geometry('1080x700')
window.minsize(500, 300)
window.iconbitmap('Capture.ico')
window.config(background = '#000000')

normal_frame = Frame(window, bg = "#000000",bd = 0)

grand_titre = Label(window, text = "h4cK3rm4n04", bg = '#000000', fg = "#fd0101", font = ("Old English Text MT", 30))
grand_titre.pack()


button_insta = Button(window, text = 'Follow Me on Instagram', font = ('CommercialScript BT', 25), bg = "#43cfff", fg = "white", command = open_insta)
button_insta.pack(side = BOTTOM)

normal_frame.pack(expand = YES)


#création d'une image sur l'interface graphique


width = 300
height = 300
prem_image = PhotoImage(file="Hacker.gif").zoom(5).subsample(9)
										#vérifier l'orthographe de highlightthickness juste au cas ou les autres ne fonctionneront pas
canvas = Canvas(normal_frame, width = width, height = 300, bg = '#000000', bd = 0, highlightthickness = 0)
canvas.create_image(width/2, height/2, image = prem_image)
canvas.grid(row = 0, column = 0, sticky = W)



#Fin de la création de l'image sur l'interface graphique

#création d'un sous boîte

right_frame = Frame(normal_frame, bg = '#000000')

texte_gen = Label(right_frame, text = 'Click on Generate Password', bg = '#000000', fg = 'green', font = ('CommercialScript BT', 50))
texte_gen.pack()


#création d'un champ d'entré de l'User
input_champ = Entry(right_frame, font = ('Arial', 50), bg = 'blue')
input_champ.pack()

right_frame.grid(row = 0, column = 1, sticky = W)

#création du bouton pour générer le mot de passe
button_to_generate = Button(right_frame, text = 'Generate Password', font = ('MD thaitype A', 30), command = generate_password)
button_to_generate.pack()  #fill = X à l'interieur des pharenthèses prend toute la place disponible sur l'axe des abs

#Création d'une barre de menu

menu_barre = Menu(window)
file_menu = Menu(menu_barre, tearoff = 0)
file_menu.add_command(label = 'Nouveau', command = generate_password)
file_menu.add_command(label = 'quitter', command = window.quit)
menu_barre.add_cascade(label = 'Fichier', menu = file_menu)

window.config(menu = menu_barre)

window.mainloop()