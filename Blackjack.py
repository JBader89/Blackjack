#Jeremy Bader, Katie Ketcham
#Final Project
#Blackjack: A Team Game?
#Team Strategy

import operator, sys, time, random
from graphics import *
import xlwt

class Environment:
    """Sets up the environment of the blackjack game"""
    def __init__(self, win):
        self.win = win;
        
    def drawTables(self):
        """Creates the four tables"""
        table1 = Image(Point(275,206.5),"table8.gif")
        table1.draw(self.win)
        table2 = Image(Point(825,619.5),"table8.gif")
        table2.draw(self.win)
        table3 = Image(Point(275,619.5),"table8.gif")
        table3.draw(self.win)
        table4 = Image(Point(825,206.5),"table8.gif")
        table4.draw(self.win)
        
    def makeDecks(self):
        """Makes the four decks"""
        deck1=[]
        cardValues1=[]
        for i in range(1,14):
            deck1.append(Image(Point(0,0),"c" + str(i) + ".gif"))
            if i<11:
                cardValues1.append(i)
            else:
                cardValues1.append(10)
        for i in range(1,14):
            deck1.append(Image(Point(0,0),"d" + str(i) + ".gif"))
            if i<11:
                cardValues1.append(i)
            else:
                cardValues1.append(10)
        for i in range(1,14):
            deck1.append(Image(Point(0,0),"h" + str(i) + ".gif"))
            if i<11:
                cardValues1.append(i)
            else:
                cardValues1.append(10)
        for i in range(1,14):
            deck1.append(Image(Point(0,0),"s" + str(i) + ".gif"))
            if i<11:
                cardValues1.append(i)
            else:
                cardValues1.append(10)
        for i in range(len(deck1)):
            for j in range(7):
                deck1.append(deck1[i].clone())
                if ((i%13)+1)<11:
                    cardValues1.append((i%13)+1)
                else:
                    cardValues1.append(10)
        cardValues2=list(cardValues1)
        cardValues3=list(cardValues1)
        cardValues4=list(cardValues1)
        deck2=list(deck1)
        deck3=list(deck1)
        deck4=list(deck1)
        downCardOriginal=Image(Point(275,165),"back101.gif")
        return deck1, deck2, deck3, deck4, downCardOriginal, cardValues1, cardValues2, cardValues3, cardValues4

    def makeChips(self):
        """Creates the betting chips"""
        chip100Original = Image(Point(275,228), "chip_100blackS.gif")
        chip10kOriginal = Image(Point(275,228), "chip_10000redS.gif")
        return chip100Original, chip10kOriginal

