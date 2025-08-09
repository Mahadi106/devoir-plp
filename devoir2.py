# Creation d'une liste vide
my_list = []

my_list.extend([10, 20, 30, 40])
my_list.insert(1,15)
 
# Etendre la liste 
my_list.extend([50, 60, 70])
 
# Suppression du dernier element 
my_list.remove(70)

# Trions la liste par ordre croissant
my_list.sort()
 
# 7. Recherche et affichage l'index de la valeur 
index_30 = my_list.index(30)

# Affichage des résultats
print("Liste finale :", my_list)
print("Index de la valeur 30 :", index_30)