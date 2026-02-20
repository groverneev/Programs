import random
from time import sleep

#classes
class card:
    #within each: attack, buying power, number of cards to draw, special ability
    def __init__(self, ally, name, cardType, subtype, cost, defense, basicAbilitiesOpt1, basicAbilitiesOpt2, faction, trashAbilities, number):
        self.ally = ally
        self.name = name
        self.cardType = cardType
        self.subtype = subtype
        self.cost = cost
        self.defense = defense
        self.basicAbilitiesOpt1 = basicAbilitiesOpt1
        self.basicAbilitiesOpt2 = basicAbilitiesOpt2
        self.faction = faction
        self.trashAbilities = trashAbilities
        self.number = number
        
        self.info = 'lvl '+ str(cost) + ' ' + str(ally) + ' '
        if cardType == 'base':
            self.info += str(subtype) + ' ' + str(cardType) + ' / defense: ' + str(defense)
        else:
            self.info += str(cardType)

        if self.basicAbilitiesOpt1 != None:
            self.info += ' / '
            self.createInfo(self.basicAbilitiesOpt1)
        if self.basicAbilitiesOpt2 != None:
            self.info += ' or '
            self.createInfo(self.basicAbilitiesOpt2)
        if self.faction != None:
            self.info += ' / '
            self.info += 'faction: '
            self.createInfo(self.faction)
        if self.trashAbilities != None:
            self.info += ' / '
            self.info += 'trash for: '
            self.createInfo(self.trashAbilities)
        
    
    def getDefense(self):
        if self.subtype == 'outpost':
            return self.defense
        else:
            return 0
    
    def getNumber(self):
        return self.number
    
    def getName(self):
        return self.name
    
    def getAlly(self):
        return self.ally
    
    def getInfo(self):
        return self.info
    
    def getCost(self):
        return self.cost
    
    def getType(self):
        return self.cardType
    
    def getBuying(self, factionUsed, option):
        buying = 0
        if option == 1:
            if self.basicAbilitiesOpt1 != None:
                if self.basicAbilitiesOpt1[1] != None:
                    buying += self.basicAbilitiesOpt1[1]
        else:
            if self.basicAbilitiesOpt2 != None:
                if self.basicAbilitiesOpt2[1] != None:
                    buying += self.basicAbilitiesOpt2[1]
        if factionUsed == True:
            if self.faction != None:
                if self.faction[1] != None:
                    buying += self.faction[1]
        return buying
    
    def getDamage(self, factionUsed, option):
        damage = 0
        if option == 1:
            if self.basicAbilitiesOpt1 != None:
                if self.basicAbilitiesOpt1[0] != None:
                    damage += self.basicAbilitiesOpt1[0]
        else:
            if self.basicAbilitiesOpt2 != None:
                if self.basicAbilitiesOpt2[0] != None:
                    damage += self.basicAbilitiesOpt2[0]
        if factionUsed == True:
            if self.faction != None:
                if self.faction[0] != None:
                    damage += self.faction[0]
        return damage
                    
    def getCardsToDraw(self, factionUsed, option):
        drawCards = 0
        if option == 1:
            if self.basicAbilitiesOpt1 != None:
                if self.basicAbilitiesOpt1[2] != None:
                    drawCards += self.basicAbilitiesOpt1[2]
        else:
            if self.basicAbilitiesOpt2 != None:
                if self.basicAbilitiesOpt2[2] != None:
                    drawCards += self.basicAbilitiesOpt2[2]
        if factionUsed == True:
            if self.faction != None:
                if self.faction[2] != None:
                    drawCards += self.faction[2]
        return drawCards
    def createInfo(self, list):
        if list != None:
            if list[0] != None:
                self.info +=  str(list[0]) + ' damage'
            if list[1] != None:
                if list[0] != None:
                    self.info += ', '
                self.info += str(list[1]) + ' buying power'
            if list[2] != None:
                if list[0] != None or list[0] != None:
                    self.info += ', '
                if list[2] == 1:
                    self.info += 'draw a card'
                else:
                    self.info += 'draw two cards'
            if list[3] != None:
                if list[0] != None or list[1] != None or list[2] != None:
                    self.info += ', '
                if list[3] == 'TODAC':
                    actualPhrase = 'Target Opponent Discards A Card'
                elif list[3] == 'Opt Scrap':
                    actualPhrase = 'You may scrap a card in your hand or discard pile'
                elif list[3] == 'Scrap Trade Row':
                    actualPhrase = 'You may scrap a card in the trade row'
                elif list[3] == 'NextShipAtTopOfDeck':
                    actualPhrase = 'You may place the next ship you aquire at the top of your deck'
                else:
                    actualPhrase = list[3]
                self.info += str(actualPhrase)