class Blackjack:
    """Handles all of the gameplay of the blackjack games"""
    def __init__(self, win, workbook, sheet, handCounter, winnings, deck1, deck2, deck3, deck4, cardOriginal, downCardOriginal, currentCards, tempCurrentCards, tempCurrentCards2, tempCurrentCards3, tempCurrentCards4, cardValues1, cardValues2, cardValues3, cardValues4, playerHand, playerHand2, dealerHand, chip100Original, chip10kOriginal, splitOn, splitHand, doubleDown1, doubleDown2, table, moveRight, moveDown, runningCount1, runningCount2, runningCount3, runningCount4, counter1, counter2, counter3, counter4, counter1text, counter2text, counter3text, counter4text, bankroll, bankrolltext, countThreshold, hitText, standText, doubleDownText, splitText, blackjackText, playerBustText, dealerBustText, playerWinText, dealerWinText, pushText, dealerScoreText, playerScoreText, playerScore2Text, dealerScores, playerScores, playerScores2, downCardScore, dealerHit):
        self.win = win
        self.workbook = workbook
        self.handCounter = handCounter
        self.winnings = winnings
        self.sheet = sheet
        self.deck1 = deck1
        self.deck2 = deck2
        self.deck3 = deck3
        self.deck4 = deck4
        self.cardValues1 = cardValues1
        self.cardValues2 = cardValues2
        self.cardValues3 = cardValues3
        self.cardValues4 = cardValues4
        self.cardOriginal = cardOriginal
        self.downCardOriginal = downCardOriginal
        self.downCard = downCardOriginal.clone()
        self.helperCard = downCardOriginal.clone()
        self.currentCards = currentCards
        self.tempCurrentCards = tempCurrentCards
        self.tempCurrentCards2 = tempCurrentCards2
        self.tempCurrentCards3 = tempCurrentCards3
        self.tempCurrentCards4 = tempCurrentCards4
        self.playerHand = playerHand
        self.playerHand2 = playerHand2
        self.dealerHand = dealerHand
        self.chip100Original = chip100Original
        self.chip100 = chip100Original.clone()
        self.chip100Clone = chip100Original.clone()
        self.chip100Clone2 = chip100Original.clone()
        self.chip100Clone3 = chip100Original.clone()
        self.chip10kOriginal = chip10kOriginal
        self.chip10k = chip10kOriginal.clone()
        self.chip10kClone = chip10kOriginal.clone()
        self.chip10kClone2 = chip10kOriginal.clone()
        self.chip10kClone3 = chip10kOriginal.clone()
        self.splitOn = splitOn
        self.splitHand = splitHand
        self.doubleDown1 = doubleDown1
        self.doubleDown2 = doubleDown2
        self.table = table
        self.moveRight = moveRight
        self.moveDown = moveDown
        self.runningCount1 = runningCount1
        self.runningCount2 = runningCount2
        self.runningCount3 = runningCount3
        self.runningCount4 = runningCount4
        self.counter1 = counter1
        self.counter2 = counter2
        self.counter3 = counter3
        self.counter4 = counter4
        self.counter1text = counter1text
        self.counter2text = counter2text
        self.counter3text = counter3text
        self.counter4text = counter4text
        self.bankrolltext = bankrolltext
        self.bankroll = bankroll
        self.countThreshold = countThreshold
        self.hitText = hitText
        self.standText = standText
        self.doubleDownText = doubleDownText
        self.splitText = splitText
        self.blackjackText = blackjackText
        self.playerBustText = playerBustText
        self.dealerBustText = dealerBustText
        self.playerWinText = playerWinText
        self.dealerWinText = dealerWinText
        self.pushText = pushText
        self.dealerScoreText = dealerScoreText
        self.playerScoreText = playerScoreText
        self.playerScore2Text = playerScore2Text
        self.dealerScores = dealerScores
        self.playerScores = playerScores
        self.playerScores2 = playerScores2
        self.downCardScore = downCardScore
        self.dealerHit = dealerHit
        
    def startGame(self):
        """Begins the game play sequence"""
        self.chip100.draw(self.win)
        right=0
        for i in range(4):
            time.sleep(.1)
            currentCard = random.randrange(self.getDeckLength())
            if i%2==1:
                dealer=125
                self.dealerHand.append(self.getCurrentCardValue(currentCard))
            elif i%2==0:
                dealer=0
                self.playerHand.append(self.getCurrentCardValue(currentCard))
            if i>1:
                right=10
            self.currentCards.append(self.getCurrentCard(currentCard))
            self.currentCards[i]._move(275+right, 290-dealer)
            self.currentCards[i].draw(self.win)
            self.removeCurrentCard(currentCard)
            self.removeCurrentCardValue(currentCard)
            if i==1:
                self.downCard.draw(self.win)
                
        self.playerTurn()
        for i in range(1000):
            if len(self.deck1)>20 and len(self.deck2)>20 and len(self.deck3)>20 and len(self.deck4)>20:
                self.dealHands()
            else:
                 i=1000
        self.workbook.save('Blackjack3.xls')
        blackjack(self.workbook, self.sheet, self.handCounter, self.winnings)

    def dealHands(self):
        """Deals each hand and restores all variables to original values for the current hand """
        time.sleep(1)
        self.handCounter+=1
        self.sheet.write(self.handCounter-1, 0, self.handCounter)
        self.sheet.write(self.handCounter-1, 1, self.winnings)
        self.removeText()
        self.dealerScoreText.undraw()
        self.playerScoreText.undraw()
        self.playerScore2Text.undraw()
        self.chip100 = self.chip100Original.clone()
        self.chip100Clone = self.chip100Original.clone()
        self.chip100Clone2 = self.chip100Original.clone()
        self.chip100Clone3 = self.chip100Original.clone()
        self.chip10k = self.chip10kOriginal.clone()
        self.chip10kClone = self.chip10kOriginal.clone()
        self.chip10kClone2 = self.chip10kOriginal.clone()
        self.chip10kClone3 = self.chip10kOriginal.clone()
        self.splitHand=1
        self.doubleDown1=False
        self.doubleDown2=False
        self.splitOn=True
        self.dealerHit=False
        self.downCardScore = 0
        if self.table==1:
            self.table=2
            self.moveRight=550
            self.moveDown=0
            for i in self.tempCurrentCards2:
                i.undraw()
            self.tempCurrentCards2 = list(self.currentCards)
        elif self.table==2:
            self.table=3
            self.moveRight=0
            self.moveDown=413
            for i in self.tempCurrentCards3:
                i.undraw()
            self.tempCurrentCards3 = list(self.currentCards)
        elif self.table==3:
            self.table=4
            self.moveRight=550
            self.moveDown=413
            for i in self.tempCurrentCards4:
                i.undraw()
            self.tempCurrentCards4 = list(self.currentCards)
        elif self.table==4:
            self.table=1
            self.moveRight=0
            self.moveDown=0
            for i in self.tempCurrentCards:
                i.undraw()
            self.tempCurrentCards = list(self.currentCards)
        for i in self.currentCards:
            i.undraw()
        if self.table==1:
            for i in self.tempCurrentCards:
                i.draw(self.win)
            for i in self.tempCurrentCards2:
                i.undraw()
            for i in range(len(self.tempCurrentCards2)):
                self.tempCurrentCards2.pop()
        elif self.table==2:
            for i in self.tempCurrentCards2:
                i.draw(self.win)
            for i in self.tempCurrentCards3:
                i.undraw()
            for i in range(len(self.tempCurrentCards3)):
                self.tempCurrentCards3.pop()
        elif self.table==3:
            for i in self.tempCurrentCards3:
                i.draw(self.win)
            for i in self.tempCurrentCards4:
                i.undraw()
            for i in range(len(self.tempCurrentCards4)):
                self.tempCurrentCards4.pop()
        elif self.table==4:
            for i in self.tempCurrentCards4:
                i.draw(self.win)
            for i in self.tempCurrentCards:
                i.undraw()
            for i in range(len(self.tempCurrentCards)):
                self.tempCurrentCards.pop()
        for i in range(len(self.currentCards)):
            self.currentCards.pop()
        for i in range(len(self.playerHand)):
            self.playerHand.pop()
        for i in range(len(self.playerHand2)):
            self.playerHand2.pop()
        for i in range(len(self.dealerHand)):
            self.dealerHand.pop()
        for i in range(len(self.playerScores)):
            self.playerScores.pop()
        for i in range(len(self.playerScores2)):
            self.playerScores2.pop()
        for i in range(len(self.dealerScores)):
            self.dealerScores.pop()
        self.runningCount1 = self.counter1
        self.runningCount2 = self.counter2
        self.runningCount3 = self.counter3
        self.runningCount4 = self.counter4
        self.chip100._move(self.moveRight, self.moveDown)
        self.chip100Clone._move(self.moveRight, self.moveDown)
        self.chip100Clone2._move(self.moveRight, self.moveDown)
        self.chip100Clone3._move(self.moveRight, self.moveDown)
        self.chip10k._move(self.moveRight, self.moveDown)
        self.chip10kClone._move(self.moveRight, self.moveDown)
        self.chip10kClone2._move(self.moveRight, self.moveDown)
        self.chip10kClone3._move(self.moveRight, self.moveDown)
        self.downCard.undraw()
        self.downCard=self.downCardOriginal.clone()
        self.downCard._move(self.moveRight, self.moveDown)

        currentCount=self.getCount()
        if currentCount>self.countThreshold:
            self.chip10k.draw(self.win)
        else:
            self.chip100.draw(self.win)
        
        right=0
        for i in range(4):
            time.sleep(.1)
            currentCard = random.randrange(self.getDeckLength())
            if i%2==1:
                dealer=125
                self.dealerHand.append(self.getCurrentCardValue(currentCard))
            elif i%2==0:
                dealer=0
                self.playerHand.append(self.getCurrentCardValue(currentCard))
            if i>1:
                right=10
            self.currentCards.append(self.getCurrentCard(currentCard))
            if self.currentCards[i].getAnchor().x!=0:
                self.currentCards[i]._move(-self.currentCards[i].getAnchor().x, -self.currentCards[i].getAnchor().y)
            self.currentCards[i]._move(275+right, 290-dealer)
            self.currentCards[i]._move(self.moveRight, self.moveDown)
            self.currentCards[i].draw(self.win)
            self.removeCurrentCard(currentCard)
            self.removeCurrentCardValue(currentCard)
            if i==1:
                self.downCard.draw(self.win)

        self.playerTurn()

    def getCurrentCard(self, currentCard):
        """Returns the current given random card image"""
        if self.table==1:
            return self.deck1[currentCard].clone()
        elif self.table==2:
            return self.deck2[currentCard].clone()
        elif self.table==3:
            return self.deck3[currentCard].clone()
        elif self.table==4:
            return self.deck4[currentCard].clone()

    def getCurrentCardValue(self, currentCard):
        """Returns the value of the current given random card, and updates the hand values"""
        if self.table==1:
            if len(self.currentCards)==0 or len(self.currentCards)==2:
                self.playerScores.append(self.cardValues1[currentCard])
            elif len(self.currentCards)==1:
                self.downCardScore+=self.cardValues1[currentCard]
            elif len(self.currentCards)==3:
               self.dealerScores.append(self.cardValues1[currentCard])
            elif self.dealerHit==False:
                if self.splitOn==False and len(self.currentCards)==5:
                    self.playerScores2.append(self.cardValues1[currentCard])
                elif self.splitHand==1:
                    self.playerScores.append(self.cardValues1[currentCard])
                elif self.splitHand==2:
                    self.playerScores2.append(self.cardValues1[currentCard])
            elif self.dealerHit==True:
                self.dealerScores.append(self.cardValues1[currentCard])
            if self.cardValues1[currentCard]>1 and self.cardValues1[currentCard]<7:
                self.counter1+=1
            elif self.cardValues1[currentCard]==1 or self.cardValues1[currentCard]>9:
                self.counter1-=1
            self.updateCount()
            self.updateScores()
            return self.cardValues1[currentCard]
        elif self.table==2:
            if len(self.currentCards)==0 or len(self.currentCards)==2:
                self.playerScores.append(self.cardValues2[currentCard])
            elif len(self.currentCards)==1:
                self.downCardScore+=self.cardValues2[currentCard]
            elif len(self.currentCards)==3:
               self.dealerScores.append(self.cardValues2[currentCard])
            elif self.dealerHit==False:
                if self.splitOn==False and len(self.currentCards)==5:
                    self.playerScores2.append(self.cardValues2[currentCard])
                elif self.splitHand==1:
                    self.playerScores.append(self.cardValues2[currentCard])
                elif self.splitHand==2:
                    self.playerScores2.append(self.cardValues2[currentCard])
            elif self.dealerHit==True:
                self.dealerScores.append(self.cardValues2[currentCard])
            if self.cardValues2[currentCard]>1 and self.cardValues2[currentCard]<7:
                self.counter2+=1
            elif self.cardValues2[currentCard]==1 or self.cardValues2[currentCard]>9:
                self.counter2-=1
            self.updateCount()
            self.updateScores()
            return self.cardValues2[currentCard]
        elif self.table==3:
            if len(self.currentCards)==0 or len(self.currentCards)==2:
                self.playerScores.append(self.cardValues3[currentCard])
            elif len(self.currentCards)==1:
                self.downCardScore+=self.cardValues3[currentCard]
            elif len(self.currentCards)==3:
               self.dealerScores.append(self.cardValues3[currentCard])
            elif self.dealerHit==False:
                if self.splitOn==False and len(self.currentCards)==5:
                    self.playerScores2.append(self.cardValues3[currentCard])
                elif self.splitHand==1:
                    self.playerScores.append(self.cardValues3[currentCard])
                elif self.splitHand==2:
                    self.playerScores2.append(self.cardValues3[currentCard])
            elif self.dealerHit==True:
                self.dealerScores.append(self.cardValues3[currentCard])
            if self.cardValues3[currentCard]>1 and self.cardValues3[currentCard]<7:
                self.counter3+=1
            elif self.cardValues3[currentCard]==1 or self.cardValues3[currentCard]>9:
                self.counter3-=1
            self.updateCount()
            self.updateScores()
            return self.cardValues3[currentCard]
        elif self.table==4:
            if len(self.currentCards)==0 or len(self.currentCards)==2:
                self.playerScores.append(self.cardValues4[currentCard])
            elif len(self.currentCards)==1:
                self.downCardScore+=self.cardValues4[currentCard]
            elif len(self.currentCards)==3:
               self.dealerScores.append(self.cardValues4[currentCard])
            elif self.dealerHit==False:
                if self.splitOn==False and len(self.currentCards)==5:
                    self.playerScores2.append(self.cardValues4[currentCard])
                elif self.splitHand==1:
                    self.playerScores.append(self.cardValues4[currentCard])
                elif self.splitHand==2:
                    self.playerScores2.append(self.cardValues4[currentCard])
            elif self.dealerHit==True:
                self.dealerScores.append(self.cardValues4[currentCard])
            if self.cardValues4[currentCard]>1 and self.cardValues4[currentCard]<7:
                self.counter4+=1
            elif self.cardValues4[currentCard]==1 or self.cardValues4[currentCard]>9:
                self.counter4-=1
            self.updateCount()
            self.updateScores()
            return self.cardValues4[currentCard]

    def removeCurrentCard(self, currentCard):
        """Removes the given card from its deck"""
        if self.table==1:
            self.deck1.pop(currentCard)
        elif self.table==2:
            self.deck2.pop(currentCard)
        elif self.table==3:
            self.deck3.pop(currentCard)
        elif self.table==4:
            self.deck4.pop(currentCard)

    def removeCurrentCardValue(self, currentCard):
        """Removes the corresponding value of the given card from its list of corresponding deck values"""
        if self.table==1:
            self.cardValues1.pop(currentCard)
        elif self.table==2:
            self.cardValues2.pop(currentCard)
        elif self.table==3:
            self.cardValues3.pop(currentCard)
        elif self.table==4:
            self.cardValues4.pop(currentCard)

    def getDeckLength(self):
        """Returns the length of the current deck"""
        if self.table==1:
            return len(self.deck1)
        elif self.table==2:
            return len(self.deck2)
        elif self.table==3:
            return len(self.deck3)
        elif self.table==4:
            return len(self.deck4)
                
    def updateCount(self):
        """Updates the count using a hi-lo count (2-6 = +1, 10-A = -1, 7-9 = Null)"""
        if self.table==1:
            self.counter1text.undraw()
            self.counter1text.setText("Count = " + str(self.counter1))
            self.counter1text.draw(self.win)
        elif self.table==2:
            self.counter2text.undraw()
            self.counter2text.setText("Count = " + str(self.counter2))
            self.counter2text.draw(self.win)
        elif self.table==3:
            self.counter3text.undraw()
            self.counter3text.setText("Count = " + str(self.counter3))
            self.counter3text.draw(self.win)
        elif self.table==4:
            self.counter4text.undraw()
            self.counter4text.setText("Count = " + str(self.counter4))
            self.counter4text.draw(self.win)

    def getCount(self):
        """Returns the count of the current table"""
        if self.table==1:
            return self.runningCount1
        elif self.table==2:
            return self.runningCount2
        elif self.table==3:
            return self.runningCount3
        elif self.table==4:
            return self.runningCount4

    def drawBankroll(self):
        """Updates the current total bankroll"""
        self.bankrolltext.undraw()
        self.bankrolltext.setText("Total Bankroll = $" + str(self.bankroll))
        self.bankrolltext.draw(self.win)

    def removeText(self):
        """Removes text from the environment"""
        self.hitText.undraw()
        self.standText.undraw()
        self.doubleDownText.undraw()
        self.splitText.undraw()
        self.blackjackText.undraw()
        self.playerBustText.undraw()
        self.dealerBustText.undraw()
        self.playerWinText.undraw()
        self.dealerWinText.undraw()
        self.pushText.undraw()
        
        self.hitText = Text(Point(380, 160), "Hit")
        self.hitText.setSize(18)
        self.hitText.setTextColor("white")
        self.standText = Text(Point(380, 160), "Stand")
        self.standText.setSize(18)
        self.standText.setTextColor("white")
        self.doubleDownText = Text(Point(380, 160), "Double Down")
        self.doubleDownText.setSize(18)
        self.doubleDownText.setTextColor("white")
        self.splitText = Text(Point(380, 160), "Split")
        self.splitText.setSize(18)
        self.splitText.setTextColor("white")
        self.blackjackText = Text(Point(380, 160), "Blackjack!")
        self.blackjackText.setSize(18)
        self.blackjackText.setTextColor("white")
        self.playerBustText = Text(Point(380, 160), "Player Bust")
        self.playerBustText.setSize(18)
        self.playerBustText.setTextColor("white")
        self.dealerBustText = Text(Point(380, 160), "Dealer Bust")
        self.dealerBustText.setSize(18)
        self.dealerBustText.setTextColor("white")
        self.playerWinText = Text(Point(380, 160), "Player Wins")
        self.playerWinText.setSize(18)
        self.playerWinText.setTextColor("white")
        self.dealerWinText = Text(Point(380, 160), "Dealer Wins")
        self.dealerWinText.setSize(18)
        self.dealerWinText.setTextColor("white")
        self.pushText = Text(Point(380, 160), "Push")
        self.pushText.setSize(18)
        self.pushText.setTextColor("white")

    def updateScores(self):
        """Updates the hand scores of the current table"""
        playerTotal=0
        playerTotal2=0
        dealerTotal=0
        self.playerScores.sort()
        self.playerScores2.sort()
        self.dealerScores.sort() 
        for i in self.playerScores:
            playerTotal+=i
        if len(self.playerScores)!=0:
            if self.playerScores[0]==1:
                if playerTotal<12:
                    playerTotal+=10
        for i in self.playerScores2:
            playerTotal2+=i
        if len(self.playerScores2)!=0:
            if self.playerScores2[0]==1:
                if playerTotal2<12:
                    playerTotal2+=10
        for i in self.dealerScores:
            dealerTotal+=i
        if len(self.dealerScores)!=0:
            if self.dealerScores[0]==1:
                if dealerTotal<12:
                    dealerTotal+=10
                    
        self.dealerScoreText.undraw()
        self.playerScoreText.undraw()
        self.playerScore2Text.undraw()
        self.dealerScoreText = Text(Point(230, 165), dealerTotal)
        self.dealerScoreText.setSize(18)
        self.dealerScoreText.setTextColor("white")
        self.dealerScoreText._move(self.moveRight, self.moveDown)
        self.dealerScoreText.draw(self.win)
        self.playerScoreText = Text(Point(230, 290), playerTotal)
        self.playerScoreText.setSize(18)
        self.playerScoreText.setTextColor("white")
        self.playerScoreText._move(self.moveRight, self.moveDown)
        self.playerScoreText.draw(self.win)
        if self.splitOn==False:
            self.playerScore2Text = Text(Point(285, 290), playerTotal2)
            self.playerScore2Text.setSize(18)
            self.playerScore2Text.setTextColor("white")
            self.playerScore2Text._move(self.moveRight, self.moveDown)
            self.playerScore2Text.draw(self.win)
            self.playerScoreText.undraw()
            if self.playerScoreText.getAnchor().x!=0:
                self.playerScoreText.getAnchor()._move(-self.playerScoreText.getAnchor().x, -self.playerScoreText.getAnchor().y)
            self.playerScoreText.move(-35,0)
            self.playerScoreText.draw(self.win)

    def playerTurn(self):
        """Manages the entire player strategy, using proven optimal black strategy"""
        time.sleep(.5)
        self.playerHand.sort()
        if self.playerHand[0]==self.playerHand[1] and len(self.playerHand)==2 and self.splitOn:
            if self.playerHand[0]==1 or self.playerHand[0]==8:
                self.split()
            elif self.playerHand[0]==10:
                self.stand(True)
            elif self.playerHand[0]==9:
                if self.dealerHand[1]==1 or self.dealerHand[1]==10 or self.dealerHand[1]==7:
                    self.stand(True)
                else:
                    self.split()
            elif self.playerHand[0]==7:
                if self.dealerHand[1]>6 or self.dealerHand[1]==1:
                    self.hit(True)
                else:
                    self.split()
            elif self.playerHand[0]==6:
                if self.dealerHand[1]>6 or self.dealerHand[1]<3:
                    self.hit(True)
                else:
                    self.split()
            elif self.playerHand[0]==5:
                if self.dealerHand[1]==10 or self.dealerHand[1]==1:
                    self.hit(True)
                else:
                    self.doubleDown()
            elif self.playerHand[0]==4:
                self.hit(True)
            elif self.playerHand[0]==3 or self.playerHand[0]==2:
                if self.dealerHand[1]>6 or self.dealerHand[1]<4:
                    self.hit(True)
                else:
                    self.split()
        else:
            player=0
            doubleOn=False
            doubleOn2=False
            self.playerHand2.sort()
            if self.splitHand==1:
                for i in self.playerHand:
                    player+=i
                temp=self.playerHand[0]
                if len(self.playerHand)==2:
                    doubleOn=True
                    doubleOn2=False
            elif self.splitHand==2:
                for i in self.playerHand2:
                    player+=i
                temp=self.playerHand2[0]
                if len(self.playerHand2)==2:
                    doubleOn=False
                    doubleOn2=True
            if temp==1 and player<12:
                player-=1
                if player==10:
                    if self.splitHand==1:
                        if len(self.playerScores)==2:
                            self.blackjack()
                        else:
                            self.stand(True)
                    elif self.splitHand==2:
                        if len(self.playerScores2)==2:
                            self.blackjack()
                        else:
                            self.stand(True)
                elif player>7:
                    self.stand(True)
                elif player==7:
                    if self.dealerHand[1]>8 or self.dealerHand[1]==1:
                        self.hit(True)
                    elif self.dealerHand[1]>6 or self.dealerHand[1]==2:
                        self.stand(True)
                    else:
                        if doubleOn or doubleOn2:
                            self.doubleDown()
                        else:
                            self.hit(True)
                elif player==6:
                    if self.dealerHand[1]>6 or self.dealerHand[1]==2:
                        self.hit(True)
                    else:
                        if doubleOn or doubleOn2:
                            self.doubleDown()
                        else:
                            self.hit(True)
                elif player==5 or player==4:
                    if self.dealerHand[1]>6 or self.dealerHand[1]<4:
                        self.hit(True)
                    else:
                        if doubleOn or doubleOn2:
                            self.doubleDown()
                        else:
                            self.hit(True)
                elif player==3 or player==2:
                    if self.dealerHand[1]>6 or self.dealerHand[1]<5:
                        self.hit(True)
                    else:
                        if doubleOn or doubleOn2:
                            self.doubleDown()
                        else:
                            self.hit(True)
                elif player==1:
                    self.hit(True)
            else:
                if player>21:
                    self.playerBust()
                elif player>16:
                    self.stand(True)
                elif player>12:
                    if self.dealerHand[1]>6 or self.dealerHand[1]==1:
                        self.hit(True)
                    else:
                        self.stand(True)
                elif player==12:
                    if self.dealerHand[1]>6 or self.dealerHand[1]<4:
                        self.hit(True)
                    else:
                        self.stand(True)
                elif player==11:
                    if self.dealerHand[1]==1:
                        self.hit(True)
                    else:
                        if doubleOn or doubleOn2:
                            self.doubleDown()
                        else:
                            self.hit(True)
                elif player==10:
                    if self.dealerHand[1]==10 or self.dealerHand[1]==1:
                        self.hit(True)
                    else:
                        if doubleOn or doubleOn2:
                            self.doubleDown()
                        else:
                            self.hit(True)
                elif player==9:
                    if self.dealerHand[1]>6 or self.dealerHand[1]<3:
                        self.hit(True)
                    else:
                        if doubleOn or doubleOn2:
                            self.doubleDown()
                        else:
                            self.hit(True)
                elif player<9:
                    self.hit(True)

    def dealerTurn(self):
        """Manages the entire dealer "strategy", using dealer's rules of hitting<17 and standing>=17"""
        self.dealerHit=True
        self.downCard.undraw()
        if len(self.dealerScores)==1:
            self.dealerScores.append(self.downCardScore)
        self.updateScores()
        time.sleep(.5)
        dealer=0
        self.dealerHand.sort()
        for i in self.dealerHand:
            dealer+=i
        if dealer>21:
            self.dealerBust()
        elif dealer>16 or (self.dealerHand[0]==1 and dealer+10>16 and dealer+10<22):
            self.stand(False)
        else:
            self.hit(False)

    def hit(self, playerHit):
        """Hit function, displays a new card added to one's hand"""
        time.sleep(.5)
        self.removeText()
        self.hitText._move(self.moveRight, self.moveDown)
        self.hitText.draw(self.win)
        currentCard = random.randrange(self.getDeckLength())
        if playerHit:
            self.currentCards.append(self.getCurrentCard(currentCard))
            if self.splitOn:
                self.playerHand.append(self.getCurrentCardValue(currentCard))
                if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
                    self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
                self.currentCards[len(self.currentCards)-1]._move(265+len(self.playerHand)*10, 290)
            elif self.splitHand==1:
                self.playerHand.append(self.getCurrentCardValue(currentCard))
                if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
                    self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
                self.currentCards[len(self.currentCards)-1]._move(225+len(self.playerHand)*10, 290)
            else:
                self.playerHand2.append(self.getCurrentCardValue(currentCard))
                if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
                    self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
                self.currentCards[len(self.currentCards)-1]._move(315+len(self.playerHand2)*10, 290)
            self.currentCards[len(self.currentCards)-1]._move(self.moveRight, self.moveDown)
            self.currentCards[len(self.currentCards)-1].draw(self.win)
            self.removeCurrentCard(currentCard)
            self.removeCurrentCardValue(currentCard)
            self.playerTurn()
        else:
            self.dealerHand.append(self.getCurrentCardValue(currentCard))
            self.currentCards.append(self.getCurrentCard(currentCard))
            if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
                self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
            self.currentCards[len(self.currentCards)-1]._move(265+len(self.dealerHand)*10, 165)
            self.currentCards[len(self.currentCards)-1]._move(self.moveRight, self.moveDown)
            self.currentCards[len(self.currentCards)-1].draw(self.win)
            self.removeCurrentCard(currentCard)
            self.removeCurrentCardValue(currentCard)
            self.dealerTurn()
            
    def stand(self, playerStand):
        """Stand function"""
        time.sleep(.5)
        self.removeText()
        self.standText._move(self.moveRight, self.moveDown)
        self.standText.draw(self.win)
        if playerStand:
            if self.splitOn:
                time.sleep(.5)
                self.dealerTurn()
            elif self.splitHand==1:
                self.splitHand=2
                self.playerTurn()
            elif self.splitHand==2:
                time.sleep(.5)
                self.dealerTurn()
        else:
            self.awardWinner()
            
    def doubleDown(self):
        """Double down function, displays a new card added to one's hand and doubles the bet"""
        time.sleep(.5)
        self.removeText()
        self.doubleDownText._move(self.moveRight, self.moveDown)
        self.doubleDownText.draw(self.win)
        currentCard = random.randrange(self.getDeckLength())
        if self.splitOn:
            self.doubleDown1=True
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                self.chip10kClone2._move(0,-3)
                self.chip10kClone2.draw(self.win)
            else:
                self.chip100Clone2._move(0,-3)
                self.chip100Clone2.draw(self.win)
            time.sleep(.5)
            self.playerHand.append(self.getCurrentCardValue(currentCard))
        elif self.splitHand==1:
            self.doubleDown1=True
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                self.chip10kClone2._move(-40,-3)
                self.chip10kClone2.draw(self.win)
            else:
                self.chip100Clone2._move(-40,-3)
                self.chip100Clone2.draw(self.win)
            time.sleep(.5)
            self.playerHand.append(self.getCurrentCardValue(currentCard))
        else:
            self.doubleDown2=True
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                self.chip10kClone3._move(50,-3)
                self.chip10kClone3.draw(self.win)
            else:
                self.chip100Clone3._move(50,-3)
                self.chip100Clone3.draw(self.win)
            time.sleep(.5)
            self.playerHand2.append(self.getCurrentCardValue(currentCard))
        self.currentCards.append(self.getCurrentCard(currentCard))
        if self.splitOn:
            if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
                self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
            self.currentCards[len(self.currentCards)-1]._move(295, 290)
        elif self.splitHand==1:
            if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
                self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
            self.currentCards[len(self.currentCards)-1]._move(255, 290)
        else:
            if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
                self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
            self.currentCards[len(self.currentCards)-1]._move(345, 290)
        self.currentCards[len(self.currentCards)-1]._move(self.moveRight, self.moveDown)
        self.currentCards[len(self.currentCards)-1].draw(self.win)
        self.removeCurrentCard(currentCard)
        self.removeCurrentCardValue(currentCard)
        if self.splitOn:
            time.sleep(.5)
            self.dealerTurn()
        elif self.splitHand==1:
            self.splitHand=2
            self.playerTurn()
        elif self.splitHand==2:
            time.sleep(.5)
            self.dealerTurn()
            
    def split(self):
        """Split function, split's the player's hand into two hands, deals a card to each, and doubles the bet"""
        time.sleep(.5)
        self.removeText()
        self.splitText._move(self.moveRight, self.moveDown)
        self.splitText.draw(self.win)
        self.currentCards[0].undraw()
        self.currentCards[0]._move(-40, 0)
        self.currentCards[0].draw(self.win)
        self.playerScores.pop()
        self.currentCards[2].undraw()
        self.currentCards[2]._move(40, 0)
        self.currentCards[2].draw(self.win)
        self.playerScores2.append(self.playerScores[0])

        currentCount=self.getCount()
        if self.splitOn:
            if currentCount>self.countThreshold:
                self.chip10k.undraw()
                self.chip10k._move(-40,0)
                self.chip10k.draw(self.win)
                self.chip10kClone._move(50,0)
                self.chip10kClone.draw(self.win)
            else:
                self.chip100.undraw()
                self.chip100._move(-40,0)
                self.chip100.draw(self.win)
                self.chip100Clone._move(50,0)
                self.chip100Clone.draw(self.win)
        
        self.splitOn=False
        self.updateScores()
        
        time.sleep(.5)
        self.playerHand2.append(self.playerHand[1])
        self.playerHand.pop()
        currentCard = random.randrange(self.getDeckLength())
        self.playerHand.append(self.getCurrentCardValue(currentCard))
        self.currentCards.append(self.getCurrentCard(currentCard))
        if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
            self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
        self.currentCards[len(self.currentCards)-1]._move(245, 290)
        self.currentCards[len(self.currentCards)-1]._move(self.moveRight, self.moveDown)
        self.currentCards[len(self.currentCards)-1].draw(self.win)
        self.removeCurrentCard(currentCard)
        self.removeCurrentCardValue(currentCard)
        currentCard = random.randrange(self.getDeckLength())
        self.playerHand2.append(self.getCurrentCardValue(currentCard))
        self.currentCards.append(self.getCurrentCard(currentCard))
        if self.currentCards[len(self.currentCards)-1].getAnchor().x!=0:
            self.currentCards[len(self.currentCards)-1]._move(-self.currentCards[len(self.currentCards)-1].getAnchor().x, -self.currentCards[len(self.currentCards)-1].getAnchor().y)
        self.currentCards[len(self.currentCards)-1]._move(335, 290)
        self.currentCards[len(self.currentCards)-1]._move(self.moveRight, self.moveDown)
        self.currentCards[len(self.currentCards)-1].draw(self.win)
        self.removeCurrentCard(currentCard)
        self.removeCurrentCardValue(currentCard)            
        self.playerTurn()
        
    def dealerBust(self):
        """Called when dealer's hand goes over 21, awards chips to player"""
        self.removeText()
        self.dealerBustText._move(self.moveRight, self.moveDown)
        self.dealerBustText.draw(self.win)
        currentCount=self.getCount()
        if self.splitOn:
            if currentCount>self.countThreshold:
                for i in range(3):
                    self.chip10k.undraw()
                    self.chip10k._move(0,20)
                    self.chip10k.draw(self.win)
                    if self.doubleDown1:
                        self.chip10kClone2.undraw()
                        self.chip10kClone2._move(0,20)
                        self.chip10kClone2.draw(self.win)
                    time.sleep(.1)
                self.chip10k.undraw()
                if self.doubleDown1:
                    self.chip10kClone2.undraw()
                    self.bankroll+=10000
                    self.winnings+=10000
                self.bankroll+=10000
                self.winnings+=10000
            else:
                for i in range(3):
                    self.chip100.undraw()
                    self.chip100._move(0,20)
                    self.chip100.draw(self.win)
                    if self.doubleDown1:
                        self.chip100Clone2.undraw()
                        self.chip100Clone2._move(0,20)
                        self.chip100Clone2.draw(self.win)
                    time.sleep(.1)
                self.chip100.undraw()
                if self.doubleDown1:
                    self.chip100Clone2.undraw()
                    self.bankroll+=100
                    self.winnings+=100
                self.bankroll+=100
                self.winnings+=100
        else:
            playerTotal=0
            playerTotal2=0
            self.playerScores.sort()
            self.playerScores2.sort()
            for i in self.playerScores:
                playerTotal+=i
            if len(self.playerScores)!=0:
                if self.playerScores[0]==1:
                    if playerTotal<12:
                        playerTotal+=10
            for i in self.playerScores2:
                playerTotal2+=i
            if len(self.playerScores2)!=0:
                if self.playerScores2[0]==1:
                    if playerTotal2<12:
                        playerTotal2+=10
            if playerTotal<21 or (playerTotal==21 and len(self.playerScores)!=2):
                if currentCount>self.countThreshold:
                    for i in range(3):
                        self.chip10k.undraw()
                        self.chip10k._move(13,20)
                        self.chip10k.draw(self.win)
                        if self.doubleDown1:
                            self.chip10kClone2.undraw()
                            self.chip10kClone2._move(13,20)
                            self.chip10kClone2.draw(self.win)
                        time.sleep(.1)
                    self.chip10k.undraw()
                    if self.doubleDown1:
                        self.chip10kClone2.undraw()
                        self.bankroll+=10000
                        self.winnings+=10000
                    self.bankroll+=10000
                    self.winnings+=10000
                else:
                    for i in range(3):
                        self.chip100.undraw()
                        self.chip100._move(13,20)
                        self.chip100.draw(self.win)
                        if self.doubleDown1:
                            self.chip100Clone2.undraw()
                            self.chip100Clone2._move(13,20)
                            self.chip100Clone2.draw(self.win)
                        time.sleep(.1)
                    self.chip100.undraw()
                    if self.doubleDown1:
                        self.chip100Clone2.undraw()
                        self.bankroll+=100
                        self.winnings+=100
                    self.bankroll+=100
                    self.winnings+=100
                time.sleep(.5)
            if playerTotal2<21 or (playerTotal2==21 and len(self.playerScores2)!=2):
                if currentCount>self.countThreshold:
                    for i in range(3):
                        self.chip10kClone.undraw()
                        self.chip10kClone._move(-17,20)
                        self.chip10kClone.draw(self.win)
                        if self.doubleDown2:
                            self.chip10kClone3.undraw()
                            self.chip10kClone3._move(-17,20)
                            self.chip10kClone3.draw(self.win)
                        time.sleep(.1)
                    self.chip10kClone.undraw()
                    if self.doubleDown2:
                        self.chip10kClone3.undraw()
                        self.bankroll-=10000
                        self.winnings-=10000
                    self.bankroll-=10000
                    self.winnings-=10000
                else:
                    for i in range(3):
                        self.chip100Clone.undraw()
                        self.chip100Clone._move(-17,20)
                        self.chip100Clone.draw(self.win)
                        if self.doubleDown2:
                            self.chip100Clone3.undraw()
                            self.chip100Clone3._move(-17,20)
                            self.chip100Clone3.draw(self.win)
                        time.sleep(.1)
                    self.chip100Clone.undraw()
                    if self.doubleDown2:
                        self.chip100Clone3.undraw()
                        self.bankroll-=100
                        self.winnings-=100
                    self.bankroll-=100
                    self.winnings-=100
        self.drawBankroll()

    def playerBust(self):
        """Called when player's hand goes over 21, awards chips to dealer"""
        self.removeText()
        self.playerBustText._move(self.moveRight, self.moveDown)
        self.playerBustText.draw(self.win)
        if self.splitOn:
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                for i in range(3):
                    self.chip10k.undraw()
                    self.chip10k._move(0,-20)
                    self.chip10k.draw(self.win)
                    if self.doubleDown1:
                        self.chip10kClone2.undraw()
                        self.chip10kClone2._move(0,-20)
                        self.chip10kClone2.draw(self.win)
                    time.sleep(.1)
                self.chip10k.undraw()
                if self.doubleDown1:
                    self.chip10kClone2.undraw()
                    self.bankroll-=10000
                    self.winnings-=10000
                self.bankroll-=10000
                self.winnings-=10000
            else:
                for i in range(3):
                    self.chip100.undraw()
                    self.chip100._move(0,-20)
                    self.chip100.draw(self.win)
                    if self.doubleDown1:
                        self.chip100Clone2.undraw()
                        self.chip100Clone2._move(0,-20)
                        self.chip100Clone2.draw(self.win)
                    time.sleep(.1)
                self.chip100.undraw()
                if self.doubleDown1:
                    self.chip100Clone2.undraw()
                    self.bankroll-=100
                    self.winnings-=100
                self.bankroll-=100
                self.winnings-=100
            self.drawBankroll()
        elif self.splitHand==1:
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                for i in range(3):
                    self.chip10k.undraw()
                    self.chip10k._move(13,-20)
                    self.chip10k.draw(self.win)
                    if self.doubleDown1:
                        self.chip10kClone2.undraw()
                        self.chip10kClone2._move(13,-20)
                        self.chip10kClone2.draw(self.win)
                    time.sleep(.1)
                self.chip10k.undraw()
                if self.doubleDown1:
                    self.chip10kClone2.undraw()
                    self.bankroll-=10000
                    self.winnings-=10000
                self.bankroll-=10000
                self.winnings-=10000
            else:
                for i in range(3):
                    self.chip100.undraw()
                    self.chip100._move(13,-20)
                    self.chip100.draw(self.win)
                    if self.doubleDown1:
                        self.chip100Clone2.undraw()
                        self.chip100Clone2._move(13,-20)
                        self.chip100Clone2.draw(self.win)
                    time.sleep(.1)
                self.chip100.undraw()
                if self.doubleDown1:
                    self.chip100Clone2.undraw()
                    self.bankroll-=100
                    self.winnings-=100
                self.bankroll-=100
                self.winnings-=100
            self.drawBankroll()
            self.splitHand=2
            self.playerTurn()
        else:
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                for i in range(3):
                    self.chip10kClone.undraw()
                    self.chip10kClone._move(-17,-20)
                    self.chip10kClone.draw(self.win)
                    if self.doubleDown2:
                        self.chip10kClone3.undraw()
                        self.chip10kClone3._move(-17,-20)
                        self.chip10kClone3.draw(self.win)
                    time.sleep(.1)
                self.chip10kClone.undraw()
                if self.doubleDown2:
                    self.chip10kClone3.undraw()
                    self.bankroll-=10000
                    self.winnings-=10000
                self.bankroll-=10000
                self.winnings-=10000
            else:
                for i in range(3):
                    self.chip100Clone.undraw()
                    self.chip100Clone._move(-17,-20)
                    self.chip100Clone.draw(self.win)
                    if self.doubleDown2:
                        self.chip100Clone3.undraw()
                        self.chip100Clone3._move(-17,-20)
                        self.chip100Clone3.draw(self.win)
                    time.sleep(.1)
                self.chip100Clone.undraw()
                if self.doubleDown2:
                    self.chip100Clone3.undraw()
                    self.bankroll-=100
                    self.winnings-=100
                self.bankroll-=100
                self.winnings-=100
            self.drawBankroll()
            self.dealerTurn()

    def blackjack(self):
        """Called when player's gets a blackjack, awards chips to player"""
        self.removeText()
        self.blackjackText._move(self.moveRight, self.moveDown)
        self.blackjackText.draw(self.win)
        if self.splitOn:
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                for i in range(3):
                    self.chip10k.undraw()
                    self.chip10k._move(0,20)
                    self.chip10k.draw(self.win)
                    time.sleep(.1)
                self.chip10k.undraw()
                self.bankroll+=15000
                self.winnings+=15000
            else:
                for i in range(3):
                    self.chip100.undraw()
                    self.chip100._move(0,20)
                    self.chip100.draw(self.win)
                    time.sleep(.1)
                self.chip100.undraw()
                self.bankroll+=150
                self.winnings+=150
            self.drawBankroll()
        elif self.splitHand==1:
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                for i in range(3):
                    self.chip10k.undraw()
                    self.chip10k._move(13,20)
                    self.chip10k.draw(self.win)
                    time.sleep(.1)
                self.chip10k.undraw()
                self.splitHand=2
                self.bankroll+=15000
                self.winnings+=15000
            else:
                for i in range(3):
                    self.chip100.undraw()
                    self.chip100._move(13,20)
                    self.chip100.draw(self.win)
                    time.sleep(.1)
                self.chip100.undraw()
                self.splitHand=2
                self.bankroll+=150
                self.winnings+=150
            self.drawBankroll()
            self.playerTurn()
        else:
            currentCount=self.getCount()
            if currentCount>self.countThreshold:
                for i in range(3):
                    self.chip10kClone.undraw()
                    self.chip10kClone._move(-17,20)
                    self.chip10kClone.draw(self.win)
                    time.sleep(.1)
                self.chip10kClone.undraw()
                self.bankroll+=15000
                self.winnings+=15000
            else:
                for i in range(3):
                    self.chip100Clone.undraw()
                    self.chip100Clone._move(-17,20)
                    self.chip100Clone.draw(self.win)
                    time.sleep(.1)
                self.chip100Clone.undraw()
                self.bankroll+=150
                self.winnings+=150
            self.drawBankroll()
            self.playerHand.sort()
            player=0
            for i in self.playerHand:
                player+=i
            if self.playerHand[0]==1 and player+10<22:
                player+=10
            if player<21 or (player==21 and len(self.playerScores)!=2):
                self.dealerTurn()
        
    def awardWinner(self):
        """Awards chips to the winning hand, or removes chips if the hands are tied"""
        self.playerHand.sort()
        self.dealerHand.sort()
        player=0
        for i in self.playerHand:
            player+=i
        dealer=0
        for i in self.dealerHand:
            dealer+=i
        if self.playerHand[0]==1 and player+10<22:
            player+=10
        if self.dealerHand[0]==1 and dealer+10<22:
            dealer+=10
        if self.splitOn:
            if player>dealer:
                self.removeText()
                self.playerWinText._move(self.moveRight, self.moveDown)
                self.playerWinText.draw(self.win)
                currentCount=self.getCount()
                if currentCount>self.countThreshold:
                    for i in range(3):
                        self.chip10k.undraw()
                        self.chip10k._move(0,20)
                        self.chip10k.draw(self.win)
                        if self.doubleDown1:
                            self.chip10kClone2.undraw()
                            self.chip10kClone2._move(0,20)
                            self.chip10kClone2.draw(self.win)
                        time.sleep(.1)
                    self.chip10k.undraw()
                    if self.doubleDown1:
                        self.chip10kClone2.undraw()
                        self.bankroll+=10000
                        self.winnings+=10000
                    self.bankroll+=10000
                    self.winnings+=10000
                else:
                    for i in range(3):
                        self.chip100.undraw()
                        self.chip100._move(0,20)
                        self.chip100.draw(self.win)
                        if self.doubleDown1:
                            self.chip100Clone2.undraw()
                            self.chip100Clone2._move(0,20)
                            self.chip100Clone2.draw(self.win)
                        time.sleep(.1)
                    self.chip100.undraw()
                    if self.doubleDown1:
                        self.chip100Clone2.undraw()
                        self.bankroll+=100
                        self.winnings+=100
                    self.bankroll+=100
                    self.winnings+=100
                self.drawBankroll()
            elif player<dealer:
                self.removeText()
                self.dealerWinText._move(self.moveRight, self.moveDown)
                self.dealerWinText.draw(self.win)
                currentCount=self.getCount()
                if currentCount>self.countThreshold:
                    for i in range(3):
                        self.chip10k.undraw()
                        self.chip10k._move(0,-20)
                        self.chip10k.draw(self.win)
                        if self.doubleDown1:
                            self.chip10kClone2.undraw()
                            self.chip10kClone2._move(0,-20)
                            self.chip10kClone2.draw(self.win)
                        time.sleep(.1)
                    self.chip10k.undraw()
                    if self.doubleDown1:
                        self.chip10kClone2.undraw()
                        self.bankroll-=10000
                        self.winnings-=10000
                    self.bankroll-=10000
                    self.winnings-=10000
                else:
                    for i in range(3):
                        self.chip100.undraw()
                        self.chip100._move(0,-20)
                        self.chip100.draw(self.win)
                        if self.doubleDown1:
                            self.chip100Clone2.undraw()
                            self.chip100Clone2._move(0,-20)
                            self.chip100Clone2.draw(self.win)
                        time.sleep(.1)
                    self.chip100.undraw()
                    if self.doubleDown1:
                        self.chip100Clone2.undraw()
                        self.bankroll-=100
                        self.winnings-=100
                    self.bankroll-=100
                    self.winnings-=100
                self.drawBankroll()
            elif player==dealer:
                self.removeText()
                self.pushText._move(self.moveRight, self.moveDown)
                self.pushText.draw(self.win)
                currentCount=self.getCount()
                if currentCount>self.countThreshold:
                    self.chip10k.undraw()
                    if self.doubleDown1:
                        self.chip10kClone2.undraw()
                else:
                    self.chip100.undraw()
                    if self.doubleDown1:
                        self.chip100Clone2.undraw()
        else:
            if player<21 or (player==21 and len(self.playerScores)!=2):
                if player>dealer and player<22:
                    self.removeText()
                    self.playerWinText._move(self.moveRight, self.moveDown)
                    self.playerWinText.draw(self.win)
                    currentCount=self.getCount()
                    if currentCount>self.countThreshold:
                        for i in range(3):
                            self.chip10k.undraw()
                            self.chip10k._move(13,20)
                            self.chip10k.draw(self.win)
                            if self.doubleDown1:
                                self.chip10kClone2.undraw()
                                self.chip10kClone2._move(13,20)
                                self.chip10kClone2.draw(self.win)
                            time.sleep(.1)
                        self.chip10k.undraw()
                        if self.doubleDown1:
                            self.chip10kClone2.undraw()
                            self.bankroll+=10000
                            self.winnings+=10000
                        self.bankroll+=10000
                        self.winnings+=10000
                    else:
                        for i in range(3):
                            self.chip100.undraw()
                            self.chip100._move(13,20)
                            self.chip100.draw(self.win)
                            if self.doubleDown1:
                                self.chip100Clone2.undraw()
                                self.chip100Clone2._move(13,20)
                                self.chip100Clone2.draw(self.win)
                            time.sleep(.1)
                        self.chip100.undraw()
                        if self.doubleDown1:
                            self.chip100Clone2.undraw()
                            self.bankroll+=100
                            self.winnings+=100
                        self.bankroll+=100
                        self.winnings+=100
                    self.drawBankroll()
                elif player<dealer and player<22:
                    self.removeText()
                    self.dealerWinText._move(self.moveRight, self.moveDown)
                    self.dealerWinText.draw(self.win)
                    currentCount=self.getCount()
                    if currentCount>self.countThreshold:
                        for i in range(3):
                            self.chip10k.undraw()
                            self.chip10k._move(13,-20)
                            self.chip10k.draw(self.win)
                            if self.doubleDown1:
                                self.chip10kClone2.undraw()
                                self.chip10kClone2._move(13,-20)
                                self.chip10kClone2.draw(self.win)
                            time.sleep(.1)
                        self.chip10k.undraw()
                        if self.doubleDown1:
                            self.chip10kClone2.undraw()
                            self.bankroll-=10000
                            self.winnings-=10000
                        self.bankroll-=10000
                        self.winnings-=10000
                    else:
                        for i in range(3):
                            self.chip100.undraw()
                            self.chip100._move(13,-20)
                            self.chip100.draw(self.win)
                            if self.doubleDown1:
                                self.chip100Clone2.undraw()
                                self.chip100Clone2._move(13,-20)
                                self.chip100Clone2.draw(self.win)
                            time.sleep(.1)
                        self.chip100.undraw()
                        if self.doubleDown1:
                            self.chip100Clone2.undraw()
                            self.bankroll-=100
                            self.winnings-=100
                        self.bankroll-=100
                        self.winnings-=100
                    self.drawBankroll()
                elif player==dealer:
                    self.removeText()
                    self.pushText._move(self.moveRight, self.moveDown)
                    self.pushText.draw(self.win)
                    currentCount=self.getCount()
                    if currentCount>self.countThreshold:
                        self.chip10k.undraw()
                        if self.doubleDown1:
                            self.chip10kClone2.undraw()
                    else:
                        self.chip100.undraw()
                        if self.doubleDown1:
                            self.chip100Clone2.undraw()
            time.sleep(.5)
            self.playerHand2.sort()
            player2=0
            for i in self.playerHand2:
                player2+=i
            if self.playerHand2[0]==1 and player2+10<22:
                player2+=10
            if player2<21 or (player2==21 and len(self.playerScores2)!=2):
                if player2>dealer and player2<22:
                    self.removeText()
                    self.playerWinText._move(self.moveRight, self.moveDown)
                    self.playerWinText.draw(self.win)
                    currentCount=self.getCount()
                    if currentCount>self.countThreshold:
                        for i in range(3):
                            self.chip10kClone.undraw()
                            self.chip10kClone._move(-17,20)
                            self.chip10kClone.draw(self.win)
                            if self.doubleDown2:
                                self.chip10kClone3.undraw()
                                self.chip10kClone3._move(-17,20)
                                self.chip10kClone3.draw(self.win)
                            time.sleep(.1)
                        self.chip10kClone.undraw()
                        if self.doubleDown2:
                            self.chip10kClone3.undraw()
                            self.bankroll+=10000
                            self.winnings+=10000
                        self.bankroll+=10000
                        self.winnings+=10000
                    else:
                        for i in range(3):
                            self.chip100Clone.undraw()
                            self.chip100Clone._move(-17,20)
                            self.chip100Clone.draw(self.win)
                            if self.doubleDown2:
                                self.chip100Clone3.undraw()
                                self.chip100Clone3._move(-17,20)
                                self.chip100Clone3.draw(self.win)
                            time.sleep(.1)
                        self.chip100Clone.undraw()
                        if self.doubleDown2:
                            self.chip100Clone3.undraw()
                            self.bankroll+=100
                            self.winnings+=100
                        self.bankroll+=100
                        self.winnings+=100
                    self.drawBankroll()
                elif player2<dealer and player2<22:
                    self.removeText()
                    self.dealerWinText._move(self.moveRight, self.moveDown)
                    self.dealerWinText.draw(self.win)
                    currentCount=self.getCount()
                    if currentCount>self.countThreshold:
                        for i in range(3):
                            self.chip10kClone.undraw()
                            self.chip10kClone._move(-17,-20)
                            self.chip10kClone.draw(self.win)
                            if self.doubleDown2:
                                self.chip10kClone3.undraw()
                                self.chip10kClone3._move(-17,-20)
                                self.chip10kClone3.draw(self.win)
                            time.sleep(.1)
                        self.chip10kClone.undraw()
                        if self.doubleDown2:
                            self.chip10kClone3.undraw()
                            self.bankroll-=10000
                            self.winnings-=10000
                        self.bankroll-=10000
                        self.winnings-=10000
                    else:
                        for i in range(3):
                            self.chip100Clone.undraw()
                            self.chip100Clone._move(-17,-20)
                            self.chip100Clone.draw(self.win)
                            if self.doubleDown2:
                                self.chip100Clone3.undraw()
                                self.chip100Clone3._move(-17,-20)
                                self.chip100Clone3.draw(self.win)
                            time.sleep(.1)
                        self.chip100Clone.undraw()
                        if self.doubleDown2:
                            self.chip100Clone3.undraw()
                            self.bankroll-=100
                            self.winnings-=100
                        self.bankroll-=100
                        self.winnings-=100
                    self.drawBankroll()
                elif player2==dealer:
                    self.removeText()
                    self.pushText._move(self.moveRight, self.moveDown)
                    self.pushText.draw(self.win)
                    currentCount=self.getCount()
                    if currentCount>self.countThreshold:
                        self.chip10kClone.undraw()
                        if self.doubleDown2:
                            self.chip10kClone3.undraw()
                    else:
                        self.chip100Clone.undraw()
                        if self.doubleDown2:
                            self.chip100Clone3.undraw()
            
