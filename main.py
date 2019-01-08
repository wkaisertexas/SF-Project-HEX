# imports
from _datetime import datetime  # this is used in order to version date the different experiments

import GUI
import os

# parameters

experiment_name = "MCTS"
experiment_version = 0

# this is the datetime that will be used in order to version date the program
start_time = datetime.now()


# this is the configuration file for the experiment (Application.json)


# this will initialize the GUI if required by the config file

class main():

  def __init__(self):
      if self.check_mode() == 0:
          print("Running Player VS Model")
      elif self.check_mode() == 1:
          print("")
      else:
          print("Error: Check mode not in range")
      return

  def check_mode(self):
    while True:
        print("Enter the mode you want the program to run in:")
        print("0 - Player vs Model")
        print("1 - Self Play Model Training")
        move = int(input("Answer: "))
        if move == 0 or move == 1:
            return move


  def train(self, times):
    return
  
  def test(self, times):
    return
  
    





