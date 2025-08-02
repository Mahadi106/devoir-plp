class Smartphone:
    # Constructeur pour donner une marque et un modèle
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.batterie = 100  # batterie initiale à 100%

    # Méthode pour appeler un numéro
    def appeler(self, numero):
        print(f"{self.marque} {self.modele} appelle {numero}...")

    # Méthode pour afficher les informations du téléphone
    def afficher_info(self):
        print(f"Smartphone: {self.marque} {self.modele}, Batterie: {self.batterie}%")

# Exemple  
print("=== Exemple Smartphone ===")
phone = Smartphone("Samsung", "A12")
phone.appeler("+22890123456")
phone.afficher_info()



# PARTIE 2 : Polymorphisme


class Voiture:
    def move(self):
        print("La voiture conduit 🚗")

class Avion:
    def move(self):
        print("L'avion vole ✈️")

class Bateau:
    def move(self):
        print("Le bateau navigue 🚤")

# Exemple d'utilisation  
print("\n=== Exemple Polymorphisme ===")
vehicules = [Voiture(), Avion(), Bateau()]

for v in vehicules:
    v.move()