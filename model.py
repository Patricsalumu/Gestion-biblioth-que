class Connexion_bdd:
	def __init__(self):
		import sqlite3 as bdd
		self.connect = bdd.connect("abonnes.db")
		self.cur = self.connect.cursor()

	#creation des tables
	def creerTables(self):
		self.cur.execute("CREATE TABLE abonnes(id_abonne INTEGER PRIMARY KEY AUTOINCREMENT\
		 UNIQUE NOT NULL, telephone TEXT UNIQUE, nom TEXT NULL, post_nom TEXT NULL, \
		 pre_nom TEXT NULL, sexe\
		  TEXT NULL, adresses TEXT, matricule TEXT, promotion TEXT, faculte TEXT, universite\
		  TEXT)")

		self.cur.execute("CREATE TABLE contenues(id_contenue INTEGER PRIMARY KEY AUTOINCREMENT\
			UNIQUE NOT NULL, titre TEXT, auteur TEXT, emplacement TEXT)")

		self.cur.execute("CREATE TABLE visites(id_visite INTEGER PRIMARY KEY AUTOINCREMENT\
			NOT NULL UNIQUE, id_abonne INTEGER, id_contenue INTEGER, date_visite TEXT, \
			est_remis INTEGER)")

		self.connect.close()

class Abonnes(Connexion_bdd):
	"""classe abonnes, le model qui gere les abonnes de la bibliotheque"""

	#ajouter abonne dans la table abonnes
	def ajouter(self, dictionnaire_abonne):
		self.cur.execute('INSERT INTO abonnes (telephone, nom, sexe, adresses, matricule,  \
			promotion, faculte, universite) VALUES(?,?,?,?,?,?,?,?)', dictionnaire_abonne)
		self.connect.commit()
		self.connect.close()

	#modifier abonne dans la table abonnes
	def modifier(self, dictionnaire_abonne, id_abonne):
		dictionnaire_abonne.append(id_abonne)
		with self.connect:
			self.cur.execute('UPDATE abonnes SET telephone=?, nom=?, sexe=?, adresses=?,\
			 matricule=?, promotion=?, faculte=?, universite=? WHERE id_abonne=?', (\
				dictionnaire_abonne))
		self.connect.commit()
		self.connect.close()
				
	#selectionner  les abonnes dans la table abonnes avec soit id, nom, telephone
	def selectionner_arg(self, argument):
		argument=['%'+str(argument)+'%', '%'+str(argument)+'%']
		abonnes = self.cur.execute('SELECT * FROM abonnes WHERE \
			telephone LIKE ? OR nom LIKE ?',argument)
		return abonnes
		
	#selectionner tout les abonnes.
	def selectionner_tout(self):
		abonnes = self.cur.execute('SELECT * FROM abonnes ORDER BY id_abonne DESC LIMIT(50)')
		return abonnes
	def checking(self, id_abonne):
		argument = []
		argument.append([id_abonne,][0])
		x=argument[0].replace('\n','')[1:]
		y=[x,]
		abonne = self.cur.execute('SELECT * FROM abonnes WHERE nom = ?',\
		 y)
		nom_existe = False
		for i in abonne:
			nom_existe = True
		return nom_existe

class Contenues(Connexion_bdd):
	"""classe contenues, le model qui regroupe les contenues : livre, article
	memoire de la bibliotheques"""

	#ajouter contenue dans la table contenues
	def ajouter(self, dictionnaire_contenue):
		self.cur.execute('INSERT INTO contenues(titre, auteur, emplacement) \
			VALUES(?,?,?)',dictionnaire_contenue)
		self.connect.commit()
		self.connect.close()

	#modifier contenue dans la table contenues
	def modifier(self, dictionnaire_contenue, id_contenue):
		dictionnaire_contenue.append(id_contenue)
		with self.connect:
			self.cur.execute('UPDATE contenues SET titre=?, auteur=?, emplacement=? WHERE \
				id_contenue=?',(dictionnaire_contenue))
		self.connect.commit()
		self.connect.close()

	#selectionner contenue dans la table contenues avec argument
	def selectionner_arg(self, argument):
		argument = ['%'+str(argument)+'%','%'+str(argument)+'%']
		contenues = self.cur.execute('SELECT * FROM contenues WHERE \
			titre LIKE ? OR auteur LIKE ?', argument)
		return contenues

	#selectionner tout les contenues
	def selectionner_tout(self):
		contenues = self.cur.execute('SELECT * FROM contenues ORDER BY id_contenue DESC LIMIT(50)')
		return contenues
	#selectionner un contenue
	def selectionner_un(self, id_contenue):
		id_contenue = [id_contenue,]
		contenues = self.cur.execute('SELECT * FROM contenues WHERE id_contenue=?',id_contenue)
		return contenues.fetchone()

class Visites(Connexion_bdd):
	"""classes visites, le model qui gere les visites de la bibliotheque"""

	#ajouter une visite
	def ajouter(self, dictionnaire_visite):
		self.cur.execute('INSERT INTO visites (id_abonne, id_contenue, date_visite, \
			est_remis) VALUES(?,?,?,?)', dictionnaire_visite)
		self.connect.commit()
		self.connect.close()

	#modifier une visite
	def modifier(self, id_visite):
		est_remis = ['Oui',id_visite]
		with self.connect:
			self.cur.execute('UPDATE visites SET est_remis=? WHERE id_visite=?', est_remis)

		self.connect.commit()
		self.connect.close()

	#selectionner une visite sur base de la date 
	def selectionner_arg(self, date_visite):
		date_visite =['%'+str(date_visite)+'%',]
		visites = self.cur.execute('SELECT * FROM visites WHERE date_visite LIKE ? ORDER BY \
			id_visite DESC', date_visite)
		return visites
	def recherche(self, argument):
		argument =['%'+str(argument)+'%',]
		visites = self.cur.execute('SELECT * FROM visites WHERE date_visite LIKE ?',\
			  argument)
		return visites
try:
	conexion = Connexion_bdd()
	conexion.creerTables()
except:
	pass