#variables
player1Deck = []
player2Deck = []
shop = []
shopDeck = []
explorerDeck = []


def transferCards(list1, list2, number):
    for _ in range(number):
        list2.append(list1[-1])
        list1.pop()
        
    

#creating Decks
#unnaligned ships
Viper = card('unaligned', 'Viper', 'ship', None, None, None, [1, None, None, None], None, None, None, 4)
for _ in range (int(Viper.getNumber()/2)):
    player1Deck.append(Viper)
    player2Deck.append(Viper)

Scout = card('unaligned', 'Scout', 'ship', None, None, None, [None, 1, None, None], None, None, None, 16)
for _ in range (int(Scout.getNumber()/2)):
    player1Deck.append(Scout)
    player2Deck.append(Scout)

Explorer = card('unaligned', 'Explorer', 'ship', None, 2, None, [None, 2, None, None], None, None, [2, None, None, None], 10)
for _ in range(Explorer.getNumber()):
    explorerDeck.append(Explorer)


#blobs
BlobFighter = card('Blob', 'Blob Fighter', 'ship', None, 1, None, [3, None, None, None], None, [None, None, 1, None], None, 3)
for _ in range (BlobFighter.getNumber()):
    shopDeck.append(BlobFighter)
    
BattlePod = card('Blob', 'Battle Pod', 'ship', None, 2, None, [4, None, None, 'Scrap Trade Row'], None, [2, None, None, None], None, 2)
for _ in range(BattlePod.getNumber()):
    shopDeck.append(BattlePod)
    
TradePod = card('Blob', 'Trade Pod', 'ship', None, 2, None, [None, 3, None, None], None, [2, None, None, None], None, 3)
for _ in range (TradePod.getNumber()):
    shopDeck.append(TradePod)

Ram = card('Blob', 'Ram', 'ship', None, 3, None, [5, None, None, None, None], None, [2, None, None, None], [None, 3, None, None], 2)
for _ in range (Ram.getNumber()):
    shopDeck.append(Ram)
    
BlobDestroyer = card('Blob', 'Blob Destroyer', 'ship', None, 4, None, [5, None, None, None], None, [None, None, None, 'You may scrap a card, You may destroy target base'], None, 2)
for _ in range(BlobDestroyer.getNumber()):
    shopDeck.append(BlobDestroyer)

BattleBlob = card('Blob', 'Battle Blob', 'ship', None, 6, None, [8, None, None, None], None, [None, None, 1, None], [4, None, None, None], 1)
for _ in range(BattleBlob.getNumber()):
    shopDeck.append(BattleBlob)
    
BlobCarrier = card('Blob', 'Blob Carrier', 'ship', None, 6, None, [7, None, None, None], None, [None, None, None, 'Acquire Free Ship'], None, 1)
for _ in range(BlobCarrier.getNumber()):
    shopDeck.append(BlobCarrier)
    
MotherShip = card('Blob', 'MotherShip', 'ship', None, 7, None, [6, None, 1, None], None, [None, None, 1, None], None, 1)
for _ in range (MotherShip.getNumber()):
    shopDeck.append(MotherShip)

BlobWheel = card('Blob', 'Blob Wheel', 'base', 'basic', 3, 5, [1, None, None, None], None, None, [None, 3, None, None], 3)
for _ in range (BlobWheel.getNumber()):
    shopDeck.append(BlobWheel)
    
Hive = card('Blob', 'Hive', 'base', 'basic', 5, 5, [3, None, None, None], None, [None, None, 1, None], None, 1)
for _ in range(Hive.getNumber()):
    shopDeck.append(Hive)
    
BlobWorld = card('Blob', 'Blob World', 'base', 'basic', 8, 7, [5, None, None, None], [None, None, 'Number of Blobs', None], None, None, 1)
for _ in range(BlobWorld.getNumber()):
    shopDeck.append(BlobWorld)



