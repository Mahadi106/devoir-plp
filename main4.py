with open("input.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()

# Compte le nombre des mots
nombre_mots = len(contenu.split())

# Convertir tout le texte en majuscules
contenu_majuscule = contenu.upper()

# Écrire le résultat dans output.txt
with open("output.txt", "w", encoding="utf-8") as fichier:
    fichier.write("=== TEXTE EN MAJUSCULE ===\n")
    fichier.write(contenu_majuscule + "\n\n")
    fichier.write(f"Nombre de mots : {nombre_mots}\n")

# Message de succès
print("Le fichier output.txt a été créé avec succès !")