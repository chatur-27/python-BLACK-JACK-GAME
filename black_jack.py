# IMPORTED RANDINT FOR ASSIGNING RANDOM CARDS TO PLAYER AND DEALER
from random import randint

# CONTAINS ALL THE FUNCTION AND ATTRIBUTES RELATED TO THE PLAYER
class player():
    balance=0                        # TOTAL AMOUNT THAT PLAYER HAS 
    def __init__(self):    
        self.points =0               # TOTAL VALUES OF ALL CARDS THAT PLAYER HAS
        self.hit=0                   # CARD THAT PLAYER GETS DURING EVERY HITTING (CHANGES EACH TIME DURING HITTING)
        self.mylist=[]               # LIST OF ALL CARD THAT PLAYER HAS
        self.mycards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']           # LIST OF DECK OF CARDS
         # A DICTIONARY TO STORE VALUE OF EVERY CARDS ( KEY 1 & 11 USED FOR ACE VALUES)  
        self.myvalues = {1:1,11:11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10} 
        self.amt=0                   # COLLECTS THE BETTING AMT EVERY ROUND
        self.new=0                   # A TEMP VARIABLE TO AVOID REPITION IN CALC OF ACE VALUES
        
    # GIVES THE INTRO ABT THE GAME (EXECUTES ONLY ONCE)
    def intro(self):
        print('\t\tWELCOME TO BLACK JACK GAME :: ')
        print('\nThe rules are as follows :')
        print("The goal of blackjack is to beat the dealer's hand without going over 21.")
        print('Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.')
        print("Each player starts with two cards, one of the dealer's cards is hidden until the end.")
        print("To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.")
        print('If you go over 21 you bust, and the dealer wins regardless of the dealers hand.')
        print('If you are dealt 21 from the start (Ace & 10), you got a blackjack.')
        print('Blackjack usually means you win 1.5 the amount of your bet.')
        print('Dealer will hit until his/her cards total 17 or higher.')
        print('Doubling is like a hit, only the bet is doubled and you only get one more card.')
        print('*'*100)
    
    # ASKS THE PLAYER TO PLAY OR NOT, IF YES ASKS FOR THE BETTING MONEY
    def play(self):
        while True:
            choose = input('So do you wanna play ? (yes/no) ::  ')
            
            if choose.lower() == 'yes':
                while True:
                    try:
                        self.amt=float(input('\nEnter the amount of bet you wanna play :: '))
                    except:
                        print(' Please enter a valid betting amount ::  ')
                
                    else:
                        if self.amt<=0:
                            print('Money not sufficient ::')
                        if self.amt > self.balance:
                            print('You dont have enough betting money ::  ')
                            return False
                        if self.balance==0 :
                            print('you dont have sufficient enough money for betting Bye...  :: ')
                            return False
                        else:
                            return True
                    
            elif choose.lower()== 'no':
                print('see you again bye...')
                return False
                
            else:
                print('{} is not a valid option :: '.format(choose))
            

    # ASSIGNS ALL OPEN CARDS AND CLOSED CARDS TO BOTH PLAYER AND DEALER
    def cards(self):   
        self.p1 = self.mycards[randint(0,12)]
        self.p2 = self.mycards[randint(0,12)]
        self.d1 = self.mycards[randint(0,12)]
        self.d2 = self.mycards[randint(0,12)]
        
        self.mylist.append(self.p1)
        self.mylist.append(self.p2)
    
    #DISPLAYS THE OPEN CARDS OF PLAYER AND DEALER (CLOSED CARD IS NOT DISPLAYED)
    def display(self):
        if self.hit==0:                        # DISPLAYS ALL OPEN CARDS AT FIRST
            print('*'*100)
            print(' \nYour open cards are :: ')
            print('\topen card 1 : ',self.p1)
            print('\topen card 2 : ',self.p2)
            print('')
            print("\tDealer's open card is : ",self.d1)
        
        if self.hit !=0:                       # DISPLAYS ALL OPEN CARDS AFTER HITTING
            print('\nYour open cards are : ',)
            for x in range(len(self.mylist)):
                print('\topen card {} : {}'.format(x+1,self.mylist[x]))
                
        if self.p1=='A':                       # IF ACE IS PRESENT IN FIRST OPEN CARDS ITSELF THEN ASKS FOR ITS VALUE (1/11)
            temp=self.acevalue()               # ACEVALUE() ASKS PLAYER FOR VALUE OF ACE AND RETURNS 1 OR 11
            if temp==1:
                self.p1=1                      # ASSIGNS 'A' AS 1 OR 11 BY PLAYER'S WISH
            else:
                self.p1=11
        if self.p2=='A':
            temp=self.acevalue()
            if temp==1:
                self.p2=1
            else:
                self.p2=11 
                
    # SUMS UP ALL CARD POINTS AND STORES IN SELF.POINTS
    def calc(self):
                       
        if self.hit ==0:                      # EXECUTES AT START (BEFORE HITTING)
            self.points =self.myvalues[self.p1] + self.myvalues[self.p2]
        else:                                 # EXECUTES LATER (AFTER HITTING)
            self.points +=  self.myvalues[self.hit]
                              
    # ASKS PLAYER FOR ACE VALUE AND RETURNS THAT VALUE
    def acevalue(self):
        if (self.points + 11) <=21:
            print(' A value is taken as 11 :: ')
            return 11
        else:
            print(' A value is taken as 1 :: ')
            return 1

    # CHECKS IF THE PLAYER POINTS EXCEEDS 21 OR NOT           
    def validity(self):
        if self.points <=21:
            return True
        else:
            return False
            
    # ASKS PLAYER FOR HITTING OR STANDING
    def decision(self):     
        while True:

            hit_stand = input('\ndo you wanna hit or stand :: (hit/stand) ')
            if hit_stand.lower()=='hit':
                self.hitting()                     # AFTER HITTING DOES CALCULATION AND CHECKS VALIDITY(IF <21) AND CONTINUES
                self.calc()
                temp=self.validity()
                if temp:
                    continue
                else:                              # IF VALIDITY FAILS(IF >21), REPORTS DEALER HAS WON
                    if (self.p1==11 or self.p2==11 or self.hit==11) and self.points > 21:
                        self.points -= 10
                        print(' Ace value is taken as 1 now :: ')
                        continue
                    print('*'*100)       
                    print('\nDealer has won :: ')
                    print('\nYou have lost :: rs',self.amt)
                    print('You have got {} points '.format(self.points))
                    self.balance -= self.amt
                    print('\nNow you have a total balance of {} :: '.format(self.balance))
                    return True                    # RETURNS TRUE TO CHECK FOR PLAY AGAIN?
            elif hit_stand.lower()=='stand':
                self.standing()                    # AFTER STANDING, BREAKS (THE PART FROM PLAYER'S SIDE IS OVER)
                break
            else:
                print('{} is not a valid option :: '.format(hit_stand))
    
    def hitting(self):
        self.hit = self.mycards[randint(0,12)]
        print('*'*100)
        print('\nyour new open card is : ',self.hit)
        self.mylist.append(self.hit)                # APPENDS THE NEW CARD TO THE LIST
        self.display()
        if self.hit=='A':                           # IF NEW CARDS IS AN ACE, AGAIN ASKS FOR AN ACE VALUE AND ASSIGNS TO IT
            temp=self.acevalue()
            if temp==1:
                self.hit=1
            else:
                self.hit=11
             
    
    def standing(self):                             # SUBMITS ALL THE DETAILS FROM PLAYER'S PART
        print('*'*100)
        print("\nSubmitting player's final details" )
        self.display()
        print('Total points = ',self.points)
        print('*'*100)
        print("\n\t\t\tNow dealer's turn")
        
    def checkblackjack(self):                       # CHECKS AT THE START, IF THE GIVEN SET IS AN BLACKJACK
        if self.p1==11 or self.p2==11:              # CHECKS FOR 11 BCOZ 'A' IS CHANGED TO 11 AFTER ACEVALUE()
            if self.p1 in [10,'J','Q','K'] or self.p2 in [10,'J','Q','K']:
                print('\nCongrats thats a BLACK JACK, YOU WON ::')
                self.amt = self.amt * 1.5
                print('\n\tyou have won  rs{} '.format(self.amt))
                self.balance+= self.amt
                print('\nNow you have a total balance of {}'.format(self.balance))
                return True                         # RETURNS TRUE TO CHECK FOR PLAY AGAIN?
        
    def replay(self):
        self.__init__()                             # RESETS EVERY VALUE TO INITIAL STATE
    
    # ASKS FOR A DOUBLE DOWN AND CHECKS VALIDITY AND RETURNS VALUES ACCORDINGLY
    def double_down(self):
        while True:
            double = input('\nDo you wanna double down your bet? (yes/no) :: ')
            if double.lower()=='yes':
                if (2*self.amt) > self.balance:
                    print('Sry you dont have sufficient balance to double down :: ')
                    return 'no'
                
                self.amt += self.amt
                
                self.hit = self.mycards[randint(0,12)]
                print('\n\t\tThe card you get after double down is :: ',self.hit)
                self.mylist.append(self.hit)                # APPENDS THE NEW CARD TO THE LIST
                self.display()
            
                if self.hit=='A':                      # IF NEW CARDS IS AN ACE, AGAIN ASKS FOR AN ACE VALUE AND ASSIGNS TO IT
                    temp=self.acevalue()
                    if temp==1:
                        self.hit=1
                    else:
                        self.hit=11
                self.points = self.myvalues[self.p1] + self.myvalues[self.p2] + self.myvalues[self.hit]
                print('\nTotal points = ',self.points)
                if self.validity():
                    return 'yes'
                else:
                    print('*'*100)       
                    print('\nDealer has won :: ')
                    print('\nYou have lost :: rs',self.amt)
                    print('You have got {} points '.format(self.points))
                    self.balance -= self.amt       # DEDUCTS THE BETTING AMT FROM TOTAL BALANCE
                    print('\nNow you have a total balance of {} :: '.format(self.balance))
                    return 'gameover'    
            
            elif double.lower()=='no':
                return 'no'
            else:
                print('\nEnter a valid value :: ')        

