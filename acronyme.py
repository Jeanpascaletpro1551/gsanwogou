print("Bienvenue ce programme permet de générer un acronyme\n")
print("Un acronyme revient à transformer un mot ou une expression en sigle\n  ")
print("Exemple:Programmation orientée a pour acronyme: po \n")
print("Dès à présent veuillez suivre nos instructions svp:\n")
mot=str(input("Donner une expression svp:"))
grace=mot.split()
faith=''
for i in grace:
    faith=faith+str(i[0]).upper()
print(mot,"a pour acronyme",faith)