def blackjack(workbook, sheet, handCounter, winnings):
    """Main function which sets up framework of the algorithm, and creates many global variables"""
    win=GraphWin("Blackjack",1100,800)
    newEnvironment=Environment(win)
    newEnvironment.drawTables()
    deck1,deck2,deck3,deck4,downCardOriginal,cardValues1,cardValues2,cardValues3,cardValues4=newEnvironment.makeDecks()
    chip100Original,chip10kOriginal=newEnvironment.makeChips()
    currentCards=[]
    tempCurrentCards=[]
    tempCurrentCards2=[]
    tempCurrentCards3=[]
    tempCurrentCards4=[]
    splitOn=True;
    playerHand=[]
    playerHand2=[]
    dealerHand=[]
    splitHand=1
    doubleDown1=False
    doubleDown2=False
    table=1
    moveRight=0
    moveDown=0
    runningCount1=0
    runningCount2=0
    runningCount3=0
    runningCount4=0
    counter1=0
    counter2=0
    counter3=0
    counter4=0
    counter1text = Text(Point(70, 390), "Count = " + str(counter1))
    counter1text.setSize(24)
    counter1text.setTextColor("light blue")
    counter1text.draw(win)
    counter2text = Text(Point(620, 390), "Count = " + str(counter2))
    counter2text.setSize(24)
    counter2text.setTextColor("light blue")
    counter2text.draw(win)
    counter3text = Text(Point(70, 780), "Count = " + str(counter3))
    counter3text.setSize(24)
    counter3text.setTextColor("light blue")
    counter3text.draw(win)
    counter4text = Text(Point(620, 780), "Count = " + str(counter4))
    counter4text.setSize(24)
    counter4text.setTextColor("light blue")
    counter4text.draw(win)
    bankroll = 500000
    bankrolltext = Text(Point(550, 20), "Total Bankroll = $" + str(bankroll))
    bankrolltext.setSize(24)
    bankrolltext.setTextColor("light blue")
    bankrolltext.draw(win)
    hitText = Text(Point(380, 160), "Hit")
    hitText.setSize(18)
    hitText.setTextColor("white")
    standText = Text(Point(380, 160), "Stand")
    standText.setSize(18)
    standText.setTextColor("white")
    doubleDownText = Text(Point(380, 160), "Double Down")
    doubleDownText.setSize(18)
    doubleDownText.setTextColor("white")
    splitText = Text(Point(380, 160), "Split")
    splitText.setSize(18)
    splitText.setTextColor("white")
    blackjackText = Text(Point(380, 160), "Blackjack!")
    blackjackText.setSize(18)
    blackjackText.setTextColor("white")
    playerBustText = Text(Point(380, 160), "Player Bust")
    playerBustText.setSize(18)
    playerBustText.setTextColor("white")
    dealerBustText = Text(Point(380, 160), "Dealer Bust")
    dealerBustText.setSize(18)
    dealerBustText.setTextColor("white")
    playerWinText = Text(Point(380, 160), "Player Wins")
    playerWinText.setSize(18)
    playerWinText.setTextColor("white")
    dealerWinText = Text(Point(380, 160), "Dealer Wins")
    dealerWinText.setSize(18)
    dealerWinText.setTextColor("white")
    pushText = Text(Point(380, 160), "Push")
    pushText.setSize(18)
    pushText.setTextColor("white")
    dealerScores = []
    dealerScoreText = Text(Point(230, 165), 0)
    dealerScoreText.setSize(18)
    dealerScoreText.setTextColor("white")
    playerScores = []
    playerScoreText = Text(Point(230, 290), 0)
    playerScoreText.setSize(18)
    playerScoreText.setTextColor("white")
    playerScores2 = []
    playerScore2Text = Text(Point(285, 290), 0)
    playerScore2Text.setSize(18)
    playerScore2Text.setTextColor("white")
    downCardScore = 0
    countThreshold = 9
    dealerHit=False
    cardOriginal=Image(Point(0,0), "back102.gif")
    newGame=Blackjack(win, workbook, sheet, handCounter, winnings, deck1, deck2, deck3, deck4, cardOriginal, downCardOriginal, currentCards, tempCurrentCards, tempCurrentCards2, tempCurrentCards3, tempCurrentCards4, cardValues1, cardValues2, cardValues3, cardValues4, playerHand, playerHand2, dealerHand, chip100Original, chip10kOriginal, splitOn, splitHand, doubleDown1, doubleDown2, table, moveRight, moveDown, counter1, runningCount1, runningCount2, runningCount3, runningCount4, counter2, counter3, counter4, counter1text, counter2text, counter3text, counter4text, bankroll, bankrolltext, countThreshold, hitText, standText, doubleDownText, splitText, blackjackText, playerBustText, dealerBustText, playerWinText, dealerWinText, pushText, dealerScoreText, playerScoreText, playerScore2Text, dealerScores, playerScores, playerScores2, downCardScore, dealerHit)
    newGame.startGame()
    
if __name__ == "__main__":
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('Game Results')
    handCounter=0
    winnings=0
    blackjack(workbook, sheet, handCounter, winnings)