###################################################### CLASS DEALER ###################################################################

# CONTAINS ALL THE FUNCTION AND ATTRIBUTES RELATED TO THE DEALER
class dealer(player):     
    def __init__(self):
        self.list=[]                # STORES THE LIST OF DEALER'S CARDS
        self.hit=0                  # CARD THAT DEALER GETS DURING EVERY HITTING (CHANGES EACH TIME DURING HITTING)
        self.result = 0             # TOTAL VALUES OF ALL CARDS THAT DEALER HAS (LIKE SELF.POINS FOR PLAYER)
    
    # DISPLAYS ALL DEALERS CARDS (INCLUDING CLOSED CARD) AND AGAIN SIMILAR PROCEDURES AS THAT OF PLAYER (CHECKING FOR ACE)
    def display(self):
        if self.hit ==0:
            print('\nDealers cards are :: ')
            print('\t\topen card was : ',instance.d1)
            print('\t\tdown card was : ',instance.d2)
            self.list.append(instance.d1)
            self.list.append(instance.d2)
            
        if self.hit != 0:
            print("\nDealer's cards are ::" )
            for x in range(len(self.list)):
                print('\t\tDealer card {} : {}'.format(x+1,self.list[x]))  
                
        if instance.d1=='A':
            temp=self.acevalue()
            if temp==1:
                instance.d1=1
            elif temp==11:
                instance.d1=11
                
        if instance.d2=='A':
            temp=self.acevalue()
            if temp==1:
                instance.d2=1
            elif temp==11:
                instance.d2=11
                
    # SUMS UP ALL CARD POINTS AND STORES IN SELF.RESULT
    def calc(self):              
        if self.hit ==0:         # BEFORE HITTING
            self.result = instance.myvalues[instance.d1] + instance.myvalues[instance.d2]
        else:                    # AFTER HITTING
            self.result +=  instance.myvalues[self.hit]
        
    # ASSIGNS ACE VALUE AUTOMATICALLY AS PER SITUATION
    def acevalue(self):
        if (self.result + 11) <=21:
            print(' A value is taken as 11 :: ')
            return 11
        else:
            print(' A value is taken as 1 :: ')
            return 1
    
    # HITS AUTOMATICALLY UNTIL PLAYER OR DEALER WINS
    def hitting(self):
        while True:
            print('*'*100)
            print('\n\t\t\t\tDealer hits')
            dealerhit = input('press any key so that dealer hits :: ')
            print('total points = ',self.result)
            self.hit = instance.mycards[randint(0,12)]
            print("\nDealer's new card is : ",self.hit)
            self.list.append(self.hit)
            self.display()
            if self.hit=='A':                  # CHECKS FOR ACE VALUE
                temp=self.acevalue()
                if temp==1:
                    self.hit=1
                elif temp==11:
                    self.hit=11
            
            self.calc()
            if self.validity():               # CHECKS FOR VALIDITY (IF <17) CONTINUES HITTING
                if self.precheck():
                    return True
                continue
            else:
                if self.final():              # OTHERWISE DISPLAYS FINAL RESULTS AND RETURNS TRUE FOR PLAYING AGAIN CONDITION
                    return True
                
     # DISPLAYS FINAL RESULT AS WHO WON BASED ON THESE CONDITIONS   
    def final(self):
        if self.result >21 or (abs(21-self.result) > abs(21 - instance.points)):
            if (instance.d1==11 or instance.d2==11 or self.hit==11) and self.result > 21:
                        self.result -= 10
                        print(' Ace value is taken as 1 now :: ')
                        self.hitting()
                        return 'nothing'
            print('*'*100)
            print('\nYou have won :: ')
            instance.display()
            self.display()
            print('\nYou have won :: rs {}'.format(instance.amt))
            print('\nDealer has got {} points and you have got {} points'.format(self.result,instance.points))
            instance.balance += instance.amt
            print('\nNow you have a total balance of {} :: '.format(instance.balance))
            print('*'*100)
            return True
        
        elif abs(21-self.result) < abs(21 - instance.points):
            print('*'*100)
            print('\nDealer has won :: ')
            instance.display()
            self.display()
            print('\nYou have lost :: rs',instance.amt)
            print('\nDealer has got {} points and you have got {} points'.format(self.result,instance.points))
            instance.balance -= instance.amt
            print('\nNow you have a total balance of {} :: '.format(instance.balance))
            print('*'*100)
            return True
            
        
        elif self.result == instance.points :
            print('\t\tMatch Tied ')
            print('Both player and dealer got same points :: ')
            print('Now you have a balance of rs ',instance.balance)
            return True
            
             
    # CHECKS FOR VALIDITY FOR POINTS OF THE DEALER
    def validity(self):
        if self.result < 17:
            return True
        else:
            return False
        
    # CHECKS IF DEALER HAS WON BEFORE GETTING 17 POINTS 
    def precheck(self):
        temp = self.validity()
        if temp:
            if self.result > instance.points:
                print('*'*100)
                print('\nDealer has won :: ')
                instance.display()
                self.display()
                print('\nYou have lost :: rs',instance.amt)
                print('\nDealer has got {} points and you have got {} points'.format(self.result,instance.points))
                instance.balance -= instance.amt
                print('\nNow you have a total balance of {} :: '.format(instance.balance))
                print('*'*100)
                return True
                  
