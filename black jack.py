from tkinter import *
from tkinter import font

import random



from tkinter import *
from tkinter import font

import random


class  Player:
    def __init__(self,name) :
        self.name=name
        self.cards = []
        self.N=0
        self.over=FALSE
    def inHand(self):
        return self.N
    def addCard(self,c):
        self.cards.append(c)
        self.N+=1
    def reset(self):
        self.N = 0
        self.cards.clear()
    def value(self):
        value=0
        for i in self.cards:
            i=Card.getValue(i)
            D=0
            if i in(2,3,4,5,6,7,8,9,10):
                value+=i
            elif i ==1:
                D="1"
            if D == "1" and value+11 <=21:
                value+=11
                self.over=TRUE
            elif D =="1" and value+11 > 21:
                value+=1
                self.over=TRUE
        if self.over == TRUE and value>21:
            value-=10
            self.over=FALSE
        return value
            
class Card:
    def __init__(self,temp):
        self.value = temp%13+1
        self.x = temp//13
    def getValue(self):
        if self.value>10:
            return 10
        else:
            return self.value
    def getsuit(self):
        if self.x==0:
            self.suit = "클로버"
        elif self.x==1:
            self.suit = "스페이드"
        elif self.x==2:
            self.suit = "하트"
        else:
            self.suit = "다이아"
        return self.suit
    def filename(self):
        return self.getsuit() + str(self.value)+".png"