#mechs
TradeBot = card('Machine Cult', 'Trade Bot', 'ship', None, 1, None, [1, None, None, 'Opt Scrap'], None, [2, None, None, None], None, 3)
for _ in range (TradeBot.getNumber()):
    shopDeck.append(TradeBot)
    
MissileBot = card('Machine Cult', 'Missile Bot', 'ship', None, 2, None, [2, None, None, 'Opt Scrap'], None, [2, None, None, None], None, 3 )
for _ in range (MissileBot.getNumber()):
    shopDeck.append(MissileBot)
    
SupplyBot = card('Machine Cult', 'Supply Bot', 'ship', None, 3, None, [None, 2, None, 'Opt Scrap'], None, [2, None, None, None], None, 3)
for _ in range(SupplyBot.getNumber()):
    shopDeck.append(SupplyBot)
    
PatrolMech = card('Machine Cult', 'Patrol Mech', 'ship', None, 4, None, [5, None, None, None], [None, 3, None, None], [None, None, None, 'Opt Scrap'], None, 2)
for _ in range(PatrolMech.getNumber()):
    shopDeck.append(PatrolMech)
    
StealthNeedle = card('machineCult', 'Stealth Needle', 'ship', None, 4, None, [None, None, None, 'This card can copy another ship you play. It counts as MachineCult and the faction you play'], None, None, None, 1)
for _ in range(StealthNeedle.getNumber()):
    shopDeck.append(StealthNeedle)
    
BattleMech = card('Machine Cult', 'Battle Mech', 'ship', None, 5, None, [4, None, None, 'Opt Scrap'], None, [None, None, 1, None], None, 1)
for _ in range(BattleMech.getNumber()):
    shopDeck.append(BattleMech)
    
MissileMech = card('Machine Cult', 'Missile Mech', 'ship', None, 6, None, [6, None, None, 'Destroy Base'], None, [None, None, 1, None], None, 1)
for _ in range(MissileMech.getNumber()):
    shopDeck.append(MissileMech)
    
BattleStation = card('Machine Cult', 'Battle Station', 'base', 'outpost', 3, 5, None, None, None, [5, None, None, None], 2)
for _ in range(BattleStation.getNumber()):
    shopDeck.append(BattleStation)
    
Junkyard = card('Machine Cult', 'Junkyard', 'base', 'outpost', 6, 5, [None, None, None, 'opt Scrap'], None, None, None, 1)
for _ in range(Junkyard.getNumber()):
    shopDeck.append(Junkyard)

MechWorld = card('Machine Cult', 'Mech World', 'base', 'outpost', 5, 6, [None, None, None, 'This card counts as all factions'], None, None, None, 1)
for _ in range(MechWorld.getNumber()):
    shopDeck.append(MechWorld)
    
MachineBase = card('Machine Cult', 'Machine Base', 'base', 'outpost', 7, 6, [None, None, None, 'draw a card then scrap a card in your hand'], None, None, None, 1)
for _ in range(MachineBase.getNumber()):
    shopDeck.append(MachineBase)
    
BrainWorld = card('Machine Cult', 'Machine Base', 'base', 'outpost', 8, 6, [None, None, None, 'Scrap up to two cards in your hand or discard pile then draw that many cards'], None, None, None, 1)
for _ in range(BrainWorld.getNumber()):
    shopDeck.append(BrainWorld)

#trade federation
FederationShuttle = card('Trade Federation', 'Federation Shuttle', 'ship', None, 1, None, [None, 2, None, None], None, [None, None, None, '4 health'], None, 3)
for _ in range(FederationShuttle.getNumber()):
    shopDeck.append(FederationShuttle)
    
Cutter = card('Trade Federation', 'Cutter', 'ship', None, 2, None, [None, 2, None, 'Health:4'], None, [4, None, None, None], None, 3)
for _ in range (Cutter.getNumber()):
    shopDeck.append(Cutter)
    
EmbassyYacht = card('Trade Federation', 'Embassy Yacht', 'ship', None, 3, None, [2, None, None, '3 health, draw two cards if you have 2 or more bases in play'], None, None, None, 2)
for _ in range (EmbassyYacht.getNumber()):
    shopDeck.append(EmbassyYacht)
    
