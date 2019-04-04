#!/usr/bin/env python
# -*- coding: utf-8 -*-



# core modules
import logging.config
import math
import pkg_resources
import random

# 3rd party modules
from gym import spaces
import cfg_load
import gym
import numpy as np



def get_chance(x):
 
    e = math.exp(1)
    return (1.0 + e) / (1. + math.exp(x + 1))

def displayBoard(board):
    print()
    print()
    for ar in board:
        for elem in ar:
            print(elem, end="")
        print()
class MazeEnv(gym.Env):
   

    def __init__(self):
        self.__version__ = "0.1.0"
        logging.info("MazeEnv - Version {}".format(self.__version__))

        #setting up maze
        self.board = [[" " for x in range(0, 10)] for x in range(0, 10)]
        self.currentSpot = self.setupBoard()
        self.isEnd = False
        #setting up action space
        self.action_space = spaces.Discrete(4)
        
        #observation space   low = 0, high - 10
        #self.observation_space = spaces.Box(0, 10)

        #current step
        self.currentStep = -1
        self.MAXSTEPS = 20

        #all actions
        self.pastActions = [None]

        #variable to pass reward from functions
        self.reward = 0

    def step(self, action):
        
        #if(self.isEnd):
         #   raise RuntimeError("end")
        self.pastActions.append(action)
        holder = self.getInput(self.currentSpot, self.board, x = action)
        self.currentSpot = holder[0]
        self.isEnd = holder[1]
        self.currentStep += 1
        
        reward = self._get_reward()
        return [self.MAXSTEPS - self.currentStep], reward, self.isEnd, {} #self.isEnd may need to be changed

    
    
    def reset(self):
     
        self.board = [[" " for x in range(0, 10)] for x in range(0, 10)]
        self.currentSpot = self.setupBoard()
        return 

    def render(self, mode='human', close=False):
        print(self.pastActions[-1])
        displayBoard(self.board)
        return

    
    def seed(self, seed):
        random.seed(seed)
        np.random.seed



    def setupBoard(self):
        for x in range(1, len(self.board)):
            self.board[x][0] = "|"
            self.board[x][-1] = "|"
        for x in range(1, len(self.board) - 1):
            self.board[0][x] = "_"
            self.board[-1][x] = "_"
    
        opening = (random.random() * (len(self.board) - 2)) + 1
        self.board[math.floor(opening)][0] = " " #opening up here
        self.board[math.floor(opening)][1] = "X"
        closing = (random.random() * (len(self.board) - 2)) + 1
        self.board[math.floor(closing)][-1] = "T"
        self.endY = math.floor(closing)
        #print("math floor of opening" + str(math.floor(opening)))
        #self.currentSpot = math.floor(opening)
        return [math.floor(opening), 1]



    def getInput(self, cs, board, x): #0 up, 1 right, 2 down, 3 left
        #x = input() #make a method to send this
        row = cs[0]
        col = cs[1]
        if int(x) == 0:
            row -= 1
        if int(x) == 1:
            col += 1
        if int(x) == 2:
            row += 1
        if int(x) == 3:
            col -= 1

        if(board[row][col] == "T"):
            self.reward = 2
            return [cs, True] # they won

        if (board[row][col] == "|" or board[row][col] == "_"):
            self.reward =1
            return [cs, True] # they lost
        cs[0] = row
        cs[1] = col
        self.reward = 0
        board[int(cs[0])][ int(cs[1])] = "X"
    
        return [cs, False]
    def _get_reward(self):
       
        self.bLength = len(self.board) - 1
        if self.reward == 2:
            return 0
        if self.reward == 1:
            return 100
        
        return math.sqrt(   ((self.currentSpot[0] - self.bLength) ** 2) + ((self.currentSpot[1] - self.endY) ** 2) )


