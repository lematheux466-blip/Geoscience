eleve_liste=[ "matheux","cheick","sayouba","gueu","moussa","geologue"]
with open("eleve.txt","a+") as file:
    for geologue in eleve_liste:
        file.write(geologue+"\n")
file.close()


file=open("eleve.txt","a+")
file.write("cheick/\n")
file.close()


import random
with open("eleve.txt","r") as file:
    content=random.choice(file.readlines())
    print("Le nom choisi pour toi est :", content)
file.close()