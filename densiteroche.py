nbre=int(input("entrer le nombre de fois"))
nom=(input("entrer le nom de l echantillon"))
localite=(input("entrer la localite de l echantillon"))
roche=(input("entrer le type de roche"))
masse=float(input("entrer la valeur de la masse en g"))
volume=float(input("entrer la valeur du volume en cm³"))
densite=masse/volume
print(f"""
echantillon:{nom}
localite:{localite}
roche:{roche}
densite:{densite} 
""")
if densite<2.6:
     print("la roche est legere ")
elif densite>2.6 and densite<3:
    print("la roches est de densite moyenne ") 
elif densite>3:
     print("la roche est dense")
else:
    print("la roche est de densite inconnue")
    print(nom)


    