# FiveInARow
## Requirements
Python 3.6 or higher, Tensorflow, tflearn, numpy

## Purpose of this project

This project is purely for learning purposes. It was made to learn about different machine learning techniques with tensorflow and tflearn.

## Goal of this project and approach

The goal of this project was to create a Deep-Learning AI for Five in A Row also known as Gomoku. The approach is to simulate random Five In A Row-games and train a classifier, so that it can decide weather a game is lost or won. By that it is meant to learn the goal of the game. When the AI is playing, it classifies every next possible move and choses the one, which looks closest to a win.
There are research Papers that indicate pure AI approaches (No MCTS) do not work so well for this game, like this one: 

http://cs231n.stanford.edu/reports/2016/pdfs/109_Report.pdf

Here you can find a better implementation of Gomoku training and using heuristics for an computer player: 

http://britlovefan.github.io/AI_Five-in-row/

## State of this project

The AI-Player is at best a little better than the random player, sometimes even worse. But the classification is having an accuracy in testing of around 0.65, which is not really good, but better than random (which would be 0.5).

Feel free to use the code for your own project at your own risk

## A message from future self: Why this does not work
First of all a accuracy of 0.65 percent is way too low, probably the network is not big enough and is underfitting. You should always check the training history to see, if the network is overfitting or underfitting.
It might actually make sense to train the network on just the pure winning (i.e. five crosses in a row, randomly placed) configurations first, so that the conv-layers can get into the right shape.
It might also make sense to have crosses as color 0, circles as 255 and empty boxes as 127.
If the cnn has an accuracy of over 90% for the pre to last frame, it might make sense to do a tree search for the game and use the cnn for pruning. 
Maybe I will get back to this project some day, but probably not too soon, since I have some more exciting projects coming up!

Author: Henrik Jürgens
