"""
TP4.2.1
Par Camille Voisin
commencé le 10 octobre 2025
finit le
"""

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

droppable_items = ["Épée courte", "Dague", "Pièce d'or", "Armure de cuir", "Cuir de kobold", "Corne de kobold"]
dropped_items = [rd.choice(droppable_items), rd.choice(droppable_items), rd.choice(droppable_items)]


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





def capacsac():
    print(f"\nLe Kobold a droppé {dropped_items}!")
    choix = input("Voulez vous ajouter des items ou retirer des items de votre sac?\nAjouter\nRetirer\n")
    capac = ["10 Pièce d'or", "Livre Saint", "Flasque", "Ration"]
    if choix == "Ajouter":
        if len(capac) >= 5:
            print("Vous n'avez plus de place dans votre sac!")
        add_item = input("Quel item voulez vous ajouter a votre sac?\n")
        search_object = add_item
        if search_object in dropped_items:
            capac.append(add_item)
            dropped_items.remove(add_item)
        else:
            print("Erreur! Vous ne pouvez pas faire ça!")
            capac.remove(add_item)
            capacsac()
    elif choix == "Retirer":
        item_a_retirer = input("Quel item voulez vous retirer?\n")
        if item_a_retirer in capac:
            capac.remove(item_a_retirer)
    print(f"Votre sac contient maintenant : {capac}")

    return capac

@dataclass
class ITEM:
    def __init__(self):
        self.bag = []
        self.add_item = input("")
        self.bag.append(self.add_item)
        print(self.bag)



item = ITEM()


"""    def add_item():
        bag = []
        item = input("\nQuel est l'item que vous voulez ajouter?\n")
        bag.append(item)
        print(f"Votre sac contient maintenant : {bag}")
"""


# jetdes()
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


class sac():
    def __init__(self):
        self.capacite = capacsac()


monstre = Kobold("Kobold", rd.randint(1, 20))

print(
    f"\nUn monstre vous attaque! C'est un {monstre.tm}.\nIl a {monstre.vie} PV en plus d'avoir une CA de {monstre.ca}!"
    f" Attention! Il t'attaque!")


def combat():
    while monstre.vie > 0 or hero.vie > 0:
        print("\nLe kobold vous attaque!!")
        kobold_attackroll = rd.randint(1, 20)
        if kobold_attackroll == 1:
            attack_kobold = "Fail"
            hero_damage_taken = 0
            hero.vie -= 0
            print(f"L'attaque du Kobold est un {attack_kobold}! Vous prenez {hero_damage_taken} dégats.")
        elif kobold_attackroll < hero.ca and kobold_attackroll > 1:
            print("Le kobold manque son coup! À vous de répliquer.")
        elif kobold_attackroll >= hero.ca and kobold_attackroll < 20:
            hero_damage_taken = rd.randint(1, 6)
            hero.vie -= hero_damage_taken
            if hero.vie < 0:
                hero.vie = 0
            print(
                f"Le kobold fait une attaque : vous perdez {hero_damage_taken} PV. Vous avez maintenant {hero.vie} PV")
            if hero.vie <= 0:
                print(f"{hero.nom} est mort, vous avez perdu!")
        elif kobold_attackroll == 20:
            hero_damage_taken = 2 * rd.randint(1, 6)
            hero.vie -= hero_damage_taken
            print(
                f"Le kobold fait un coup critique : vous perdez {hero_damage_taken} PV. Vous avez maintenant {hero.vie} PV")
            if hero.vie <= 0:
                print(
                    f"Le hero a pris une attaque fatale et est mort. RIP {hero.nom}. Vous avez échoué a votre mission.")

        print("\nVous répliquez à l'attaque du kobold.")
        hero_attackroll = rd.randint(1, 20)
        if hero_attackroll == 1:
            attack_hero = "Fail"
            kobold_damage_taken = 0
            monstre.vie -= 0
            print(f"Votre attaque est un {attack_hero}. Le kobold prend {kobold_damage_taken} dégats.")
        elif hero_attackroll < monstre.ca and hero_attackroll > 1:
            print("Vous ratez votre coup! Le Kobold réplique!")
        elif hero_attackroll >= monstre.ca and hero_attackroll < 20:
            kobold_damage_taken = rd.randint(1, 6)
            monstre.vie -= kobold_damage_taken
            if monstre.vie < 0:
                monstre.vie = 0
            print(f"Vous avez touché le kobold! Il prend {kobold_damage_taken} dégats. Il lui reste {monstre.vie} PV.")
            if monstre.vie <= 0:
                print("Le kobold est mort! vous avez triomphé du combat, votre mission est maintenant finie.")
                print(f"Il a droppé {dropped_items}!")
        elif hero_attackroll == 20:
            kobold_damage_taken = 2 * rd.randint(1, 6)
            monstre.vie -= kobold_damage_taken
            print(
                f"Vous infligez un coup critique! Le kobold perd {kobold_damage_taken} PV. Il a maintenant {monstre.vie} PV")
            if monstre.vie <= 0:
                print("Le kobold est mort! vous avez triomphé du combat, votre mission est maintenant finie.")
                print(f"Il a droppé {dropped_items}!")
def next():
    next_step = input("Voulez vous ajouter des items dans votre sac?\n")
    if next_step == "Oui" or "oui":
        item.add_item = input("Quel est l'item que vous voulez ajouter?\n")
        search_object = item.add_item
        if search_object in dropped_items:
            item.bag.append(item.add_item)
            dropped_items.remove(item.add_item)
        else:
            print("Erreur! Vous ne pouvez pas faire ça!")
            item.bag.remove(item.add_item)
        item.bag.append(item.add_item)
        print(item.bag)
    elif next_step == "Non" or "non":
        print("Vous allez refaire des combats.")
        combat()


combat()
#capacsac()
"""add_more_items = input("Voulez vous ajouter d'autres objets a votre sac?\nOui\nNon\n")
if add_more_items == "Oui" or "oui":
    next()
elif add_more_items == "Non" or "non":
    faire_autre_combat = input("Voulez vous refaire des combats?\nOui\nNon\n")
    if faire_autre_combat == "Oui":
        print("Vous recommencez à faire des combats.")
        combat()
    elif faire_autre_combat == "Non":
        print("Vous quittez le jeu.")
        exit()"""

next()
