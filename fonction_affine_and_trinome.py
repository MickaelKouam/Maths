""" Projet Maths: resolution de fonction """
"""
Ce projet veut traiter une fonction simple dans un premier temps
de son domaine de definition a son tableau de variation
"""

def menu():
    print("======= Bienvenue dans votre programme traiteur de fonction !!! =======")
    print("=   Pour commencer vous devez choisir le type de votre fonction !     =")
    print("=              1: Fonction affine - f(x) = ax + b                     =")
    print("=            2: Fonction trinome - f(x) = ax2 + bx + c                =")
    print("=         3: Fonction quotient - f(x) = (ax + b) / (cx + d)           =")
    print("=                 4: Fonction racine carree                           =")
    print("=======================================================================")
    return 0


menu()
print()
choix = int(input("Entrez votre choix ! "))
if(choix == 1):
    print("Vous allez a present entrer la valeur des coef. a et b \n")
    a = int(input("Entrez la valeur de 'a' "))
    b = int(input("Entrez la valeur de 'b' "))
    if(b < 0):
        signe = "-"
    elif(b > 0):
        signe = "+"
    # reduire b a sa valeur absolue pour affichage
    bAffich = abs(b)
    
    # afficher la fonction de l'utilisateur 
    print("\nVotre fonction est: f(x) = {}x {} {} ".format(a, signe, bAffich))

    # afficher le domaine de definition
    print("\nDomaine de definition: DF = R = ]-inf, +inf[ ")
    # calculer les limites aux bornes de DF
    if(a > 0):
        limitG = "-inf"
        limitD = "+inf"
        signeA = ">"
        sensVar = "croissante"
    elif(a < 0):
        limitG = "+inf"
        limitD = "-inf"
        signeA = "<"
        sensVar = "decroissante"
    print("\nlim f(-inf) = {} ; lim f(+inf) = {} ".format(limitG, limitD)) 
    # determiner la derivee de f(x)
    print("\nla derivee f'(x) = {} ".format(a))

    # equation de la tangente en un point
    print("\nRappel equation tangenge en a: y = f'(a)(x - a) + f(a) ")
    print("Remarque: \n- Quelque soit la valeur de x choisi, \
        \n- l'equation de la tangente d'une fonction affine est egale a la fonction affine elle meme \
        \n- Exemple: f(x) = 2x + 3, Equation tangente: y = 2x + 3 ")

    # sens de variation
    print("\nRappel sens de variation: \n- si f'(x) > 0 alors f(x) est croissante sur DF ")
    print("- si f'(x) < 0 alors f(x) est decroissante sur DF ")
    print("\nSens variation: Puisque f'(x) {} 0 alors f(x) est {} sur DF ".format(signeA, sensVar))
    print("|------------------------------------------------|")
    print("|  x   |-inf                                 +inf|")
    print("|------|-----------------------------------------|")
    print("|f'(x) |                     {}                   |".format(signeA))
    print("|------------------------------------------------|")

