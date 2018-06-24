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

The AI-Player is at best a little better than the random player, sometimes even worse. But the classification is having an accuracy in testing of around 0.65, which is not really good, but better than random (which would be 0.5). These values are results from tests with a board side length of five, above that the AI becomes significantly worse.

Feel free to use the code for your own project at your own risk

Author: Henrik Jürgens