class blackjack:
    def __init__(self):
        self.savemoney=0
        self.window = Tk()
        self.window.title("BLACK JACK")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstlye = font.Font(self.window, size=24, weight='bold',family='Consolas')
        self.fontstlye2 = font.Font(self.window, size=16, weight='bold',family='Consolas')
        self.setupButton()
        self.setupLabel()

        self.player = Player("player")
        self.dealer = Player("dealer")
        self.betMoney = 0
        self.playerMoney =1000
        self.nCardsDealer=0
        self.nCardsPlayer=0
        self.LcardsDealer=[]
        self.LcardsPlayer=[]
        self.deckN=0
        self.window.mainloop()
    def setupButton(self):
        self.B50=Button(self.window, text="Bet 50", width=6, height=1, font=self.fontstlye2,command=self.pressedB50)
        self.B50.place(x=50,y=500)
        self.B10=Button(self.window, text="Bet 10", width=6, height=1, font=self.fontstlye2,command=self.pressedB10)
        self.B10.place(x=150,y=500)
        self.B1=Button(self.window, text="Bet 1", width=6, height=1, font=self.fontstlye2,command=self.pressedB1)
        self.B1.place(x=250,y=500)
        self.Hit=Button(self.window, text="Hit", width=6, height=1, font=self.fontstlye2,command=self.pressedHit)
        self.Hit.place(x=400,y=500)
        self.Stay=Button(self.window, text="Stay", width=6, height=1, font=self.fontstlye2,command=self.stay)
        self.Stay.place(x=500,y=500)
        self.Deal=Button(self.window, text="Deal", width=6, height=1, font=self.fontstlye2,command=self.deal)
        self.Deal.place(x=600,y=500)
        self.again=Button(self.window, text="again", width=6, height=1, font=self.fontstlye2,command=self.pressedagain)
        self.again.place(x=700,y=500)

        self.Hit['state']='disabled'
        self.Hit['bg']='gray'
        self.Stay['state']='disabled'
        self.Stay['bg']='gray'
        self.Deal['state']='disabled'
        self.Deal['bg']='gray'
        self.again['state']='disabled'
        self.again['bg']='gray'

    def setupLabel(self):
        self.LbetMoney = Label(text="$0",width=4,height=1,font=self.fontstlye,bg="green",fg="cyan")
        self.LbetMoney.place(x=200,y=450)
        self.LplayerMoney = Label(text="당신이 소유한 돈:$1000",width=30,height=1,font=self.fontstlye,bg="green",fg="cyan")
        self.LplayerMoney.place(x=280,y=450)
        self.LplayerPts = Label(text="",width=2,height=1,font=self.fontstlye2,bg="green",fg="white")
        self.LplayerPts.place(x=300,y=300)
        self.LdealerPts = Label(text="",width=2,height=1,font=self.fontstlye2,bg="green",fg="white")
        self.LdealerPts.place(x=300,y=100)
        self.Lstatus = Label(text="",width=15,height=1,font=self.fontstlye,bg="green",fg="white")
        self.Lstatus.place(x=500,y=300)

    def pressedB50(self):
        self.betMoney+=50
        if self.betMoney<= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney-=50
            self.LplayerMoney.configure(text="당신이 소유한 돈:$"+str(self.playerMoney))
            self.Deal["state"]="active"
            self.Deal["bg"]="white"
        else:
            self.betMoney-=50

    def pressedB10(self):
        self.betMoney+=10
        if self.betMoney<= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney-=10
            self.LplayerMoney.configure(text="당신이 소유한 돈:$"+str(self.playerMoney))
            self.Deal["state"]="active"
            self.Deal["bg"]="white"
        else:
            self.betMoney-=10

    def pressedB1(self):
        self.betMoney+=1
        if self.betMoney<= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney-=1
            self.LplayerMoney.configure(text="당신이 소유한 돈:$"+str(self.playerMoney))
            self.Deal["state"]="active"
            self.Deal["bg"]="white"
        else:
            self.betMoney-=1
            
    def deal(self):
        self.player.reset()
        self.dealer.reset()
        self.cardDeck = [i for i in  range(52)]
        random.shuffle(self.cardDeck)
        self.deckN=0

        self.hitPlayer(0)
        self.hitDealerDown()
        self.hitPlayer(1)
        self.hitDealer(0)
        self.nCardsPlayer =1
        self.nCardsDealer =0

        self.B50['state']='disabled'
        self.B50['bg']='gray'
        self.B10['state']='disabled'
        self.B10['bg']='gray'
        self.B1['state']='disabled'
        self.B1['bg']='gray'
        self.Hit['state']='active'
        self.Hit['bg']='white'
        self.Stay['state']='active'
        self.Stay['bg']='white'
        self.Deal['state']='disable'
        self.Deal['bg']='gray'
    def hitPlayer(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN+=1
        self.player.addCard(newCard)
        p=PhotoImage(file="card/"+newCard.filename())
        self.LcardsPlayer.append(Label(self.window,image=p))
        self.LcardsPlayer[self.player.inHand()-1].image=p
        self.LcardsPlayer[self.player.inHand()-1].place(x=250+n*30,y=350)
        self.LplayerPts.configure(text=str(self.player.value()))

    def hitDealerDown(self):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN+=1
        self.dealer.addCard(newCard)
        p=PhotoImage(file="card/back.png")
        self.LcardsDealer.append(Label(self.window,image=p))
        self.LcardsDealer[self.dealer.inHand()-1].image=p
        self.LcardsDealer[self.dealer.inHand()-1].place(x=250,y=150)

    def hitDealer(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN+=1
        self.dealer.addCard(newCard)
        p=PhotoImage(file="card/"+newCard.filename())
        self.LcardsDealer.append(Label(self.window,image=p))
        self.LcardsDealer[self.dealer.inHand()-1].image=p
        self.LcardsDealer[self.dealer.inHand()-1].place(x=280+n*30,y=150)
        self.LdealerPts.configure(text=str(self.dealer.value()))
    def stay(self):
        self.checkWinner()

    def pressedHit(self):
        self.nCardsPlayer+=1
        self.hitPlayer(self.nCardsPlayer)
        if self.player.value()>21:
            self.checkWinner()

    def checkWinner(self):
        p=PhotoImage(file="card/"+self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p)
        self.LcardsDealer[0].image=p
        n=0
        if self.dealer.value()<17:

            n+=1
            self.hitDealer(n)

        self.LdealerPts.configure(text=str(self.dealer.value()))
        
        if self.player.value()>21:
            self.Lstatus.configure(text="Player Bursts")
        elif self.dealer.value()>21:
            self.Lstatus.configure(text="Dealer Bursts")
            self.playerMoney+=self.betMoney*2
        elif self.dealer.value() ==self.player.value():
            self.Lstatus.configure(text='Push')
            self.playerMoney+=self.betMoney
        elif self.dealer.value() < self.player.value():
            self.Lstatus.configure(text='You Win!')
            self.playerMoney=+self.betMoney*2
        else:
            self.Lstatus.configure(text="You lost")
        self.betMoney = 0
        self.LplayerMoney.configure(text="당신이 소유한 돈:$"+str(self.playerMoney))

        self.B50['state']='disabled'
        self.B50['bg']='gray'
        self.B10['state']='disabled'
        self.B10['bg']='gray'
        self.B1['state']='disabled'
        self.B1['bg']='gray'
        self.Hit['state']='disabled'
        self.Hit['bg']='gray'
        self.Stay['state']='disabled'
        self.Stay['bg']='gray'
        self.Deal['state']='disabled'
        self.Deal['bg']='gray'
        self.again['state']='active'
        self.again['bg']='white'

    def pressedagain(self):
        self.LcardsPlayer.clear()
        self.LcardsDealer.clear()
        self.B50['state']='active'
        self.B50['bg']='white'
        self.B10['state']='active'
        self.B10['bg']='white'
        self.B1['state']='active'
        self.B1['bg']='white'
        self.reset()

    def reset(self):
        for wg in self.window.place_slaves(): # 전체 창 내부에 있는 위젯 하나씩 불러와서
            wg.destroy()  
        self.setupButton()
        self.setupLabel()
        self.savemoney=self.playerMoney
        self.LplayerMoney.configure(text="당신이 소유한 돈:$"+str(self.playerMoney))

blackjack()