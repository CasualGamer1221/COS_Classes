# Task 1
import random


def weapon():
    weaponlist = ("Club", "Longsword", "Rapier", "Shortbow", "Dagger")
    weaponchosen = random.choice(weaponlist)
    return weaponchosen


def damagevalues():
    mindamage = 0
    maxdamage = 0 
    number1 = random.randrange(1000)
    number2 = random.randrange(1000)
    if number1 < number2:
        mindamage = number1
        maxdamage = number2
    else:
        maxdamage = number1
        mindamage = number2

    return mindamage, maxdamage


def randomadjective():
    adjectivelist = ("abandoned", "accurate", "advanced", "alarming", "crooked", " cool", "dazzling", "decent", "shiny", "deficient", "delayed", "dependent", "diligent", "disfigured", "dull",
                     "enormous", "exotic", "excellent", "fantastic", "fitting", "focused", "fumbling", "grandiose", "hidden", "horrible", "ideal", "illegal", "impeccable", "impractical", "infamous",
                     "inferior", "ironclad", "lavish", "lazy", "loud", "little", "luxurious", "menacing", "puny", "precious", "powerful", "ruddy", "rundown", "repulsive", "scary", "sentimental",
                     "slight", "sparklingviolent", "weak")
    adjectivechoice = random.choice(adjectivelist)
    adjectivechoice2 = random.choice(adjectivelist)
    adjectivechoice = adjectivechoice.title()
    adjectivechoice2 = adjectivechoice2.title()
    return adjectivechoice , adjectivechoice2


weaponchosen = weapon()
mindamage , maxdamage = damagevalues()
adjectivechoice , adjectivechoice2 = randomadjective()
