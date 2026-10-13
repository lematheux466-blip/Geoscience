x=2
while x<12:
    print( x)
    x+=2


    etudiants=["Matheux","sayouba","gueu","moussa"]
    for i in etudiants:
        print(i,len(i))


for i in range(4,12):
    nom =input("entrer le nom de l echantillon: ")
    localite = input("entrer la localite: ")
    roche=input("entrer le type de la roche: ")
    masse=float(input("entrer la valeur de la masse en g "))
    volume=float(input("entrer la valeur du volume en cm"))
    densite=masse/volume
    print(f""
    nom={nom}
    localite:{localite}
    roche:{roche}
    masse:{masse}
    volume:{volume}
     densite:{densite}
     "")
if densite<2.6:
     print("la roche est legere ")
elif densite>2.6 and densite<3:
    print("la roches est de densite moyenne ") 
elif densite>3:
     print("la roche est dense")
else:
    print("la roche est de densite inconnue")
    print(nom)



import equat  ion
equation.facto(2)

from equation import facto
print (facto (3))