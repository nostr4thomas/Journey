import math
import random
import time

### Battle Function ###
def battle(Stats, EnemyStats):
    PlayerHealth = Stats[0]
    PlayerAttack = Stats[1]
    #PlayerSneak = Stats[2]
    EnemyHealth = EnemyStats[0]
    EnemyAttack = EnemyStats[1]
    EnemyName = EnemyStats[2]
    pointChoice = 0
    print("The battle has begun!")
    input()
    #continue loop until player dies or enemy dies
    while PlayerHealth > 0 and EnemyHealth > 0:
        randomint = random.randint(1, 10)
        #player attacks
        if randomint >= 5:
            print("You successfully attack the", EnemyName, "!")
            EnemyHealth -= PlayerAttack
            print("You did", PlayerAttack, "damage.")
            if EnemyHealth <= 0:
                EnemyHealth == 0
            print("The", EnemyName,"has", EnemyHealth, "health left.")
            input()
        #enemy attacks
        elif randomint < 5:
            print("The", EnemyName, "successfully attacks you!")
            PlayerHealth -= EnemyAttack
            print("They did", EnemyAttack, "damage.")
            print("You have", PlayerHealth, "health left.")
            input()
    if PlayerHealth > 0:
        print("You have defeated the", EnemyName)
        print()
        print("Would you like to consume the enemy for a Red Point or consume the resources they were guarding for a Green Point?")
        print("1: Red Point")
        print("2: Green Point")
        try:
            pointChoice = int(input("Enter 1 or 2: "))
        except ValueError:
            print("You suddenly feel compelled to consume the enemy.")
            pointChoice = 1
        while pointChoice!=1 and pointChoice!=2 and pointChoice=="":
            pointChoice = int(input("Enter 1 or 2: "))
        print()
        return pointChoice
    else:
        return 3
    pass
    return pointChoice

### Sneak Function ###
def sneak(Stats, EnemyStats):
    PlayerSneak = Stats[2]
    EnemyName = EnemyStats[2]
    randomint = random.randint(1, 100)
    print("You observe the", EnemyName, "waiting for the perfect moment to sneak past.")
    input()
    #check for successful sneak
    if PlayerSneak > randomint:
        print("You sneak past successfully!")
        print("You gain access to the resources the", EnemyName, "was guarding and gain 1 Green Point.")
        input()
        return 1
    #unsuccessful sneak attempt
    else:
        print("You are caught trying to sneak by the", EnemyName, ". Prepare for battle!")
        input()
        return 2

