from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import ctrl
import datetime


global fenetre_principal 
fenetre_principal = Tk()
class configuration(object):
	"""classe pour la configuration gerale"""
	def __init__(self):
		global fenetre_principal
		fenetre_principal.title("Gestion Bibliothèque by Congo Mémoire")
		fenetre_principal.geometry("800x600+" + str(0) + "+" + str(0))

		#menu
		self.barre_de_menu = Menu(fenetre_principal)

		self.menu_abonnes = Menu(self.barre_de_menu, tearoff=1)
		self.menu_abonnes.add_command(label="Afficher Abonnés", command=demarrage_abonne)
		self.barre_de_menu.add_cascade(label="Abonnés", menu=self.menu_abonnes)
		fenetre_principal.config(menu=self.barre_de_menu)

		self.menu_contenues = Menu(self.barre_de_menu, tearoff=1)
		self.menu_contenues.add_command(label="Afficher Contenus", \
			command=demarrage_contenue)
		self.barre_de_menu.add_cascade(label="Contenus", menu=self.menu_contenues)
		fenetre_principal.config(menu=self.barre_de_menu)

		self.menu_visites = Menu(self.barre_de_menu, tearoff=1)
		self.menu_visites.add_command(label="Afficher visites", \
			command=demarrage_visite)
		self.barre_de_menu.add_cascade(label="Visites", menu=self.menu_visites)
		fenetre_principal.config(menu=self.barre_de_menu)
	
	def nouvel_abonne():
		def ajouter():
			abonne = [telephoneEntry.get(), nomEntry.get(), sexeEntry.get(), \
			adresseEntry.get(), matriculeEntry.get(), promotionEntry.get(),\
			faculteEntry.get(), universiteEntry.get()]
			if telephoneEntry.get()=='':
				messagebox.showerror("Ajouter abonné", "Impossible d'ajouter \
numèro de telephone ne doit pas etre vide.")
			else:
				try:
					ctrl.ajouter_abonne(abonne)
				except:
					messagebox.showerror("Ajouter abonné", "Impossible d'ajouter \
	numèro de telephone existe")
				
			top.destroy()
			abonnes = ctrl.afficher_abonne()
			Abonnes.misajour(abonnes)


		top=Toplevel()
		top.title("Enregistrer Abonné")
		top.resizable(width=False, height=False)

		lar = top.winfo_screenwidth()
		lon = top.winfo_screenheight()

		x = int(lar / 2 - 400 / 2)
		y = int(lon / 2 - 600 / 2)
		top.geometry("400x550+" + str(x) + "+" + str(y))

		telephone=Label(top, text="1. Telephone  ")
		telephone.place(relx=0.02, rely=0.02, relheight=0.03, relwidth=0.20)
		telephoneEntry=Entry(top, bd=2, width=45)
		telephoneEntry.place(relx=0.02, rely=0.05, relheight=0.045, relwidth=0.95)


		nom=Label(top, text="2. nom  ")
		nom.place(relx=0.02, rely=0.10, relheight=0.03, relwidth=0.11)
		nomEntry=Entry(top, bd=2, width=45)
		nomEntry.place(relx=0.02, rely=0.13, relheight=0.045, relwidth=0.95)


		sexe=Label(top, text="3. sexe  ")
		sexe.place(relx=0.02, rely=0.18, relheight=0.03, relwidth=0.11)
		sexeEntry=Entry(top, bd=2, width=45)
		sexeEntry.place(relx=0.02, rely=0.21, relheight=0.045, relwidth=0.95)


		adresse=Label(top, text="5. adresse  ")
		adresse.place(relx=0.02, rely=0.26, relheight=0.03, relwidth=0.15)
		adresseEntry=Entry(top, bd=2, width=45)
		adresseEntry.place(relx=0.02, rely=0.29, relheight=0.045, relwidth=0.95)

		universite=Label(top, text="4. universite  ")
		universite.place(relx=0.02, rely=0.34, relheight=0.03, relwidth=0.19)
		universiteEntry=Entry(top, bd=2, width=45)
		universiteEntry.place(relx=0.02, rely=0.37, relheight=0.045, relwidth=0.95)


		matricule=Label(top, text="6. matricule  ")
		matricule.place(relx=0.02, rely=0.42, relheight=0.03, relwidth=0.18)
		matriculeEntry=Entry(top, bd=2, width=45)
		matriculeEntry.place(relx=0.02, rely=0.45, relheight=0.045, relwidth=0.95)

		faculte=Label(top, text="8. faculte  ")
		faculte.place(relx=0.02, rely=0.50, relheight=0.03, relwidth=0.15)
		faculteEntry=Entry(top, bd=2, width=45)
		faculteEntry.place(relx=0.02, rely=0.53, relheight=0.045, relwidth=0.95)


		promotion=Label(top, text="7. promotion  ")
		promotion.place(relx=0.02, rely=0.58, relheight=0.03, relwidth=0.20)
		promotionEntry=Entry(top, bd=2, width=45)
		promotionEntry.place(relx=0.02, rely=0.61, relheight=0.045, relwidth=0.95)


		btn_enregistrer=Button(top, text='Enregistrer',\
		 bg='#1D1F90', fg='white', command=ajouter)
		btn_enregistrer.place(relx=0.77, rely=0.80, relheight=0.05,relwidth=0.20)

	def modifier_abonne(telephone):
		objet = ctrl.selectionner_abonne(telephone)
		global abonne
		abonne = []
		for valeur in objet:
			abonne.append(valeur)
		def modifier():
			global abonne
			id_abonne = abonne[0][0]
			abonnes = [telephoneEntry.get(), nomEntry.get(), sexeEntry.get(), \
			adresseEntry.get(), matriculeEntry.get(), promotionEntry.get(),\
			faculteEntry.get(), universiteEntry.get()]
			if telephoneEntry.get()=='':
				messagebox.showerror("Modifier abonné", "Impossible de modifier \
numèro de telephone ne doit pas etre vide")
			else:
				try:
					ctrl.modifier_abonne(abonnes, id_abonne)
				except:
					messagebox.showerror("Modifier abonné", "Impossible de modifier \
numèro de telephone existe")

			top.destroy()
			abonnes = ctrl.afficher_abonne()
			Abonnes.misajour(abonnes)


		top=Toplevel()
		top.title("Modifier Abonné")
		top.resizable(width=False, height=False)

		lar = top.winfo_screenwidth()
		lon = top.winfo_screenheight()

		x = int(lar / 2 - 400 / 2)
		y = int(lon / 2 - 600 / 2)
		top.geometry("400x550+" + str(x) + "+" + str(y))

		telephone=Label(top, text="1. Telephone  ")
		telephone.place(relx=0.02, rely=0.02, relheight=0.03, relwidth=0.20)
		telephoneEntry=Entry(top, bd=2, width=45)
		telephoneEntry.insert(0, str(abonne[0][1]))
		telephoneEntry.place(relx=0.02, rely=0.05, relheight=0.045, relwidth=0.95)
		


		nom=Label(top, text="2. nom  ")
		nom.place(relx=0.02, rely=0.10, relheight=0.03, relwidth=0.11)
		nomEntry=Entry(top, bd=2, width=45)
		nomEntry.insert(0, str(abonne[0][2]))
		nomEntry.place(relx=0.02, rely=0.13, relheight=0.045, relwidth=0.95)
		


		sexe=Label(top, text="3. sexe  ")
		sexe.place(relx=0.02, rely=0.18, relheight=0.03, relwidth=0.11)
		sexeEntry=Entry(top, bd=2, width=45)
		sexeEntry.insert(0, str(abonne[0][5]))
		sexeEntry.place(relx=0.02, rely=0.21, relheight=0.045, relwidth=0.95)
		
		adresse=Label(top, text="4. adresse  ")
		adresse.place(relx=0.02, rely=0.26, relheight=0.03, relwidth=0.15)
		adresseEntry=Entry(top, bd=2, width=45)
		adresseEntry.insert(0, str(abonne[0][6]))
		adresseEntry.place(relx=0.02, rely=0.29, relheight=0.045, relwidth=0.95)

		universite=Label(top, text="5. universite  ")
		universite.place(relx=0.02, rely=0.34, relheight=0.03, relwidth=0.19)
		universiteEntry=Entry(top, bd=2, width=45)
		universiteEntry.insert(0, str(abonne[0][10]))
		universiteEntry.place(relx=0.02, rely=0.37, relheight=0.045, relwidth=0.95)
		
		matricule=Label(top, text="6. matricule  ")
		matricule.place(relx=0.02, rely=0.42, relheight=0.03, relwidth=0.18)
		matriculeEntry=Entry(top, bd=2, width=45)
		matriculeEntry.insert(0, str(abonne[0][7]))
		matriculeEntry.place(relx=0.02, rely=0.45, relheight=0.045, relwidth=0.95)		

		faculte=Label(top, text="7. faculte  ")
		faculte.place(relx=0.02, rely=0.50, relheight=0.03, relwidth=0.15)
		faculteEntry=Entry(top, bd=2, width=45)
		faculteEntry.insert(0, str(abonne[0][9]))
		faculteEntry.place(relx=0.02, rely=0.53, relheight=0.045, relwidth=0.95)

		promotion=Label(top, text="8. promotion  ")
		promotion.place(relx=0.02, rely=0.58, relheight=0.03, relwidth=0.20)
		promotionEntry=Entry(top, bd=2, width=45)
		promotionEntry.insert(0, str(abonne[0][8]))
		promotionEntry.place(relx=0.02, rely=0.61, relheight=0.045, relwidth=0.95)

		

		btn_enregistrer=Button(top, text="Modifier",\
		 bg='#1D1F90', fg='white', command=modifier)
		btn_enregistrer.place(relx=0.77, rely=0.80, relheight=0.05,relwidth=0.20)
	

	def nouvau_contenu():
		def ajouter():
			contenue = [titreEntry.get(1.0, END), auteurEntry.get(), emplacementEntry.get(1.0, END)]
			top.destroy()
			ctrl.ajouter_contenue(contenue)
			contenues = ctrl.afficher_contenue()
			Contenues.misajour(contenues)


		top=Toplevel()
		top.title("Enregistrer contenu")
		top.resizable(width=False, height=False)

		lar = top.winfo_screenwidth()
		lon = top.winfo_screenheight()

		x = int(lar / 2 - 400 / 2)
		y = int(lon / 2 - 600 / 2)
		top.geometry("400x550+" + str(x) + "+" + str(y))

		titre=Label(top, text="1. Titre  ")
		titre.place(relx=0.02, rely=0.02, relheight=0.03, relwidth=0.12)
		titreEntry=Text(top, bd=2, width=45)
		titreEntry.place(relx=0.02, rely=0.05, relheight=0.06, relwidth=0.95)


		auteur=Label(top, text="2. Auteur  ")
		auteur.place(relx=0.02, rely=0.14, relheight=0.03, relwidth=0.15)
		auteurEntry=Entry(top, bd=2, width=45)
		auteurEntry.place(relx=0.02, rely=0.18, relheight=0.045, relwidth=0.95)


		emplacement=Label(top, text="3. Emplacement  ")
		emplacement.place(relx=0.02, rely=0.26, relheight=0.03, relwidth=0.24)
		emplacementEntry=Text(top, bd=2, width=45)
		emplacementEntry.place(relx=0.02, rely=0.30, relheight=0.06, relwidth=0.95)


		btn_enregistrer=Button(top, text='Enregistrer',\
		 bg='#1D1F90', fg='white', command=ajouter)
		btn_enregistrer.place(relx=0.77, rely=0.80, relheight=0.05,relwidth=0.20)

	def modifier_contenue(id_contenue):
		global id_con
		id_con = id_contenue
		contenue = ctrl.selectionner_un_contenue(id_contenue)
		def modifier():
			global id_con
			contenue = [titreEntry.get(1.0, END), auteurEntry.get(), emplacementEntry.get(1.0, END)]
			top.destroy()
			ctrl.modifier_contenue(contenue, id_con)
			contenues = ctrl.afficher_contenue()
			Contenues.misajour(contenues)


		top=Toplevel()
		top.title("Modifier contenu")
		top.resizable(width=False, height=False)

		lar = top.winfo_screenwidth()
		lon = top.winfo_screenheight()

		x = int(lar / 2 - 400 / 2)
		y = int(lon / 2 - 600 / 2)
		top.geometry("400x550+" + str(x) + "+" + str(y))

		titre=Label(top, text="1. Titre  ")
		titre.place(relx=0.02, rely=0.02, relheight=0.03, relwidth=0.12)
		titreEntry=Text(top, bd=2, width=45)
		titreEntry.insert(END, contenue[1])
		titreEntry.place(relx=0.02, rely=0.05, relheight=0.06, relwidth=0.95)


		auteur=Label(top, text="2. Auteur  ")
		auteur.place(relx=0.02, rely=0.14, relheight=0.03, relwidth=0.15)
		auteurEntry=Entry(top, bd=2, width=45)
		auteurEntry.insert(END, contenue[2])
		auteurEntry.place(relx=0.02, rely=0.18, relheight=0.045, relwidth=0.95)


		emplacement=Label(top, text="3. Emplacement  ")
		emplacement.place(relx=0.02, rely=0.26, relheight=0.03, relwidth=0.24)
		emplacementEntry=Text(top, bd=2, width=45)
		emplacementEntry.insert(END, contenue[3])
		emplacementEntry.place(relx=0.02, rely=0.30, relheight=0.06, relwidth=0.95)


		btn_enregistrer=Button(top, text='Modifier',\
		 bg='#1D1F90', fg='white', command=modifier)
		btn_enregistrer.place(relx=0.77, rely=0.80, relheight=0.05,relwidth=0.20)

	def nouvelle_visite():
		def miseajour_abonne(abonne):
			liste_abonne.delete(0, END)
			for titre in ctrl.selectionner_abonne(abonne):
				liste_abonne.insert(int(titre[0]), ' '+str(titre[2]))

		def miseajour_contenue(abonne):
			liste_contenue.delete(0, END)
			for contenue in ctrl.selectionner_contenue(abonne):
				liste_contenue.insert(int(contenue[0]), ' '+str(contenue[1])+' \
				('+contenue[2]+')')

		def getrow_abonne(event):
			abonneEntry.delete(0.0, END)
			abonneEntry.insert(END, liste_abonne.get(ANCHOR))

		def getrow_contenue(event):
			contenueEntry.delete(0.0, END)
			contenueEntry.insert(END, liste_contenue.get(ANCHOR))
		global rec0
		rec0 = ''
		def recherche_abonne(event):
			global rec0
			if repr(event.char)=="'\\x08'":
				rec0=rec0[:len(rec0)-1]
			else:
				rec0=rec0+repr(event.char).replace("'","")
				rec0=rec0
			miseajour_abonne(rec0)
		global rec1
		rec1 = ''
		def recherche_contenue(event):
			global rec1
			if repr(event.char)=="'\\x08'":
				rec1=rec1[:len(rec1)-1]
			else:
				rec1=rec1+repr(event.char).replace("'","")
				rec1=rec1
			miseajour_contenue(rec1)

		def ajouter():
			visites = [abonneEntry.get(0.0, END), contenueEntry.get(0.0, END),
			 date_now, 'Non']
			variable_vis = str(abonneEntry.get(1.0, END))
			if str(abonneEntry.get(0.0, END))!='\n':
				if ctrl.checking_abonne(variable_vis):
					top.destroy()
					ctrl.ajouter_visite(visites)
					visites = ctrl.afficher_visite(date_now)
					Visites.misajour(visites)
				else:
					messagebox.showerror('Erreur visite','Abonné Inconnu')


			else:
				messagebox.showerror('Erreur visite','Abonné ne doit pas etre vide')

		top=Toplevel()
		top.title("Enregistrer une visite")
		top.resizable(width=False, height=False)

		lar = top.winfo_screenwidth()
		lon = top.winfo_screenheight()

		x = int(lar / 2 - 400 / 2)
		y = int(lon / 2 - 600 / 2)
		top.geometry("400x550+" + str(x) + "+" + str(y))

		abonne=Label(top, text="1. Abonne  ")
		abonne.place(relx=0.02, rely=0.02, relheight=0.03, relwidth=0.16)
		abonneEntry=Text(top, bd=2, width=45)
		abonneEntry.place(relx=0.02, rely=0.05, relheight=0.06, relwidth=0.95)
		abonneEntry.bind('<Key>', recherche_abonne)

		liste_abonne = Listbox(top, bd=0)
		for titre in ctrl.selectionner_abonne(' '):
			liste_abonne.insert(int(titre[0]), ' '+str(titre[2]))
		liste_abonne.bind('<Double 1>', getrow_abonne)
		liste_abonne.place(relx=0.02, rely=0.10, relheight=0.20, relwidth=0.95)



		contenue=Label(top, text="2. Contenu  ")
		contenue.place(relx=0.02, rely=0.32, relheight=0.03, relwidth=0.18)
		contenueEntry=Text(top, bd=2, width=45)
		contenueEntry.place(relx=0.02, rely=0.35, relheight=0.06, relwidth=0.95)
		contenueEntry.bind('<Key>', recherche_contenue)

		liste_contenue = Listbox(top, bd=0)
		for contenue in ctrl.selectionner_contenue(' '):
			liste_contenue.insert(int(contenue[0]), ' '+str(contenue[1]))
		liste_contenue.bind('<Double 1>', getrow_contenue)
		liste_contenue.place(relx=0.02, rely=0.40, relheight=0.20, relwidth=0.95)


		btn_enregistrer=Button(top, text='Enregistrer',\
		 bg='#1D1F90', fg='white', command=ajouter)
		btn_enregistrer.place(relx=0.77, rely=0.80, relheight=0.05,relwidth=0.20)

	def modifier_visite(id_visite):
		ctrl.modifier_visite(id_visite)
		visites = ctrl.afficher_visite(date_now)
		Visites.misajour(visites)



	def passer():
		pass

