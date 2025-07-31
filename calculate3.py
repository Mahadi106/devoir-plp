def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:

# pas de remise

        return price
orginal_price = float(input("Saisir le prix d'origine : "))
discount = float(input("Saisir le pourcentage de remise : ")) 

# calcul final

final_prix = calculate_discount(original_price, discount)

# affichage du resultat

print(f"Le prix après la remise final est : {final_price}")