Freighter = card('Trade Federation', 'Freighter', 'ship', None, 4, None, [None, 4, None, None], None, [None, None, None, 'NextShipAtTopOfDeck'], None, 2)
for _ in range (Freighter.getNumber()):
    shopDeck.append(Freighter)
    
Flagship = card('Trade Federation', 'Flagship', 'ship', None, 6, None, [5, None, 1, None], None, [None, None, None, '5 health'], None, 1)
for _ in range(Flagship.getNumber()):
    shopDeck.append(Flagship)
    
CommandShip = card('Trade Federation', 'Command Ship', 'ship', None, 8, None, [5, None, 2, '4 health'], None, [None, None, None, 'Destroy base'], None, 1)
for _ in range(CommandShip.getNumber()):
    shopDeck.append(CommandShip)

TradeEscort = card('Trade Federation', 'Trade Escort','ship', None, 5, None, [4, None, None, '4 health'], None, [None, None, 1, None], None, 1)
for _ in range (TradeEscort.getNumber()):
    shopDeck.append(TradeEscort)

TradingPost = card('Trade Federation', 'Trading Post', 'base', 'outpost', 3, 4, [None, 1, None, None], [None, None, None, '1 health'], None, [3, None, None, None], 2)
for _ in range (TradingPost.getNumber()):
    shopDeck.append(TradingPost)

BarterWorld = card('Trade Federation', 'Barter World', 'base', 'basic', 4, 4, [None, 2, None, None], [None, None, None, '2 health'], None, [5, None, None, None], 2)
for _ in range (BarterWorld.getNumber()):
    shopDeck.append(BarterWorld)

    
DefenseCenter = card('Trade Federation', 'Defense Center', 'base', 'outpost', 5, 5, [None, None, None, '3 health'], [2, None, None, None], [2, None, None, None], None, 1)
for _ in range(DefenseCenter.getNumber()):
    shopDeck.append(DefenseCenter)

PortOfCall = card('Trade Federation', 'Port Of Call', 'base', 'outpost', 6, 6, [None, 3, None, None], None, None, [None, None, 1, 'Destroy Base'], 1)
for _ in range(PortOfCall.getNumber()):
    shopDeck.append(PortOfCall)
    
CentralOffice = card('Trade Federation', 'Central Office', 'base', 'basic', 7, 7, [None, 2, None, 'NextShipAtTopOfDeck'], None, [None, None, 1, None], None, 1)
for _ in range(CentralOffice.getNumber()):
    shopDeck.append(CentralOffice)


#star empire
ImperialFighter = card('Star Empire', 'Imperial Fighter', 'ship', None, 1, None, [2, None, None, None, 'TODAC'], None, [2, None, None, None], None, 3)
for _ in range (ImperialFighter.getNumber()):
    shopDeck.append(ImperialFighter)

Corvette = card('Star Empire', 'Corvette', 'ship', None, 2, None, [1, None, 1, None], None, [2, None, None, None], None, 2)
for _ in range(Corvette.getNumber()):
    shopDeck.append(Corvette)

SurveyShip = card('Star Empire', 'Survey Ship', 'ship', None, 3, None, [None, 1, 1, None], None, None, [None, None, None, 'TODAC'], 3)
for _ in range (SurveyShip.getNumber()):
    shopDeck.append(SurveyShip)
    
ImperialFrigate = card('Star Empire', 'Imperial Frigate', 'ship', None, 3, None, [4, None, None, 'TODAC'], None, [2, None, None, None], [None, None, 1, None], 3)
for _ in range(ImperialFrigate.getNumber()):
    shopDeck.append(ImperialFrigate)
    
Battlecruiser = card('Star Empire', 'Battlecruiser', 'ship', None, 6, None, [5, None, 1, None], None, [None, None, None, 'TODAC'], [None, None, 1, 'Destroy Base'], 1)
for _ in range(Battlecruiser.getNumber()):
    shopDeck.append(Battlecruiser)
    
Dreadnaught = card('Star Empire', 'Dreadnaught', 'ship', None, 7, None, [7, None, 1, None], None, None, [5, None, None, None], 1)
for _ in range (Dreadnaught.getNumber()):
    shopDeck.append(Dreadnaught)
    
