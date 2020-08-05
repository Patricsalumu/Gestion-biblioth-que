import model


def ajouter_abonne(dictionnaire_abonne):
	abonne = model.Abonnes()
	abonne.ajouter(dictionnaire_abonne)

def afficher_abonne():
	liste_abonnes = model.Abonnes()
	return liste_abonnes.selectionner_tout()
def checking_abonne(id_abonne):
	abonne = model.Abonnes()
	return abonne.checking(id_abonne)

def selectionner_abonne(telephone):
	abonne = model.Abonnes()
	return abonne.selectionner_arg(telephone)

def modifier_abonne(dictionnaire_abonne, id_abonne):
	abonne = model.Abonnes()
	abonne.modifier(dictionnaire_abonne, id_abonne)

def afficher_contenue():
	contenue = model.Contenues()
	return contenue.selectionner_tout()

def ajouter_contenue(dictionnaire_contenue):
	contenue = model.Contenues()
	contenue.ajouter(dictionnaire_contenue)

def selectionner_un_contenue(id_contenue):
	contenue = model.Contenues()
	return contenue.selectionner_un(id_contenue)
def selectionner_contenue(argument):
	contenue = model.Contenues()
	return contenue.selectionner_arg(argument)

def modifier_contenue(dictionnaire_contenue,id_contenue):
	contenue = model.Contenues()
	contenue.modifier(dictionnaire_contenue, id_contenue)


def afficher_visite(date_visite):
	visite = model.Visites()
	return visite.selectionner_arg(date_visite)

def recherche_visite(argument):
	visite = model.Visites()
	return visite.recherche(argument)

def ajouter_visite(dictionnaire_visite):
	visite = model.Visites()
	visite.ajouter(dictionnaire_visite)

def modifier_visite(id_visite):
	visite = model.Visites()
	visite.modifier(id_visite)

