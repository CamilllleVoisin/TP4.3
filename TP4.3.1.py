"""
TP4.2.1
Par Camille Voisin
commencé le 27 novembre 2025
finit le 27 novembre 2025 à 15h55
"""


from enum import Enum
import random as rd


def jetdes():
    lancerdes = [rd.randint(1, 6) for i in range(4)]
    lancerdes.sort(reverse=True)
    #print(f"lancer des decroissant: {lancerdes}")
    trois_grands_lancers = lancerdes[0:3]
    #print(f"Les plus grands lancers : {trois_grands_lancers}")
    total_trois_grands_lancers = lancerdes[0] + lancerdes[1] + lancerdes[2]
    #print(f"Le total des trois jets est : {total_trois_grands_lancers}")
    return sum(trois_grands_lancers)

jetCA = rd.randint(1, 12)
nom_possible = ["Bob", "Bobby", "Robert", "Jean-bob", "Rafael"]
nom_choisi = rd.choice(nom_possible)
race_possible = ["Tieflin", "Nain", "Humain", "Gnome", "Elf", "Dragonborn"]
race_choisie = rd.choice(race_possible)
#proffession_possibles = ["Rogue", "Barde", "Guerrier", "Mage", "Noble", "ranger"]
#proffession_choisie = rd.choice(proffession_possibles)
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


class alignement(Enum):
    LAWFUL_GOOD = 0
    LAWFUL_NEUTRAL = 1
    LAWFUL_EVIL = 2
    NEUTRAL_GOOD = 3
    NEUTRAL = 4
    NEUTRAL_EVIL = 5
    CHAOTIC_GOOD = 6
    CHAOTIC_NEUTRAL = 7
    CHAOTIC_EVIL = 8
    SANS_ALIGNEMENT = 9



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
        self.align = alignement.SANS_ALIGNEMENT


npc1 = NPCDND(rd.randint(1, 20))
print(f"Votre alignement est : {npc1.align}")


print(f"La force du NPC est : {npc1.force}, sa constitution est de {npc1.const}, sa dexterité est de {npc1.dex},"
      f" son intelligence est de {npc1.intel}, sa sagesse est de {npc1.sage}, son charisme est de : {npc1.char},"
      f" sa AC est de : {npc1.ca}. \nSon nom est {npc1.nom}, sa race est : {npc1.race}"
      f" et son espèce est : {npc1.espece}. Le NPC est un : {npc1.profession}. Il a {npc1.vie} PV.")

class Hero(NPCDND):
    def __init__(self, hp):
        super().__init__(hp)
        self.raceh = race()
        self.nom = nom_perso()
        #print(f"{self.raceh}")
        self.espece = specification_race( self.raceh)
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



monstre = Kobold("Kobold", rd.randint(1, 20))

print(f"\nUn monstre vous attaque! C'est un {monstre.tm}.\nIl a {monstre.vie} PV en plus d'avoir une CA de {monstre.ca}!"
      f" Attention! Il t'attaque!")

"""while hero.vie or monstre.vie > 0:
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
            exit()
    elif kobold_attackroll == 20:
        hero_damage_taken = 2*rd.randint(1, 6)
        hero.vie -= hero_damage_taken
        print(
            f"Le kobold fait un coup critique : vous perdez {hero_damage_taken} PV. Vous avez maintenant {hero.vie} PV")
        if hero.vie <= 0:
            print(f"Le hero a pris une attaque fatale et est mort. RIP {hero.nom}. Vous avez échoué a votre mission.")
            exit()


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
            exit()
    elif hero_attackroll == 20:
        kobold_damage_taken = 2*rd.randint(1,6)
        monstre.vie -= kobold_damage_taken
        print(
            f"Vous infligez un coup critique! Le kobold perd {kobold_damage_taken} PV. Il a maintenant {monstre.vie} PV")
        if monstre.vie <= 0:
            print("Le kobold est mort! vous avez triomphé du combat, votre mission est maintenant finie.")
            exit()
"""