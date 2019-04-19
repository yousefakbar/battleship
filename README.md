# BATTLESHIP

## Purpose

Battleship is a classic board game (AxB grid) with the aim of guessing and shooting enemy ships.

This is a python project I worked on in high school as part of my overall grade. The aim was to recreate a simple game using concepts taught in class.

## Directions

To play, simply download the .py and run it with your local version of python.

Alternatively, you can pull to your desired location using git:


  git pull https://github.com/yousefakbar/battleship.git

and launch it from there.

## How to play

When launched, the game generates a 5x5 grid with letters for rows and numbers for columns. Here is what the grid looks like:

![Image of example grid](/grid.png)

When initiated, the game generates 5 ship locations and scatters them around the map.

Information about each grid element is stored in a 3-dimensional list. Information stored consists of co-ordinates, hit status, and ship_piece boolean value.

Status symbols: □ = Available, X = Not Available, # = Ship.

The game is won when all 5 ship pieces are destroyed. You cannot lose :).

## Concepts mastered in this project

* RNG number generation
* List functionality and manipulation
* Usage of multi-dimensional lists as arrays
* While loops as a simple basis for gameplay
* Formatting print statements to display nicely

# Enjoy!
