reponse_menu = 0
noises = 0
mornilles = 0
gallions = 0

liste = [0, 0, 0, 0, 0, 0, 0, 0, 0]
liste_billet = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def rendre_argent_1(somme):
    """
    Cette fonction sert à rendre la monnaie en un minimum de billets.
    ENTREE: Valeur à rendre
    Sortie: Liste énumérant les billets nécessaire pour faire la monnaie.
    """
    somme_reste = 0
    liste = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if somme <= 0:
        print(f"Il m'est impossible de vous rendre la monnaie de {somme}€ !")
    else:
        somme_reste = somme
        print(f"Pour {somme}, il faut vous rendre :")
        for i in range(len(liste_billet)):
            while somme_reste >= liste_billet[i]:
                somme_reste = somme_reste - liste_billet[i]
                liste[i] = liste[i] + 1
            if liste[i] > 0:
                print(f"{liste[i]} billets de {liste_billet[i]} euros,")
    return(' ')

caisse = [200, 100, 100, 100, 50, 20, 10, 2, 2, 2, 2, 2]


def rendu_limite(rendu_demande, caisse):
    """
    Cette fonction permet de rendre la monnaie à partir d'une caisse limitée.
    Le rendu de monnaie n'est pas toujours exact, mais est optimal avec les
    options limitées que l'on a.
    ENTREE: Valeur à rendre, et liste contenant les billets disponibles.
    SORTIE: Liste contenant les billets à rendre
    """
    rendu_reste = rendu_demande
    monnaie_a_rendre = []
    for i in range(len(caisse)):
        if rendu_reste - caisse[i] >= 0:
            monnaie_a_rendre.append(caisse[i])
            rendu_reste -= caisse[i]
    if rendu_reste != 0:
        print(f"Nous ne pourrons pas rendre la totalité des {rendu_demande}€ demandés, "
              f"il manque {rendu_reste} euros à vous rendre")
    for valeur in monnaie_a_rendre[:]:
        if monnaie_a_rendre.count(valeur) != 0:
            print(f"On va vous rendre {monnaie_a_rendre.count(valeur)} billets de {valeur}€")
        if monnaie_a_rendre.count(valeur) > 1:
            for value in monnaie_a_rendre[:]:
                if value == valeur:
                    monnaie_a_rendre.remove(value)
    print("")


