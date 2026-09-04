print ( "veillez renseigner ce formulaire si vous voulez utiliser  nos machines")
nom=input(" entrer le nom de la machine  ")
niveau =input("quel est votre niveau de formation?  ")
if niveau == "debutant":
    print(f" vu votre niveau: {niveau} vous  n'avez pas accè à la machine {nom}")
elif niveau== "intermediaire":
    print(f" vous avez accè uniquement à {nom} ")
else:
    print(f" vous avez accè à toutes les machines")

    