### Evolutionary Traits Menu ###
def shop(RedPoints, GreenPoints, Traits):
    t0 = Traits[0]
    t1 = Traits[1]
    t2 = Traits[2]
    t3 = Traits[3]
    healthIncrease = 0
    damageIncrease = 0
    sneakIncrease = 0
    print("Your current point totals are:")
    print("Red Points:", RedPoints)
    print("Green Points:", GreenPoints)
    input()
    print("The currently available evolutionary traits and their prices are:")
    TraitTable = '{trait:33}{price:10}'
    print(TraitTable.format(trait='Evolutionary Trait', price = 'Price'))
    print('-'*45)
    print(TraitTable.format(trait=t0, price="1 Green Point"))
    print(TraitTable.format(trait=t1, price="2 Red Points"))
    print(TraitTable.format(trait=t2, price="1 Red Point & 1 Green Point"))
    print(TraitTable.format(trait=t3, price="4 Red Points"))
    input()
    try:
        makePurchase = int(input("Would you like to purchase a trait and evolve? Enter 1 if yes, 2 if no: "))
    except ValueError:
        print("You lose your focus and miss you opportunity to evolve.")
        makePurchase = 2
    print()
    while makePurchase != 1 and makePurchase !=2:
        int(input("Please enter a 1 or 2: "))

    #Player chooses to make a purchase
    if makePurchase == 1:
        print("Enter 1 to purchase", t0, ". Enter 2 to purchase", t1, ". Enter 3 to purchase", t2, ". Enter 4 to purchase", t3)
        try:
            purchaseChoice = int(input("Trait to purchase: "))
        except ValueError:
            purchaseChoice = 5
        while purchaseChoice != 1 and purchaseChoice != 2 and purchaseChoice != 3 and purchaseChoice != 4 and purchaseChoice != 5:
            int(input("Please enter a 1, 2, 3 or 4: "))
        ### Trait 0 purchased or purchase failed ###
        if purchaseChoice == 1 and GreenPoints >= 1:
            print("You selected", t0, ". Your body changes and you now have 50 more health!")
            healthIncrease = 50
            input()
            GreenPoints -= 1
            print("You now have", GreenPoints, "Green Points.")
            input()
        elif purchaseChoice == 1 and GreenPoints < 1:
            print("You do not have enough Green Points.")
            input()
            print("You have missed your opportunity to evolve.")
            input()
        ### Trait 1 purchased or purchase failed ###
        if purchaseChoice == 2 and RedPoints >=2:
            print("You selected", t1, ". Your body changes and you now do 10 more damage!")
            damageIncrease = 10
            input()
            RedPoints -= 2
            print("You now have", RedPoints, "Red Points.")
            input()
        elif purchaseChoice == 2 and RedPoints < 2:
            print("You do not have enough Green Points.")
            input()
            print("You have missed your opportunity to evolve.")
            input()
        ### Trait 2 purchased or purchase failed ###
        if purchaseChoice == 3 and RedPoints >= 1 and GreenPoints >= 1:
            print("You selected", t2, ". Your body changes and you are now much sneakier!")
            sneakIncrease = 25
            input()
            RedPoints -= 1
            GreenPoints -= 1
            print("You now have", RedPoints, "Red Points and", GreenPoints, "Green Points.")
            input()
        elif purchaseChoice == 3 and RedPoints < 1 and GreenPoints >= 1:
            print("You do not have enough Red Points.")
            input()
            print("You have missed your opportunity to evolve.")
            input()
        elif purchaseChoice == 3 and RedPoints >= 1 and GreenPoints < 1:
            print("You do not have enough Green Points.")
            input()
            print("You have missed your opportunity to evolve.")
            input()
        ### Trait 3 purchased or purchase failed ###
        if purchaseChoice == 4 and RedPoints >= 4:
            print("You selected", t3, ". My god...this wasn't supposed to happen. Your body...grows a gun. You now do 100 more damage.")
            damageIncrease = 100
            input()
            RedPoints -= 4
            print("You now have", RedPoints, "Red Points.")
            input()
        elif purchaseChoice == 4 and RedPoints < 4:
            print("You do not have enough Red Points.")
            input()
            print("You have missed your opportunity to evolve.")
            input()
        if purchaseChoice == 5:
            print("You should know better than to blindly hit \"Enter\" by now. Tsk tsk.")
    #Player chooses not to make a purchase
    else:
        print("Refusing to evolve could be the end of you. Be careful!")
        input()
    return(RedPoints,GreenPoints,healthIncrease,damageIncrease,sneakIncrease)

### Encounter Function ###
def encounter(encounterChoice, Stats, EnemyStats):
    #RedPoints = Stats[3]
    #GreenPoints = Stats[4]
    RedAndGreenPoints = [0,0]
    #Player chooses to attack
    if encounterChoice == 1:
        battleOutcome = battle(Stats,EnemyStats)
        if battleOutcome == 1:
            print("You are healed by your consumption.")
            print("You gain 1 Red Point.")
            RedAndGreenPoints[0] += 1
            return RedAndGreenPoints
        elif battleOutcome == 2:
            print("You are healed by your consumption.")
            print("You gain 1 Green Point.")
            RedAndGreenPoints[1] += 1
            return RedAndGreenPoints
        else:
            gameOver = 1
    #Player chooses to attempt a sneak by
    elif encounterChoice == 2:
        sneakOutcome = sneak(Stats, EnemyStats)
        #successful sneak
        if sneakOutcome == 1:
            RedAndGreenPoints[1] += 1
            return RedAndGreenPoints
        #unsuccessful sneak, forced to fight
        else:
            battleOutcome = battle(Stats, EnemyStats)
            if battleOutcome == 1:
                print("You are healed by your consumption.")
                print("You gain 1 Red Point.")
                RedAndGreenPoints[0] += 1
                return RedAndGreenPoints
            elif battleOutcome == 2:
                print("You are healed by your consumption.")
                print("You gain 1 Green Point.")
                RedAndGreenPoints[1] += 1
                return RedAndGreenPoints
            else:
                gameOver = 1
    if gameOver == 1:
        print("You have been killed by the", EnemyStats[2])
        GAMEOVER(gameOver)

### Game over Function
def GAMEOVER(gameOver):
    GO = gameOver
    print("You lineage ends with you.")
    print("GAME OVER.")
    while GO == 1:
        input("Exit the game to try again")