class Abonnes(configuration):
	"""vue visites"""
	global fenetre_principal
	global tableau
	global rec
	rec=""
	def misajour(abonnes):
		global tableau
		tableau.delete(*tableau.get_children())
		for abonne in abonnes:
			tableau.insert("", "end", values=(abonne[2],abonne[1],\
				abonne[5],abonne[10],abonne[6]))

	def modifier(event):
		item=tableau.item(tableau.focus())
		configuration.modifier_abonne(item['values'][1])
	def recherche(event):
		global rec
		if repr(event.char)=="'\\x08'":
			rec=rec[:len(rec)-1]
		else:
			rec=rec+repr(event.char).replace("'","")
			rec=rec
		abonnes = ctrl.selectionner_abonne(rec)
		Abonnes.misajour(abonnes)

	def afficher(self):
		rechercheEntry=Entry(fenetre_principal, bd=2, width=45)
		rechercheEntry.place(relx=0.67, rely=0.01, relheight=0.045, relwidth=0.30)
		rechercheEntry.bind('<Key>', Abonnes.recherche)
		global tableau
		tableau=ttk.Treeview(fenetre_principal, columns=(1,2,3,4,5), \
			show='headings')
		tableau.place(relx=0.02, rely=0.06, relheight=0.84,relwidth=0.95)
		tableau.heading(1, text='Nom')
		tableau.column(1, width=140)
		tableau.heading(2, text='Telephone')
		tableau.column(2, width=100)
		tableau.heading(3, text='Sexe')
		tableau.column(3, width=20)
		tableau.heading(4, text='Universite')
		tableau.column(4, width=60)
		tableau.heading(5, text='Adresse')
		tableau.column(5, width=200)


		btn_nouvel_abone=Button(fenetre_principal, text='Nouvel Abonné',\
		 bg='#1D1F90', fg='white', command=configuration.nouvel_abonne)
		btn_nouvel_abone.place(relx=0.77, rely=0.93, relheight=0.05,relwidth=0.20)

		for abonne in ctrl.afficher_abonne():
			tableau.insert("", "end", values=(abonne[2],abonne[1],abonne[5],abonne[10],abonne[6]))

		tableau.bind('<Double 1>', Abonnes.modifier)

		fenetre_principal.mainloop()

