print("veuilez renseigner cette fiche Technique de materiau:")
nom=input(" quel est le  nom du materiau ?")
epaisseur= int(input(" de quel epaisseur?"))
quantite=int(input(" quelle qantite voulez vous?"))
prix=int(5000 )
total= prix*quantite
print(f" bonjours monsieur ,vous voulez:{nom}, d'une epaisseur de {epaisseur} mm, {quantite} pices ; vous devez  alors payez: total={prix}*{quantite}= {total} CFA merci pour votre confiance.")