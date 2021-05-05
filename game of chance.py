# user can bet on any number from 0 to 30.
# If it is an even number they get x2 money back
# if it is a multiple of 10 they get x3 money back
# if it is a prime number they get x5 money back
# if number below 5 they get x2 bonus

# user guesses number and if it is correct they get a bonus
# e.g. 20  means a bonus of 2 x 3 = x6 their money

# allow user to enter the amount they want to bet and work out the bonus they recieve
# store the user's current balance and stop them from betting if they have no money left.
# the user cannot enter into a negative amount of cash
# input should be between 1 and 10 units of currency
# allow multiple bets on different numbers

import random

class Player():
    def __init__(self):
        self.bets = []
        self.money = 100
        self.bet_money = 0
        self.correct_bet = False
        self.can_bet = False

    def check_prime(self, num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False
        

    def bet_cash(self):
        random_num = random.randint(0,31)
        
        while True:
            num = int(input("number to bet on (0-30):"))
            bet = int(input("amount to bet (number can be up to 10 digits long): £ "))  
            
            if num < 0 or num > 30:
                print("number out of range try again")
            elif self.money - self.bet_money < 0:
                print("you do not have enough money available")
            elif len(str(bet)) > 10 or bet < 0:
                print("you cannot bet that much")
            else:
                self.bets.append(num)
                self.bet_money += bet
                self.can_bet = True
              
            another_bet = input("would you like to bet on another number (y/n): ")

            if another_bet == "n":
                 break

        if self.can_bet:
            for number in self.bets:
                if number == random_num:
                    print()
                    print("you have guessed correctly")
                    self.correct_bet = True
                    break
            else:
                self.money -= self.bet_money
                print()
                print("sorry, incorrect bet")
                print("the actual number is :", random_num)

            if self.correct_bet:
                if random_num  % 2 == 0:
                    self.bet_money = self.bet_money*2
                    
                if random_num % 10 == 0:
                    self.bet_money = self.bet_money*3
                    
                if self.check_prime(random_num):
                    self.bet_money = self.bet_money*5

                if random_num < 5:
                    self.bet_money = self.bet_money*5

                self.money += self.bet_money
                
                print()
                print("you have won: £", self.bet_money)
                
            print()
            print("you have currently: ", self.money)

            self.bet_money = 0
            self.bets = []
            self.correct_bet = False
            self.can_bet = False
                

kate = Player()

while True:
    print()
    go = input("do you want to bet: (y/n): ")

    if go == "y":
        kate.bet_cash()
    elif go == "n":
        break
    else:
        print("cannot understand :(")