def rendre_argent_2(noises, mornilles, gallions):
    """
Cette fonction sert à retransformer les quantités de gallions, mornilles et noises,
     en un nombre minimal de gallions, mornilles, et noises.

    ENTREE: Quantité à rendre sous la forme de gallions, mornilles et noises.
    -->Transformation des quantités des 3 monnaies en noises uniquement,
    afin de simplifier les calculs futurs.
    SORTIE: Quantité totale à rendre, transformée en gallions, mornilles et noises.
    """
    somme_rendre_totale = noises + (29 * mornilles) + (17 * 29 * gallions)
    if somme_rendre_totale < 0:
        print("Ce n'est pas possible ça :)")
    else:
        somme_reste = somme_rendre_totale

        quantite_gallion = 0
        quantite_gallion = quantite_gallion + (somme_reste // (29 * 17))
        print(f"Pour rendre {gallions} gallions, "\
              f"{mornilles} mornilles, et {noises} noises :")
        print(f"-Il faut rendre {quantite_gallion} gallions.")
        somme_reste = somme_reste - (quantite_gallion * 29 * 17)

        quantite_mornille = 0
        quantite_mornille = quantite_mornille + (somme_reste // (29))
        print(f"-Il faut rendre {quantite_mornille} mornilles.")
        somme_reste = somme_reste - (quantite_mornille * 29)
        print(f"-Il faut rendre {somme_reste} noises.")
        somme_reste = 0
        print("")


def fleury_et_bott():
    """
    IHM de la partie a. : permet d'afficher les résultats de l'algorithme correspondant.
    -->fonction rendre_argent_1
    Permet également de rentrer une valeur manuellement si souhaité.
    Enfin, permet de revenir au menu principal / de quitter le programme.
    """

    print("")
    print(f"Bienvenue chez Fleury & Bott !")
    print("")
    print(rendre_argent_1(0))
    print(rendre_argent_1(60))
    print(rendre_argent_1(63))
    print(rendre_argent_1(231))
    print(rendre_argent_1(899))
    reponse_manuelle = int(input(f"Souhaites-tu entrer une valeur manuelle pour que je t'en rende la monnaie ?\n\
            Si oui, entrer 1\n\
            Si non, entrer 2 : "))
    if reponse_manuelle == 1:
        valeur_reponse = int(input("Entre la valeur souhaitée : "))
        rendre_argent_1(valeur_reponse)
    reponse_fin = int(input(f"Souhaites-tu revenir au menu, ou bien sortir du chemin de traverse ?\n\
                Pour revenir au menu, entrer 1\n\
                Pour sortir du chemin de traverse, entrer 2 :"))
    if reponse_fin == 1:
        menu_principal()
    if reponse_fin == 2:
        print("A bientôt, j'espère !")


def madame_guipure():
    """
    IHM de la partie b. : permet d'afficher les résultats de l'algorithme correspondant.
    -->fonction rendu_limite
    Permet également de rentrer une valeur manuellement si souhaité.
    Enfin, permet de revenir au menu principal / de quitter le programme.
    """
    print("Bienvenue chez Madame Guipure !")
    rendu_limite(0, caisse)
    rendu_limite(8, caisse)
    rendu_limite(62, caisse)
    rendu_limite(231, caisse)
    rendu_limite(497, caisse)
    rendu_limite(842, caisse)
    reponse_manuelle_2 = int(input(f"Souhaites-tu entrer une valeur manuelle pour que je t'en rende la monnaie ?\n\
            Si oui, entrer 1\n\
            Si non, entrer 2 : "))
    if reponse_manuelle_2 == 1:
        valeur_reponse_2 = int(input("Entre la valeur souhaitée : "))
        rendu_limite(valeur_reponse_2, caisse)
    reponse_fin = int(input(f"Souhaites-tu revenir au menu, ou bien sortir du chemin de traverse ?\n\
                Pour revenir au menu, entrer 1\n\
                Pour sortir du chemin de traverse, entrer 2 :"))
    if reponse_fin == 1:
        menu_principal()
    if reponse_fin == 2:
        print("A bientôt, j'espère !")


def ollivander():
    """
    IHM de la partie c. : permet d'afficher les résultats de l'algorithme correspondant.
    --> rendre_argent_2
    Permet également de rentrer des valeurs manuellement si souhaité.
    Enfin, permet de revenir au menu principal / de quitter le programme.
    """
    print(f"Bienvenue chez Ollivander !")
    rendre_argent_2(0, 0, 0)
    rendre_argent_2(654, 0, 0)
    rendre_argent_2(78, 23, 0)
    rendre_argent_2(9, 11, 2)
    rendre_argent_2(451, 531, 7)

    reponse_manuelle_3 = int(input(f"Souhaites-tu entrer une valeur manuelle pour que je t'en rende la monnaie ?\n\
            Si oui, entrer 1\n\
            Si non, entrer 2 : "))
    if reponse_manuelle_3 == 1:
        valeur_noises = int(input("Entre la valeur souhaitée de noises: "))
        valeur_mornilles = int(input("Entre la valeur souhaitée de mornilles: "))
        valeur_gallions = int(input("Entre la valeur souhaitée de gallions: "))
        rendre_argent_2(valeur_noises, valeur_mornilles, valeur_gallions)
    reponse_fin = int(input(f"Souhaites-tu revenir au menu, ou bien sortir du chemin de traverse ?\n\
                Pour revenir au menu, entrer 1\n\
                Pour sortir du chemin de traverse, entrer 2 :"))
    if reponse_fin == 1:
        menu_principal()
    if reponse_fin == 2:
        print("A bientôt, j'espère !")


def menu_principal():
    """
    IHM du menu principal, choix du magasin.
    Permet de déclencher le code de chaque magasin.
    """
    reponse_menu = int(input("Dans quel magasin souhaites-tu rentrer ?\n\
            Pour entrer chez Fleury & Bott, entrer 1\n\
            Pour entrer chez Madame Guipure, entrer 2\n\
            Pour entrer Chez Mr. Ollivander, entrer 3 : "))
    if reponse_menu == 1:
        fleury_et_bott()
    elif reponse_menu == 2:
        print(madame_guipure())
    elif reponse_menu == 3:
        ollivander()
    else:
        print('Merci de choisir un magasin !')
        menu_principal()

print(f"Bienvenue dans le chemin de Traverse !")
menu_principal()