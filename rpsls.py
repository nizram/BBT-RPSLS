#!/usr/bin/python

"""
This is a simulator of the game Rock-Paper_Scissors-Lizard-Spock
from The Big Bang Theory

The rules of Rock-paper-scissors-lizard-Spock are:

    Scissors cut paper
    Paper covers rock
    Rock crushes lizard
    Lizard poisons Spock
    Spock smashes (or melts) scissors
    Scissors decapitate lizard
    Lizard eats paper
    Paper disproves Spock
    Spock vaporizes rock
    Rock breaks scissors

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

   #return (selection)

def determineResults(computer, user):
    if computer == user:
        return "tie"
    else:
        print "Something broke... exiting!!!"
    #exit with error
    
if __name__ == "__main__":
    selectUserThrow()