SpaceStation = card('Star Empire', 'Space Station', 'base', 'outpost', 4, 4, [2, None, None, None], None, [2, None, None, None], [None, 4, None, None], 2)
for _ in range(SpaceStation.getNumber()):
    shopDeck.append(SpaceStation)
    
recyclingStation = card('Star Empire', 'Recycling Station', 'base', 'outpost', 4, 4, [None, 1, None, None], [None, None, None, 'Discard up to two cards then draw that many cards'], None, None, 2)
for _ in range(recyclingStation.getNumber()):
    shopDeck.append(recyclingStation)
    
warWorld = card('Star Empire', 'War World', 'base', 'outpost', 5, 4, [3, None, None, None], None, [4, None, None, None], None, 1)
for _ in range(warWorld.getNumber()):
    shopDeck.append(warWorld)
    
RoyalRedoubt = card('Star Empire', 'Royal Redoubt', 'base', 'outpost', 6, 6, [3, None, None, None], None, [None, None, None, 'TODAC'], None, 1)
for _ in range(RoyalRedoubt.getNumber()):
    shopDeck.append(RoyalRedoubt)
    
FleetHQ = card('Star Empire', 'Fleet HQ', 'base', 'basic', 8, 8, [None, None, None, 'Gain one extra damage for each ship you play'], None, None, None, 1)
for _ in range(FleetHQ.getNumber()):
    shopDeck.append(FleetHQ)

random.shuffle(shopDeck)
random.shuffle(player1Deck)
random.shuffle(player2Deck)
transferCards(shopDeck, shop, 5)
transferCards(explorerDeck, shop, 1)
gameOver = False
playerHand = []
player1Discard = []
player2Discard = []
player1Authority = 50
player2Authority = 50
player1Bases = []
player2Bases = []

def checkIfEnoughBuying(buying):
    enoughBuying = False
    for i in range (len(shop)):
        if buying > shop[i].getCost()-1:
            enoughBuying = True
    
    return enoughBuying


def printShop():
    print('Shop:')
    for i in range(len(shop)):
        print(str(shop[i].getName()) + ': ' + str(shop[i].getInfo()))

