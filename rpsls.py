#!/usr/bin/python

"""
This is a simulator of the game Rock-Paper_Scissors-Lizard-Spock
from The Big Bang Theory

The rules of Rock-Paper-Scissors-Lizard-Spock are:

    Scissors cut Paper
    Paper covers Rock
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitate Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock breaks Scissors

"""
import random

def selectComputerThrow():
   list = ['rock','paper','scissors','lizard','spock']
   return random.choice(list)
    
def selectUserThrow():
   print "The computer has made its selection."
   list = ['rock','paper','scissors','lizard','spock']
   print "Please select one of the following options:"
   print "\t1: Rock"
   print "\t2: Paper"
   print "\t3: Scissors"
   print "\t4: Lizard"
   print "\t5: Spock"
   selection = raw_input("Selection: ")
   return list[int(selection)-1]

def determineResults(computer, player):
    if computer == "rock":
        if player == "rock":
            print "Rock vs Rock results in a tie"
        elif player == "paper":
            print "Paper covers Rock.  The player wins!!"
        elif player == "scissors":
            print "Rock breaks Scissors.  The computer wins!!"
        elif player == "lizard":
            print "Rock crushes Lizard.  The computer wins!!"
        elif player == "spock":
            print "Spock vaporizes Rock.  The player wins!!"
    elif computer == "paper":
        if player == "rock":
            print "Paper covers Rock.  The computer wins!!"
        elif player == "paper":
            print "Paper vs Paper results in a tie"
        elif player == "scissors":
            print "Scissors cut Paper.  The player wins!!"
        elif player == "lizard":
            print "Lizard eats Paper.  The player wins!!"
        elif player == "spock":
            print "Paper disproves Spock.  The computer wins!!"
    elif computer == "scissors":
        if player == "rock":
            print "Rock breaks Scissors.  The player wins!!"
        elif player == "paper":
            print "Scissors cut Paper.  The computer wins!!"
        elif player == "scissors":
            print "Scissors vs Scissors results in a tie"
        elif player == "lizard":
            print "Scissors decapitate Lizard.  The computer wins!!"
        elif player == "spock":
            print "Spock smashes Scissors.  The player wins!!"
    elif computer == "lizard":
        if player == "rock":
            print "Rock crushes Lizard.  The player wins!!"
        elif player == "paper":
            print "Lizard eats Paper.  The computer wins!!"
        elif player == "scissors":
            print "Scissors decapitate Lizard. The player wins!!"
        elif player == "lizard":
            print "Lizard vs Lizard results in a tie"
        elif player == "spock":
            print "Lizard poisons Spock.  The computer wins!!"
    elif computer == "spock":
        if player == "rock":
            print "Spock vaporizes Rock.  The computer wins!!"
        elif player == "paper":
            print "Paper disproves Spock. The player wins!!"
        elif player == "scissors":
            print "Spock smashes Scissors.  The computer wins!!"
        elif player == "lizard":
            print "Lizard poisons Spock.  The player wins!!"
        elif player == "spock":
            print "Spock vs Spock results in a tie"
    else:
        print "Something broke... exiting!!!"
    #exit with error
    
if __name__ == "__main__":
    determineResults(selectComputerThrow(),selectUserThrow())