### WIN Function###
def WIN():
    winner = 1
    print("The Narrator has sent you back.")
    print("The game continues.")
    while winner ==1:
        input("Exit the game to play again")
    
######################################## Beginning Player Stats #######################################
Health = 70
Attack = 10
Sneak = 30
RedPoints = 0
GreenPoints = 0
Stats = [Health, Attack, Sneak]
gameOver = 0
pointsAfterShop = []
### Start game ###
print("Now starting Your Journey")

print("     .-.    .--.    ___  ___   ___ .-.     ___ .-.     .--.    ___  ___  ")
print("    / __\  /    \  (   )(   ) (   )   \   (   )   \   /    \  (   )(   ) ")
print("    \ ''/ |  ..  |  | |  | |   | ' .-. \   |  .-. |  |  .-. |  | |  | |  ")
print("     | |  | |  | |  | |  | |   |  / (___)  | |  | |  |  | | |  | |  | |  ")
print("     | |  | |  | |  | |  | |   | |         | |  | |  |  |/  |  | '  | |  ")
print("     | |  | |  | |  | |  | |   | |         | |  | |  |  ' _.'  '  `-' |  ")
print("     | |  | |  | |  | |  ; '   | |         | |  | |  |  .'.-.   `.__. |  ")
print(" ___ | |  \  `-' /  ' `-'  /   | |         | |  | |  '  `-' /   ___ | |  ")
print("(   )' |   `.__.'    '.__.'   (___)       (___)(___)  `.__.'   (   )' |  ")
print(" ; `-' '                                                        ; `-' '  ")
print("  .__.'                                                          .__.'   ")

input("Press ENTER to begin")
######################################## Backstory and game explanation #######################################
input("Welcome to the beginning of the age of life. After millenia of you ancestors swimming in the primordial soup, now exists...YOU! (1/6)")
input("Your job is to continue the process of evolution by defeating enemies and consuming them, or forgoing the danger and consuming plants. (2/6)")
input("But beware, attempting to sneak past your foes may fail, throwing you into battle regardless of your non-confrontational ways. (3/6)")
input("Regardless, you will need to consume something to survive, earning you points used to increase your abilities by choosing evolutionary traits. (4/6)")
input("You will begin your journey in ocean. Prepare yourself for 4 tough opponents and 1 boss. (5/6)")
input("If you succeed, I will transport you forward in time to live as a distant descendant of yours. Good luck! (6/6)")
print()