###################################################### MAIN PROGRAM ###############################################################

instance= player()                   # (AUTOMATICALLY INIT FUNCTION IS CALLED NOW)  
instance.intro()                     # DISPLAYS RULES OF THE GAME

# GETS THE TOTAL MONEY THAT A PLAYER HAS (NOT BETTING MONEY)
while True:
    try:
        instance.balance = float(input('\nEnter the total amount of money you have :: '))
    except:
        print('Enter valid amount ')
    else:
        if instance.balance <=0:
            print('Money not sufficient :: ')
            continue
        break

# REPEATS THE PROGRAM UNTIL PLAYER DECIDES NOT TO PLAY OR OUT OF MONEY
while True:
    local=0
    if not instance.play():   # EXITS THE LOOP IF THE PLAYERS SELECTS 'NO' IN "IF YOU WANNA PLAY CONDITION"
        break
    instance.cards()
    instance.display()
    instance.calc()
    temp = instance.double_down()
    if temp=='yes':
        local=1
    elif temp=='no':
        pass
    elif temp=='gameover':
        instance.replay()
        continue
    if local==0: 
        if instance.checkblackjack():
            instance.replay()    # RESETS EVERY ATTRIBUTE SO THE GAME STARTS FRESH AGAIN
            continue             # IF THE PLAYER GOT BLACKJACK, ASKS FOR THE PLAYER DO U WANNA PLAY AGAIN
        if instance.decision():
            instance.replay()
            continue             # IF THE PLAYER LOSES BY HITTING,ASKS FOR THE PLAYER DO U WANNA PLAY AGAIN
    

    dinst = dealer()
    
    dinst.display()
    dinst.calc()
    if dinst.precheck():
        instance.replay()
        continue
        
    if not dinst.validity(): # IF VALDITY(>17) FAILS BEFORE HITTING (DEALER LOSES OR WINS BEFORE HITTING), ASKS FOR REMATCH
        if dinst.final():
            instance.replay()
            continue
    if dinst.hitting():      # ASKS FOR REMATACH, AFTER DEALER WINS OR LOSES BY HITTING
        instance.replay()
        continue

