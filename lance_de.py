import random
print("Le programme permet d'affcher la face d'un dé\n")
print("Il est à noter qu'un dé à six faces numérotées se 1 à 6\n")
print("Dès à présent veuillez suivre nos instructions svp\n")
print("Taper 1:pour lancer le dé 0:pour quitter\n")
while True:
    x=int(input("cliquer sur une touche"))
    if x==0:
        print("Bye")
        break
    elif x==1:
        print(random.randint(1,6))
    else:
        print("J'ai pas compris")

    print("Vous devez garder à l'esprit que lorsque vous taper 0 vous sortez du jeu 1 vous lancer le dé tout autre touche n'affiche rien d'important\n")
    print("Merci pour votre compréhension au revoir et à la prochaine")