######################################################## Ocean Stage ########################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ocean Enemy Stats and Evolutionary Traits  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Sea Urchin ###
SeaUrchin = "Sea Urchin"
SeaUrchinHealth = 50
SeaUrchinAttack = 4
SeaUrchinStats = [SeaUrchinHealth, SeaUrchinAttack, SeaUrchin]
### Jellyfish ###
Jellyfish = "Jellyfish"
JellyfishHealth = 60
JellyfishAttack = 6
JellyfishStats = [JellyfishHealth, JellyfishAttack, Jellyfish]
### Lionfish ###
Lionfish = "Lionfish"
LionfishHealth = 75
LionfishAttack = 8
LionfishStats = [LionfishHealth, LionfishAttack, Lionfish]
### Octopus ###
Octopus = "Octopus"
OctopusHealth = 90
OctopusAttack = 10
OctopusStats = [OctopusHealth, OctopusAttack, Octopus]
### Shark ###
Shark = "Shark"
SharkHealth = 100
SharkAttack = 15
SharkStats = [SharkHealth, SharkAttack, Shark]
### Ocean Stage Evolutionary Trait Options ###
OceanTraits = ["Improved Scales", "Shark Teeth", "Fast Fins", "A gun"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 1
### Ocean Stage Level 1: Sea Urchin ###
print("You come across a sea urchin. Would you like to (1)attack or (2)swim by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, SeaUrchinStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, OceanTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 2
### Ocean Stage Level 2: Jellyfish ###
print("You come across a jellyfish. Would you like to (1)attack or (2)swim by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, JellyfishStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, OceanTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 3
### Ocean Stage Level 3: Lionfish ###
print("You come across a lionfish. Would you like to (1)attack or (2)swim by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, LionfishStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, OceanTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 4
### Ocean Stage Level 4: Octopus ###
print("You come across an octopus. Would you like to (1)attack or (2)swim by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, OctopusStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, OceanTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 5
### Ocean Stage Level 5: Shark Boss ###
print("The shark boss is blocking your way! Your only option is to attack!")
battleOutcome = battle(Stats,SharkStats)
if battleOutcome == 1:
    print("You are healed by your consumption.")
    #print("You gain 1 Red Point.")
    #RedPoints += 1
elif battleOutcome == 2:
    print("You are healed by your consumption.")
    #print("You gain 1 Green Point.")
    #GreenPoints += 1
else:
    gameOver = 1

if gameOver == 1:
        GAMEOVER(gameOver)
print()
input("Congratulations. You have proven yourself worthy of taken a step through time. Prepare to be reborn as a distant descendant.")
print()
#################################################### Small Mammal Stage ####################################################

input("Your journey continues in the future. You now exist as a small mammal. (1/3)")
input("Prepare yourself for 4 tough opponents and 1 boss. (2/3)")
input("If you succeed, I will transport you forward in time to live as a distant descendant of yours. Good luck! (3/3)")
print()

### reset Player's stats to initial values ###
Health = 70
Attack = 10
Sneak = 30
RedPoints = 0
GreenPoints = 0
Stats = [Health, Attack, Sneak]
gameOver = 0
pointsAfterShop = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Small Mammal Enemy Stats and Evolutionary Traits ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Chipmunk ###
Chipmunk = "Chipmunk"
ChipmunkHealth = 50
ChipmunkAttack = 4
ChipmunkStats = [ChipmunkHealth, ChipmunkAttack, Chipmunk]
### Squirrel ###
Squirrel = "Squirrel"
SquirrelHealth = 60
SquirrelAttack = 6
SquirrelStats = [SquirrelHealth, SquirrelAttack, Squirrel]
### Raccoon ###
Raccoon = "Raccoon"
RaccoonHealth = 75
RaccoonAttack = 8
RaccoonStats = [RaccoonHealth, RaccoonAttack, Raccoon]
### Fox ###
Fox = "Fox"
FoxHealth = 90
FoxAttack = 9
FoxStats = [FoxHealth, FoxAttack, Fox]
### Wolverine ###
Wolverine = "Wolverine"
WolverineHealth = 100
WolverineAttack = 15
WolverineStats = [WolverineHealth, WolverineAttack, Wolverine]
### Small Mammal Stage Evolutionary Trait Options ###
SmallMammalTraits = ["Thick Skin", "Fangs", "Improved Tail", "A gun"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 6
### Small Mammal Stage Level 6: Chipmunk ###
print("You come across a chipmunk. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, ChipmunkStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, SmallMammalTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 7
### Small Mammal Stage Level 7: Squirrel ###
print("You come across a squirrel. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, SquirrelStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, SmallMammalTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 8
### Small Mammal Stage Level 8: Raccoon ###
print("You come across a raccoon. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, RaccoonStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, SmallMammalTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 9
### Small Mammal Stage Level 9: Fox ###
print("You come across a fox. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, FoxStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, SmallMammalTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 10
### Small Mammal Stage Level 10: Wolverine Boss ###
print("The wolverine boss is blocking your way! Your only option is to attack!")
battleOutcome = battle(Stats,WolverineStats)
if battleOutcome == 1:
    print("You are healed by your consumption.")
    #print("You gain 1 Red Point.")
    #RedPoints += 1
elif battleOutcome == 2:
    print("You are healed by your consumption.")
    #print("You gain 1 Green Point.")
    #GreenPoints += 1
else:
    gameOver = 1

if gameOver == 1:
        GAMEOVER(gameOver)
print()
input("Congratulations. You have proven yourself worthy of taken a step through time. Prepare to be reborn as a distant descendant.")
print()
#################################################### Large Mammal Stage ####################################################

input("Your journey continues in the future. You now exist as a large mammal. (1/3)")
input("Prepare yourself for 4 tough opponents and 1 boss. (2/3)")
input("If you succeed, I will transport you forward in time to live as a distant descendant of yours. Good luck! (3/3)")
print()

### reset Player's stats to initial values ###
Health = 70
Attack = 10
Sneak = 30
RedPoints = 0
GreenPoints = 0
Stats = [Health, Attack, Sneak]
gameOver = 0
pointsAfterShop = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Large Mammal Enemy Stats and Evolutionary Traits ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Coyote ###
Coyote = "Coyote"
CoyoteHealth = 50
CoyoteAttack = 4
CoyoteStats = [CoyoteHealth, CoyoteAttack, Coyote]
### Elk ###
Elk = "Elk"
ElkHealth = 60
ElkAttack = 6
ElkStats = [ElkHealth, ElkAttack, Elk]
### Saber Tooth Tiger ###
SaberToothTiger = "Saber Tooth Tiger"
SaberToothTigerHealth = 75
SaberToothTigerAttack = 8
SaberToothTigerStats = [SaberToothTigerHealth, SaberToothTigerAttack, SaberToothTiger]
### Bear ###
Bear = "Bear"
BearHealth = 90
BearAttack = 9
BearStats = [BearHealth, BearAttack, Bear]
### Mammoth ###
Mammoth = "Mammoth"
MammothHealth = 100
MammothAttack = 15
MammothStats = [MammothHealth, MammothAttack, Mammoth]
### Large Mammal Stage Evolutionary Trait Options ###
LargeMammalTraits = ["Buffalo hump", "Saber teeth", "Improved footpads", "A gun"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 11
### Large Mammal Stage Level 11: Coyote ###
print("You come across a coyote. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, CoyoteStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, LargeMammalTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 12
### Large Mammal Stage Level 12: Elk ###
print("You come across a elk. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, ElkStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, LargeMammalTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 13
### Large Mammal Stage Level 13: Saber tooth tiger ###
print("You come across a saber tooth tiger. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, SaberToothTigerStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, LargeMammalTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 14
### Large Mammal Stage Level 14: Bear ###
print("You come across a fox. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, BearStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, LargeMammalTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 15
### Large Mammal Stage Level 15: Mammoth Boss ###
print("The mammoth boss is blocking your way! Your only option is to attack!")
battleOutcome = battle(Stats,MammothStats)
if battleOutcome == 1:
    print("You are healed by your consumption.")
    #print("You gain 1 Red Point.")
    #RedPoints += 1
elif battleOutcome == 2:
    print("You are healed by your consumption.")
    #print("You gain 1 Green Point.")
    #GreenPoints += 1
else:
    gameOver = 1

if gameOver == 1:
        GAMEOVER(gameOver)
print()
input("Congratulations. You have proven yourself worthy of taken a step through time. Prepare to be reborn as a distant descendant.")
print()
#################################################### Caveman Stage ####################################################

input("Your journey continues in the future. You now exist as a caveman. (1/3)")
input("Prepare yourself for 4 tough opponents and 1 boss. (2/3)")
input("If you succeed, I will transport you forward in time to live as a distant descendant of yours. Good luck! (3/3)")
print()

### reset Player's stats to initial values ###
Health = 70
Attack = 10
Sneak = 30
RedPoints = 0
GreenPoints = 0
Stats = [Health, Attack, Sneak]
gameOver = 0
pointsAfterShop = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Large Mammal Enemy Stats and Evolutionary Traits ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Fox ###
Fox = "Fox"
FoxHealth = 50
FoxAttack = 4
FoxStats = [FoxHealth, FoxAttack, Coyote]
### Eagle ###
Eagle = "Eagle"
EagleHealth = 60
EagleAttack = 6
EagleStats = [EagleHealth, EagleAttack, Eagle]
### Deer ###
Deer = "Deer"
DeerHealth = 75
DeerAttack = 8
DeerStats = [DeerHealth, DeerAttack, Deer]
### Wolf ###
Wolf = "Wolf"
WolfHealth = 90
WolfAttack = 9
WolfStats = [WolfHealth, WolfAttack, Wolf]
### Caveman ###
Caveman = "Caveman"
CavemanHealth = 100
CavemanAttack = 15
CavemanStats = [CavemanHealth, CavemanAttack, Caveman]
### Caveman Stage Evolutionary Trait Options ###
CavemanStageTraits = ["Knowledge of nutrients", "Knowledge of weapons", "A tail", "A gun"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 16
### Caveman Stage Level 16: Fox ###
print("You come across a fox. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, FoxStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, CavemanStageTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 17
### Caveman Stage Level 17: Eagle ###
print("You come across a eagle. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, EagleStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, CavemanStageTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 18
### Caveman Stage Level 18: Deer ###
print("You come across a deer. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, DeerStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, CavemanStageTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 19
### Caveman Stage Level 19: Wolf ###
print("You come across a wolf. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, WolfStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, CavemanStageTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 20
### Caveman Stage Level 20: Caveman Boss ###
print("The caveman boss is blocking your way! Your only option is to attack!")
battleOutcome = battle(Stats,CavemanStats)
if battleOutcome == 1:
    print("You are healed by your consumption.")
    #print("You gain 1 Red Point.")
    #RedPoints += 1
elif battleOutcome == 2:
    print("You are healed by your consumption.")
    #print("You gain 1 Green Point.")
    #GreenPoints += 1
else:
    gameOver = 1

if gameOver == 1:
        GAMEOVER(gameOver)
print()
input("Congratulations...you have proven yourself worthy of taken a step through time. Prepare to be reborn as a distant descendant.")
print()

#################################################### Alien Stage ####################################################

input("You think you're so talented don't you? Let's see how you fare against my men. (1/3)")
input("Prepare yourself for 4 tough opponents and 1 boss. (2/3)")
input("You won't succeed, I will not allow it. Good riddance! (3/3)")
print()

### reset Player's stats to initial values ###
Health = 70
Attack = 10
Sneak = 30
RedPoints = 0
GreenPoints = 0
Stats = [Health, Attack, Sneak]
gameOver = 0
pointsAfterShop = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Alien Enemy Stats and Evolutionary Traits ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Mindling ###
Mindling = "Mindling"
MindlingHealth = 50
MindlingAttack = 4
MindlingStats = [MindlingHealth, MindlingAttack, Mindling]
### Mindling Soldier ###
MindlingSoldier = "Mindling Soldier"
MindlingSoldierHealth = 60
MindlingSoldierAttack = 6
MindlingSoldierStats = [MindlingSoldierHealth, MindlingSoldierAttack, MindlingSoldier]
### Mindling Brute ###
MindlingBrute = "Mindling Brute"
MindlingBruteHealth = 75
MindlingBruteAttack = 8
MindlingBruteStats = [MindlingBruteHealth, MindlingBruteAttack, MindlingBrute]
### Mindling Savant ###
Savant = "Mindling Savant"
SavantHealth = 90
SavantAttack = 9
SavantStats = [SavantHealth, SavantAttack, Savant]
### The Narrator ###
Narrator = "Narrator"
NarratorHealth = 100
NarratorAttack = 15
NarratorStats = [NarratorHealth, NarratorAttack, Narrator]
### Caveman Stage Evolutionary Trait Options ###
AlienTraits = ["Vitals booster", "Psychic awakening", "State-of-matter transformation", "A ray gun"]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 21
### Alien Stage Level 21: Mindling ###
print("You come across a Mindling. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, MindlingStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, AlienTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 22
### Alien Stage Level 22: Mindling Soldier ###
print("You come across a Mindling Soldier. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, MindlingSoldierStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, AlienTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 23
### Alien Stage Level 23: Mindling Brute ###
print("You come across a Mindling Brute. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, MindlingBruteStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, AlienTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 24
### Alien Stage Level 24: Mindling Savant ###
print("You come across a Mindling Savant. Would you like to (1)attack or (2)sneak by?")
try:
    encounterChoice = int(input("Enter your choice: "))
except ValueError:
    print("Not actively making a choice may be your downfall.")
    encounterChoice = 1
while encounterChoice != 1 and encounterChoice !=2:
    encounterChoice = int(input("Please enter a 1 or 2: "))
encounterOutcome = encounter(encounterChoice, Stats, SavantStats)
RedPoints += encounterOutcome[0]
GreenPoints += encounterOutcome[1]
#enter evolution shop
pointsAfterShop = shop(RedPoints, GreenPoints, AlienTraits)
RedPoints = pointsAfterShop[0]
GreenPoints = pointsAfterShop[1]
Health += pointsAfterShop[2]
Attack += pointsAfterShop[3]
Sneak += pointsAfterShop[4]
Stats = [Health, Attack, Sneak]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Level 25
### Alien Stage Level 25: Narrator Boss ###
print("This wasn't supposed to happen! I CREATED you for this, MY GAME! HOW DARE YOU RUIN MY FUN! PREPARE TO DIE!")
battleOutcome = battle(Stats,NarratorStats)
if battleOutcome == 1:
    #print("You are healed by your consumption.")
    #print("You gain 1 Red Point.")
    RedPoints += 1
elif battleOutcome == 2:
    #print("You are healed by your consumption.")
    #print("You gain 1 Green Point.")
    GreenPoints += 1
else:
    gameOver = 1

if gameOver == 1:
        GAMEOVER(gameOver)
print()
print("THAT'S IT! If I can move you forward like they told me, then I bet I can send you BACK! Get out of here and go back to whence you came!")
#call win function
WIN()
print()