"""
TP4.2.1
Par Camille Voisin
commencé le 10 octobre 2025
finit le 3 Décembre 2025
"""

from enum import Enum
import random as rd
from dataclasses import dataclass

def jetdes():
    lancerdes = [rd.randint(1, 6) for i in range(4)]
    lancerdes.sort(reverse=True)
    trois_grands_lancers = lancerdes[0:3]
    total_trois_grands_lancers = lancerdes[0] + lancerdes[1] + lancerdes[2]
    return sum(trois_grands_lancers)


jetCA = rd.randint(1, 12)
nom_possible = ["Bob", "Bobby", "Robert", "Jean-bob", "Rafael"]
nom_choisi = rd.choice(nom_possible)
race_possible = ["Tieflin", "Nain", "Humain", "Gnome", "Elf", "Dragonborn"]
race_choisie = rd.choice(race_possible)



def race():
    race_possible = ["Tieflin", "Nain", "Humain", "Gnome", "Elf", "Dragonborn"]
    race_choisie = rd.choice(race_possible)
    return race_choisie


def nom_perso():
    nom_possible = ["Bob", "Bobby", "Robert", "Jean-bob", "Rafael"]
    nom_choisi = rd.choice(nom_possible)
    return nom_choisi


def specification_race(race_selectionnee):
    espece = "invalide"
    if race_selectionnee == "Tieflin":
        choix_espece = rd.randint(1, 3)
        if choix_espece == 1:
            espece = "Abyssal"
        elif choix_espece == 2:
            espece = "Chtonic"
        elif choix_espece == 3:
            espece = "Infernal"
    elif race_selectionnee == "Nain":
        choix_espece = rd.randint(1, 2)
        if choix_espece == 1:
            espece = "Nain des montagnes"
        elif choix_espece == 2:
            espece = "Nain gris"
    elif race_selectionnee == "Humain":
        choix_espece = rd.randint(1, 2)
        if choix_espece == 1:
            espece = "Blanc"
        elif choix_espece == 2:
            espece = "Noir"
    elif race_selectionnee == "Gnome":
        if nom_choisi == "Raphael":
            espece = "Psycopath malade mental qui tue des pingouins"
        else:
            choix_espece = rd.randint(1, 3)
            if choix_espece == 1:
                espece = "Gnome des prairies"
            elif choix_espece == 2:
                espece = "Gnome des forets"
            elif choix_espece == 3:
                espece = "Gnome des montagnes"
    elif race_selectionnee == "Elf":
        choix_espece = rd.randint(1, 5)
        if choix_espece == 1:
            espece = "Elf normal"
        elif choix_espece == 2:
            espece = "Elf Sylvestre"
        elif choix_espece == 3:
            espece = "Elf des montagnes"
        elif choix_espece == 4:
            espece = "Elf Noir"
        elif choix_espece == 5:
            espece = "Haut Elf"
    elif race_selectionnee == "Dragonborn":
        choix_espece = rd.randint(1, 10)
        if choix_espece == 1:
            espece = "Brass"
        elif choix_espece == 2:
            espece = "Bronze"
        elif choix_espece == 3:
            espece = "Copper"
        elif choix_espece == 4:
            espece = "Gold"
        elif choix_espece == 5:
            espece = "Silver"
        elif choix_espece == 6:
            espece = "Black"
        elif choix_espece == 7:
            espece = "Blue"
        elif choix_espece == 8:
            espece = "Green"
        elif choix_espece == 9:
            espece = "Red"
        elif choix_espece == 10:
            espece = "White"
    return espece


def specif_prof():
    profession_possibles = ["Rogue", "Barde", "Guerrier", "Mage", "Noble", "Ranger"]
    profession_choisie = rd.choice(profession_possibles)
    return profession_choisie

jetdes()
class NPCDND:
    def __init__(self, hp):
        self.force = jetdes()
        self.const = jetdes()
        self.dex = jetdes()
        self.intel = jetdes()
        self.sage = jetdes()
        self.char = jetdes()
        self.ca = jetCA
        self.nom = nom_perso()
        self.race = race()
        self.espece = specification_race(self.race)
        self.profession = specif_prof()
        self.vie = hp


npc1 = NPCDND(rd.randint(1, 20))
print(f"La force du NPC est : {npc1.force}, sa constitution est de {npc1.const}, sa dexterité est de {npc1.dex},"
      f" son intelligence est de {npc1.intel}, sa sagesse est de {npc1.sage}, son charisme est de : {npc1.char},"
      f" sa AC est de : {npc1.ca}. \nSon nom est {npc1.nom}, sa race est : {npc1.race}"
      f" et son espèce est : {npc1.espece}. Le NPC est un : {npc1.profession}. Il a {npc1.vie} PV.")