class Contenues(configuration):
	"""vue Contenues"""
	global tableau
	global rec
	rec=""
	def misajour(contenues):
		global tableau
		tableau.delete(*tableau.get_children())
		for contenue in contenues:
			tableau.insert("", "end", values=(contenue))
	def modifier(event):
		item=tableau.item(tableau.focus())
		configuration.modifier_contenue(item['values'][0])
	def recherche(event):
		global rec
		if repr(event.char)=="'\\x08'":
			rec=rec[:len(rec)-1]
		else:
			rec=rec+repr(event.char).replace("'","")
			rec=rec
		contenues = ctrl.selectionner_contenue(rec)
		Contenues.misajour(contenues)

	def afficher(self):
		rechercheEntry=Entry(fenetre_principal, bd=2, width=45)
		rechercheEntry.place(relx=0.67, rely=0.01, relheight=0.045, relwidth=0.30)
		rechercheEntry.bind('<Key>', Contenues.recherche)
		global tableau
		tableau=ttk.Treeview(fenetre_principal, columns=(1,2,3, 4), \
			show='headings')
		tableau.place(relx=0.02, rely=0.06, relheight=0.84,relwidth=0.95)
		tableau.heading(1, text='Id')
		tableau.column(1, width=3)
		tableau.heading(2, text='Titre')
		tableau.column(2, width=140)
		tableau.heading(3, text='Auteur')
		tableau.column(3, width=100)
		tableau.heading(4, text='Emplacement')
		tableau.column(4, width=20)

		for contenue in ctrl.afficher_contenue():
			tableau.insert("", "end", values=contenue)
		
		tableau.bind('<Double 1>', Contenues.modifier)

		btn_nouvel_abone=Button(fenetre_principal, text='Nouvau contenu',\
		 bg='#1D1F90', fg='white', command=configuration.nouvau_contenu)
		btn_nouvel_abone.place(relx=0.77, rely=0.93, relheight=0.05,relwidth=0.20)
		
		fenetre_principal.mainloop()

