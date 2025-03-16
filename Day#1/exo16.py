prix = int(input("Donner un prix : " ))
tva = int(input("Donner le TVA pourcentage : " + "%" ))
montant_TVA = prix * (tva /100 )
montant_TTC = prix + montant_TVA
print (f"Le TTC est : {montant_TTC}")