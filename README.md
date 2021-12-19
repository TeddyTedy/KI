# Implementation of the A* search algorithm for a moving labyrinth

As part of university project assignment of the artificial intelligence course of the Baden-Württemberg Cooperative State University, this repo implements the A* search algorithm for a moving labyrinth.

## Structure of the repository

- [Code](/Code)
- [Input Data](/Input)
- [Task Assignment (German)](/Aufgabenstellung)
- [Documentation (German)](/Documentation)

## Problem description

- The goal of the player is to traverse the two-dimensional, moving labyrinth from its starting to position to a defined goal position
- There are a different types of tiles if different access towards other tiles, specifying which surrounding tiles the player is able to reach.
- Additionally, there is one free tile which can be inserted at predefined positions, altering the labyrinth and potentially even the position of the player if he stands on a labyrinth tile that is affected
- if the player is pushed out of the labyrinth, he immediately is set at the position of the tile which insertion has pushed him out
- The goal is to reach the goal destination with minimal cost, every tile insertion costs one unit while player movements are free from any costs

## Game Visualization

![Visualization of the two dimensional labyrinth grid, tile input locations and more](/Other/Game_Visualisation.png "Game Visualization")

## Game Execution

(Depens on OS, example below for Ubuntu 18.04)

python3 Path_To_main.py/main.py Path_to_input_File/input.json 