class Visites(configuration):
	"""Vue Visites"""
	global tableau
	global rechercheEntry
	rechercheEntry = ""
	global date_now
	date_now = datetime.datetime.now()
	date_now = 	dateNow=str(date_now.year)+"-"+str(date_now.month)+"-"+\
	str(date_now.day)
	def misajour(visites):
		global tableau
		tableau.delete(*tableau.get_children())
		for visite in visites:
			tableau.insert("", "end", values=visite)
	def recherche(event):
		global rechercheEntry
		if repr(event.char)=="'\\r'":
			visites = ctrl.recherche_visite(rechercheEntry.get())
			Visites.misajour(visites)

	def modifier(event):
		rep=messagebox.askokcancel("Confirmer L'operation", "Contenu est remis ? \
			\n Nb: Cette action est irrevestible")
		if rep :
			item=tableau.item(tableau.focus())
			configuration.modifier_visite(item['values'][0])

	def afficher(self):
		global fenetre_principal
		global date_now
		global rechercheEntry
		rechercheEntry=Entry(fenetre_principal, bd=2, width=45)
		rechercheEntry.insert(0,date_now)
		rechercheEntry.place(relx=0.67, rely=0.01, relheight=0.045, relwidth=0.30)
		rechercheEntry.bind('<Key>', Visites.recherche)

		global tableau
		tableau=ttk.Treeview(fenetre_principal, columns=(1,2,3,4,5), \
			show='headings')
		tableau.place(relx=0.02, rely=0.06, relheight=0.84,relwidth=0.95)
		tableau.heading(1, text='Id')
		tableau.column(1, width=10)
		tableau.heading(2, text='Nom abonné')
		tableau.column(2, width=100)
		tableau.heading(3, text='Contenu consulté')
		tableau.column(3, width=200)
		tableau.heading(4, text='Date')
		tableau.column(4, width=60)
		tableau.heading(5, text='Remise')
		tableau.column(5, width=20)


		btn_nouvelle_visite=Button(fenetre_principal, text='Nouvelle visite',\
		 bg='#1D1F90', fg='white', command=configuration.nouvelle_visite)
		btn_nouvelle_visite.place(relx=0.77, rely=0.93, relheight=0.05,relwidth=0.20)
		for visite in ctrl.afficher_visite(date_now):
			tableau.insert("", "end", values=(visite))

		tableau.bind('<Double 1>', Visites.modifier)
		fenetre_principal.mainloop()
def demarrage_abonne():
	demarrage = Abonnes()
	demarrage.afficher()
def demarrage_contenue():
	demarrage = Contenues()
	demarrage.afficher()
def demarrage_visite():	
	demarrage = Visites()
	demarrage.afficher()

demarrage_abonne()