def playTurn(player, startingHand):
    global player1Authority, player2Authority, player1Deck, player2Deck, player1Discard, player2Discard, playerHand
    if player == 1:
        print('**Player 1 (' + str(player1Authority) +' health) **')
    else:
        print('**Player 2 (' + str(player2Authority) +' health) **')
    printShop()
    print('Your hand:')
    buyingPower = 0
    mechsPlayed = 0
    blobsPlayed = 0
    turnDamage = 0
    tradeFederationPlayed = 0
    starEmpirePlayed = 0
    cardsDraw = startingHand
    playerHand = []
    if player == 1:
        bases = player1Bases
    else:
        bases = player2Bases
    while startingHand + cardsDraw  > len(playerHand) - len(bases):
        buyingPower = 0
        mechsPlayed = 0
        blobsPlayed = 0
        turnDamage = 0
        tradeFederationPlayed = 0
        starEmpirePlayed = 0
        if len(playerHand) > 0:
            if cardsDraw == 1:
                print('You draw a card:')
            else: 
                print('You draw ' + str(cardsDraw) + ' more cards:')
        if player == 1:
            if len(player1Deck) < cardsDraw:
                retransfer = cardsDraw - len(player1Deck)
                transferCards(player1Deck, playerHand, len(player1Deck))
                player1Deck = player1Discard.copy()
                random.shuffle(player1Deck)
                player1Discard = []
                transferCards(player1Deck, playerHand, retransfer)
            else:
                transferCards(player1Deck, playerHand, cardsDraw)
        else:
            if len(player2Deck) < cardsDraw:
                retransfer = cardsDraw - len(player2Deck)
                transferCards(player2Deck, playerHand, len(player2Deck))
                player2Deck = player2Discard.copy()
                random.shuffle(player2Deck)
                player2Discard = []
                transferCards(player2Deck, playerHand, retransfer)
            else:
                transferCards(player2Deck, playerHand, cardsDraw)
        if len(playerHand) == startingHand:
            playerHand = playerHand + bases
            cardsDraw = 0
        else:
            cardsDraw = -1 * cardsDraw
        for i in range(2*len(playerHand)):
            if i < len(playerHand):
                print(str(playerHand[i].getName()) + ': ' + str(playerHand[i].getInfo()))
                if playerHand[i].getAlly() == 'Blob':
                    blobsPlayed += 1
                elif playerHand[i].getAlly() == 'Machine Cult':
                    mechsPlayed += 1
                elif playerHand[i].getAlly() == 'Trade Federation':
                    tradeFederationPlayed += 1
                elif playerHand[i].getAlly() == 'Star Empire':
                    starEmpirePlayed += 1
            else:
                allyPlayed = False
                if playerHand[i-len(playerHand)].getAlly() == 'Blob':
                    if blobsPlayed > 1:
                        allyPlayed = True
                elif playerHand[i-len(playerHand)].getAlly() == 'Machine Cult':
                    if mechsPlayed > 1:
                        allyPlayed = True
                elif playerHand[i-len(playerHand)].getAlly() == 'Trade Federation':
                    if tradeFederationPlayed > 1:
                        allyPlayed = True
                elif playerHand[i-len(playerHand)].getAlly() == 'Star Empire':
                    if starEmpirePlayed > 1:
                        allyPlayed = True
                buyingPower += playerHand[i-len(playerHand)].getBuying(allyPlayed, 1)
                turnDamage += playerHand[i-len(playerHand)].getDamage(allyPlayed, 1)
                cardsDraw += playerHand[i-len(playerHand)].getCardsToDraw(allyPlayed, 1)  
        numCards = len(playerHand)
        if cardsDraw == 0:
            for i in range(numCards):
                if playerHand[0].getType() == 'ship':
                    if player == 1:
                        player1Discard.append(playerHand[0])
                    else:
                        player2Discard.append(playerHand[0])
                elif playerHand[0].getType() == 'base':
                    if i < numCards - len(bases):
                        if player == 1:
                            player1Bases.append(playerHand[0])
                        else:
                            player2Bases.append(playerHand[0])
                playerHand.pop(0)
            if player == 1:
                player2Authority -= turnDamage
            else:
                player1Authority -= turnDamage
            print('Totals:')
            if turnDamage > 0:
                print('Damage: ' + str(turnDamage))
                if player == 1:
                    if len(player2Bases) > 0:
                        print('*opponent bases*:')
                    for i in range(len(player2Bases)):
                        print(player2Bases[i].getName() + ': ' + player2Bases[i].getInfo())
                    print('opponent health --> ' + str(player2Authority))
                    if player2Authority < 1:
                        print('Player 1 wins!')
                        return True
                else:
                    if len(player1Bases) > 0:
                        print('*opponent bases*:')
                    for i in range(len(player1Bases)):
                        print(player1Bases[i].getName() + ': ' + player1Bases[i].getInfo())
                    print('opponent health --> ' + str(player1Authority))
                    if player1Authority < 1:
                        print('Player 2 wins!')
                        return True
            if buyingPower > 0:
                canBuy = True
                while canBuy:
                    canBuy = checkIfEnoughBuying(buyingPower)
                    print('Buying power: ' + str(buyingPower))
                    if canBuy:
                        cardToBuy = input('would you like to buy anything?')
                        if cardToBuy != 'No' and cardToBuy != 'no':
                            cardFound = False
                            for i in range(len(shop)):
                                if cardToBuy.lower() == shop[i].getName().lower():
                                    cardFound = True
                                    if buyingPower > shop[i].getCost() - 1:
                                        print('You bought ' + shop[i].getName())
                                        buyingPower -= shop[i].getCost()
                                        if player == 1:
                                            player1Discard.append(shop[i])
                                        else:
                                            player2Discard.append(shop[i])
                                        shop.pop(i)
                                        if i == 5:
                                            if len(explorerDeck) > 0:
                                                shop.append(explorerDeck[0])
                                                explorerDeck.pop()
                                        else:
                                            shop.insert(i, shopDeck[-1])
                                            shopDeck.pop()
                                        printShop()
                                    else:
                                        print("You don't have enough buying")
                            if not cardFound:
                                 print('card not found')
                        else:
                            canBuy = False
                    else:
                        print("You can't buy anything")
        if cardsDraw == 0:
            sleep(2)
            return False
#Start of game   
gameOver = playTurn(player=1, startingHand=3)
while not gameOver:
    gameOver = playTurn(player=2, startingHand=5)
    if not gameOver:
        gameOver = playTurn(player=1, startingHand=5)