class Hero(NPCDND):

    def __init__(self, hp):
        super().__init__(hp)
        self.raceh = race()
        self.nom = nom_perso()
        # print(f"{self.raceh}")
        self.espece = specification_race(self.raceh)
        self.vie = hp



hero = Hero(rd.randint(1, 20))




print(f"Voici les stats du Hero : La force du Hero est : {hero.force}, sa constitution est de {hero.const},"
      f" sa dexterité est de {hero.dex},son intelligence est de {hero.intel}, sa sagesse est de {hero.sage},"
      f" son charisme est de : {hero.char}, sa AC est de : {hero.ca}."
      f" \nSon nom est {hero.nom}, sa race est : {hero.raceh}"
      f" et son espèce est : {hero.espece}. Le NPC est un : {hero.profession}. Il a {hero.vie} PV.")


class Kobold(NPCDND):
    def __init__(self, type_de_monstre, hp):
        super().__init__(type_de_monstre)
        self.tm = type_de_monstre
        self.vie = hp


@dataclass
class Item:
    nom: str
    qte: int

    def __eq__(self, other):
        if self.nom == other.nom:
            return True


class Sac:
    def __init__(self):
        #self.capacite = capacsac()
        self.contenu = []

    def ajouter(self, item_ajouter: Item):
        for item in self.contenu:
            if item.nom == item_ajouter.nom:
                item.qte += item_ajouter.qte
                return
        self.contenu.append(item_ajouter)


    def retirer(self, item_enlever: Item):
        for item in self.contenu:
            if item.nom == item_enlever.nom:
                if item.qte - item_enlever.qte == 0:
                    self.contenu.remove(item)
                    print(item.qte)
                    return
                elif item.qte - item_enlever.qte > 0:
                    print("Action possible")
                    return
                elif item.qte - item_enlever.qte < 0:
                    print(f"Impossible de retirer {item_enlever.qte} de '{item_enlever.nom}'")
                    return
                item.qte -= item_enlever.qte
        print(f"Impossible, l'item '{item_enlever}' n'est pas dans le sac")###

s = Sac()
s.ajouter(Item("or", 5))
s.ajouter(Item("or", 5))
s.ajouter(Item("Peluche de kobold", 1))
s.ajouter(Item("argent", 50))
print(s.contenu)
s.retirer(Item("or", 9))
s.retirer(Item("argent", 45))
s.retirer(Item("argene3333t", 45))
#s.retirer(Item("Téléphone", 4))
print(s.contenu)

def action_avec_sac():
    interaction_avec_sac = int(input("Que voulez vous faire?\n 1 -Ajouter des items a votre sac\n 2 -Retirer des items de votre sac\n"))
    if interaction_avec_sac == 1:
        nom_objet  = input("Quel est l'item que vous voulez ajouter?\n")
        quantite = int(input("Quelle est la quantité d'objet que vous voulez ajouter?\n"))
        s.contenu.append(Item(nom_objet, quantite))
        print(s.contenu)
        ajouter_autres_items = input("Voulez vous faire d'autre action avec le sac?\n -Oui\n -Non\n")
        if ajouter_autres_items == "Oui":
            action_avec_sac()
        elif ajouter_autres_items == "Non":
            print("Vous quittez le code...")
            print ("Exiting...\nPlease don't turn off PC when the code is closing...\nCode closed")
    elif interaction_avec_sac == 2:
        nom_objet = input("Quel est l'item que vous voulez retirer?\n")
        quantite = int(input("Quelle est la quantité d'objet que vous voulez retirer?\n"))
        item_a_verifier = Item(nom_objet, quantite)
        if item_a_verifier in s.contenu:
            print("L'item est dans le sac, vous pouvez le retirer")
            for item in s.contenu:
                if item.nom == item_a_verifier.nom:
                    pass
        else:
            print("L'item que vous voulez retirer n'est pas dans le sac.")
            exit()
        s.contenu.remove(Item(nom_objet, quantite))
        print(s)
        ajouter_autres_items = input("Voulez vous faire d'aurtes actions avec le sac?\n -Oui\n -Non\n")
        if ajouter_autres_items == "Oui":
            action_avec_sac()
        elif ajouter_autres_items == "Non":
            print("Vous quittez le code...")
            print("Exiting...\nPlease don't turn off PC when the code is closing...\nCode closed")
    return s

#action_avec_sac()

#print(s.contenu)
#s.retirer(Item("Pièce or", 3))

#print(s.contenu)