if(choix == 2):
    print("Vous allez maintenant entrer les informations a, b et c \n")
    a = int(input("Entrez la valeur de 'a' "))
    b = int(input("Entrez la valeur de 'b' "))
    c = int(input("Entrez la valeur de 'c' "))
    # test des signes de b et c pour correct affichage
    if(b < 0):
        signeB = "-"
    elif(b > 0):
        signeB = "+"
    
    if(c < 0):
        signeC = "-"
    elif(c > 0):
        signeC = "+"

    # reduire b et c a leur valeur absolue pour affichage
    bAffich = abs(b)
    cAffich = abs(c)

    # afficher la fonction de l'utilisateur 
    if(b != 0 and c != 0):
        print("\nVotre fonction est: f(x) = {}x2 {} {}x {} {} ".format(a, signeB, bAffich, signeC, cAffich))
    elif(b == 0):
        print("\nVotre fonction est: f(x) = {}x2 {} {} ".format(a, signeC, cAffich))
    elif(c == 0):
        print("\nVotre fonction est: f(x) = {}x2 {} {}x ".format(a, signeB, bAffich))
    elif(b == 0 and c ==0):
        print("\nVotre fonction est: f(x) = {}x2 ".format(a))

    # afficher le domaine de definition
    print("\nDomaine de definition: DF = R = ]-inf, +inf[ ")

    # calculer les limites aux bornes de DF
    if(a > 0):
        limitG = "+inf"
        limitD = "+inf"
    elif(a < 0):
        limitG = "-inf"
        limitD = "-inf"
    print("\nlim f(-inf) = {} ; lim f(+inf) = {} ".format(limitG, limitD))

    # determiner la derivee de f(x)
    derivee = 2 * a  # coeff dir
    if(b != 0):
        print("\nla derivee f'(x) = {}x {} {} ".format(derivee, signeB, bAffich))
    elif(b == 0):
        print("\nla derivee f'(x) = {}x ".format(derivee))

    # equation de la tangente en un point
    tang = int(input("\nEntrez la valeur pour laquelle vous souhaitez une equation de tangente: "))
    print("\nRappel equation tangenge en a: y = f'(a)(x - a) + f(a) ")
    # calcul f'(a) et f(a)
    fprimA = fA = 0 
    fA = (a * (tang * tang)) + (b * tang) + c
    fprimA = (derivee * tang) + b
    print("f'({}) = {} et f({}) = {} ".format(tang, fprimA, tang, fA))
    constY = (((-1) * tang) * fprimA) + fA
    if(constY < 0):
        signeConstY = "-"
    elif(constY > 0):
        signeConstY = "+"
    constYAff = abs(constY)
    # affichage tangente
    if(constY != 0):
        print("Tangente a f(x) en {}: y = {}x {} {} ".format(tang, fprimA, signeConstY, constYAff))
    elif(constY == 0):
        print("Tangente a f(x) en {}: y = {}x ".format(tang, fprimA))

    # calcul de la valeur qui annule la derivee
    deriveeNull = ((-1)*b)/derivee

    # sens de variation
    print("\nRappel sens de variation: \n- Puisque derivee sous la forme f'(x) = ax + b ")
    print("1. Trouver la valeur de x pour laquelle f'(x) = 0. Donc resoudre f'(x) = 0 ")
    print("2. Observer le signe du coefficient directeur de f'(x) coeffDir ")
    print("3. Si coeffDir < 0 alors f'(x) positive sur ]-inf, x] et negative sur [x, +inf[ ")
    print("4. Si coeffDir > 0 alors f'(x) negative sur ]-inf, x] et positive sur [x, +inf[ ")
    print("Note: \n- positive ===> croissante; negative ====> decroissante")

    if(derivee > 0):
        sensVarG = ["negative", "decroissante", "-"]
        sensVarD = ["positive", "croissante", "+"]
    elif(derivee < 0):
        sensVarG = ["positive", "croissante", "+"]
        sensVarD = ["negative", "decroissante", "-"]
    
    print("\nSens variation: f'(x) est {} sur ]-inf, {}] et {} sur [{}, +inf[ ".format(sensVarG[0], deriveeNull, sensVarD[0], deriveeNull))
    print("Sens variation: f(x) est {} sur ]-inf, {}] et {} sur [{}, +inf[ ".format(sensVarG[1], deriveeNull, sensVarD[1], deriveeNull))

    print("|------------------------------------------------|")
    print("|  x   |-inf                {}              +inf|".format(deriveeNull))
    print("|------|-----------------------------------------|")
    print("|f'(x) |           {}         0        {}          |".format(sensVarG[2], sensVarD[2]))
    print("|------------------------------------------------|")

if(choix == 3):
    print("Pas encore resolu !!!")

if(choix == 4):
    print("Pas encore resolu !!! ")