# monstre = Kobold("Kobold", rd.randint(1, 20))
#
# print(
#     f"\nUn monstre vous attaque! C'est un {monstre.tm}.\nIl a {monstre.vie} PV en plus d'avoir une CA de {monstre.ca}!"
#     f" Attention! Il t'attaque!")
#
#
# def combat():
#     while monstre.vie > 0 or hero.vie > 0:
#         print("\nLe kobold vous attaque!!")
#         kobold_attackroll = rd.randint(1, 20)
#         if kobold_attackroll == 1:
#             attack_kobold = "Fail"
#             hero_damage_taken = 0
#             hero.vie -= 0
#             print(f"L'attaque du Kobold est un {attack_kobold}! Vous prenez {hero_damage_taken} dégats.")
#         elif kobold_attackroll < hero.ca and kobold_attackroll > 1:
#             print("Le kobold manque son coup! À vous de répliquer.")
#         elif kobold_attackroll >= hero.ca and kobold_attackroll < 20:
#             hero_damage_taken = rd.randint(1, 6)
#             hero.vie -= hero_damage_taken
#             if hero.vie < 0:
#                 hero.vie = 0
#             print(
#                 f"Le kobold fait une attaque : vous perdez {hero_damage_taken} PV. Vous avez maintenant {hero.vie} PV")
#             if hero.vie <= 0:
#                 print(f"{hero.nom} est mort, vous avez perdu!")
#         elif kobold_attackroll == 20:
#             hero_damage_taken = 2 * rd.randint(1, 6)
#             hero.vie -= hero_damage_taken
#             print(
#                 f"Le kobold fait un coup critique : vous perdez {hero_damage_taken} PV. Vous avez maintenant {hero.vie} PV")
#             if hero.vie <= 0:
#                 print(
#                     f"Le hero a pris une attaque fatale et est mort. RIP {hero.nom}. Vous avez échoué a votre mission.")
#
#         print("\nVous répliquez à l'attaque du kobold.")
#         hero_attackroll = rd.randint(1, 20)
#         if hero_attackroll == 1:
#             attack_hero = "Fail"
#             kobold_damage_taken = 0
#             monstre.vie -= 0
#             print(f"Votre attaque est un {attack_hero}. Le kobold prend {kobold_damage_taken} dégats.")
#         elif hero_attackroll < monstre.ca and hero_attackroll > 1:
#             print("Vous ratez votre coup! Le Kobold réplique!")
#         elif hero_attackroll >= monstre.ca and hero_attackroll < 20:
#             kobold_damage_taken = rd.randint(1, 6)
#             monstre.vie -= kobold_damage_taken
#             if monstre.vie < 0:
#                 monstre.vie = 0
#             print(f"Vous avez touché le kobold! Il prend {kobold_damage_taken} dégats. Il lui reste {monstre.vie} PV.")
#             if monstre.vie <= 0:
#                 print("Le kobold est mort! vous avez triomphé du combat, votre mission est maintenant finie.")
#                 print(f"Il a droppé {dropped_items}!")
#         elif hero_attackroll == 20:
#             kobold_damage_taken = 2 * rd.randint(1, 6)
#             monstre.vie -= kobold_damage_taken
#             print(
#                 f"Vous infligez un coup critique! Le kobold perd {kobold_damage_taken} PV. Il a maintenant {monstre.vie} PV")
#             if monstre.vie <= 0:
#                 print("Le kobold est mort! vous avez triomphé du combat, votre mission est maintenant finie.")
#                 print(f"Il a droppé {dropped_items}!")
#     return combat()
# def next():
#     next_step = input("Voulez vous ajouter des items dans votre sac?\n")
#     if next_step == "Oui" or "oui":
#         item.add_item = input("Quel est l'item que vous voulez ajouter?\n")
#         search_object = item.add_item
#         if search_object in dropped_items:
#             item.bag.append(item.add_item)
#             dropped_items.remove(item.add_item)
#         else:
#             print("Erreur! Vous ne pouvez pas faire ça!")
#             item.bag.remove(item.add_item)
#         item.bag.append(item.add_item)
#         print(item.bag)
#     elif next_step == "Non" or "non":
#         print("Vous allez refaire des combats.")
#         combat()
#     return next_step
#
# combat()
# next()
# #capacsac()
# """add_more_items = input("Voulez vous ajouter d'autres objets a votre sac?\nOui\nNon\n")
# if add_more_items == "Oui" or "oui":
#     next()
# elif add_more_items == "Non" or "non":
#     faire_autre_combat = input("Voulez vous refaire des combats?\nOui\nNon\n")
#     if faire_autre_combat == "Oui":
#         print("Vous recommencez à faire des combats.")
#         combat()
#     elif faire_autre_combat == "Non":
#         print("Vous quittez le jeu.")
#         exit()"""
#
# next()
